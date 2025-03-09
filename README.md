# Large Scale Data Management - Streaming Project

## Overview

This project implements a streaming data pipeline using Apache Spark, Apache Kafka, and Apache Cassandra. The system simulates a movie rating service where users rate movies, with this data being processed in real-time.

## Project Components

### Part I: Data Generation

A Python script that:

- Creates a list of fake user names using the Faker library
- Periodically generates movie ratings (1-10) for each user
- Publishes these ratings to a Kafka topic
- Includes data such as user name, movie name, timestamp, and rating

### Part II: Data Processing and Storage

A PySpark streaming application that:

- Consumes the Kafka topic with movie ratings
- Processes the incoming data
- Stores the results in Cassandra with a schema optimized for time-based user queries
- Implements caching for performance optimization
- Processes data in configurable intervals (default: 30 seconds)

## Setup

### Prerequisites

- [Vagrant](https://www.vagrantfile.org/) and [VirtualBox](https://www.virtualbox.org/)
- Alternatively: Docker and Docker Compose

### Using Vagrant

1. Clone this repository
2. Navigate to the project directory
3. Run `vagrant up` to start the VM with all required services

### Using Docker

If you encounter issues with the VM setup, you can use Docker directly:

```bash
docker-compose -f docker-compose-kafka.yml up -d
docker-compose -f docker-compose-cassandra.yml up -d
docker-compose -f docker-compose-spark.yml up -d
```

## Running the Application

### Data Generator

```bash
python3 reviews-producer.py
```

### Spark Streaming Application

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0 reviews-consumer.py
```

Or start a PySpark shell:

```bash
pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0
```

## Cassandra Schema

The Cassandra data model is designed to efficiently support queries for specific users within time blocks:

```sql
CREATE TABLE reviews.records (
    name text,
    hour timestamp,
    time timestamp,
    movie text,
    rating int,
    PRIMARY KEY ((name, hour), time)
)
```

This schema uses a composite partition key of (name, hour) which allows efficient retrieval of all ratings for a specific user during a specific hour. The time field is used as a clustering column to sort entries within each partition chronologically.

## Querying Data

Example CQL queries for retrieving:

- Average rating of movies rated by a specific user during a particular hour:

  ```sql
  SELECT AVG(rating) AS avg_rating
  FROM reviews.records
  WHERE name = 'username' AND hour = '2025-03-15 10:00:00';
  ```

- Names of movies rated by a specific user during a particular hour:
  ```sql
  SELECT movie
  FROM reviews.records
  WHERE name = 'username' AND hour = '2025-03-15 10:00:00';
  ```

## Files

- `movie_rating_generator.py`: Kafka producer that generates simulated movie ratings
- `movie_rating_processor.py`: PySpark streaming job that processes and stores data
- `movies.csv`: Dataset containing movie information
- `README.md`: This file

## Requirements

- Python 3.6+
- Apache Spark 3.5.0
- Apache Kafka
- Apache Cassandra
- Python libraries: Faker, kafka-python
