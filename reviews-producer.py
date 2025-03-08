import pandas as pd
import json
import asyncio
import random
from aiokafka import AIOKafkaProducer
from faker import Faker
from datetime import datetime

topic = 'test'

def serializer(value):
    return json.dumps(value).encode()

def init_names(no_names=10):
    names = []

    for _ in range(no_names):
        names.append(fake.name())
    names.append('Michail Theofanopoulos')

    return names

async def produce(names, movies, processing_interval=30):
    
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:29092',
        value_serializer=serializer,
        compression_type="gzip")
    
    try:
      
      while True:
        await producer.start()

        name = random.choice(names)
        movie = random.choice(movies)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        rating = random.randint(1, 10)

        data = {"name": name, "movie": movie, "date": date, "rating": rating}
        await producer.send(topic, data)
        print(f"Sent: {data}")
        
        await asyncio.sleep(processing_interval)
    except KeyboardInterrupt:
        pass
    finally:
        # Close the producer when done
        await producer.stop()

# Create a Faker instance
fake = Faker()

no_names = 50
processing_interval = 50

movies_df = pd.read_csv('./data/movies.csv')
movies = movies_df.iloc[:, 0].tolist()
names = init_names(no_names)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(produce(names, movies, processing_interval))
