import pandas as pd
import json
import asyncio
import random
from aiokafka import AIOKafkaProducer
from faker import Faker

topic = 'test'

def serializer(value):
    return json.dumps(value).encode()

def init_names():
    names = []

    for _ in range(10):
        names.append(fake.name())
    names.append('Michail Theofanopoulos')

    return names

async def produce(names, movies):
    
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:29092',
        value_serializer=serializer,
        compression_type="gzip")
    
    try:
      
      id = 0

      while True:
        await producer.start()

        name = random.choice(names)
        movie = random.choice(movies)
        date = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
        rating = random.randint(1, 10)

        data = {"id": id, "name": name, "movie": movie, "date": date, "rating": rating}
        await producer.send(topic, data)
        print(f"Sent: {data}")

        id += 1
        
        await asyncio.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        # Close the producer when done
        await producer.stop()

# Create a Faker instance
fake = Faker()

movies_df = pd.read_csv('./data/movies.csv')
movies = movies_df.iloc[:, 0].tolist()
names = init_names()

id = 0

loop = asyncio.get_event_loop()
result = loop.run_until_complete(produce(names, movies))
