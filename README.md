# Hadoop MapReduce Examples

This repository contains examples of Hadoop MapReduce jobs for processing car sales data. The main goal is to demonstrate how to use Hadoop for data processing tasks.

## Project Overview

The project includes a MapReduce job that processes car sales data to calculate the maximum and average price differences for cars sold by different sellers in a given month.

### Key Components

- **Mapper**: Extracts relevant information from each record and emits key-value pairs.
- **Reducer**: Aggregates the data to calculate the maximum and average price differences.

## Prerequisites

- Docker
- Docker Compose
- Vagrant
- Maven
- Java 8

## Project Structure

- `src/main/java/gr/aueb/mapreduce/carsales/Driver.java`: Main class to set up and run the MapReduce job.
- `src/main/java/gr/aueb/mapreduce/carsales/WordCount.java`: Contains the Mapper and Reducer classes for processing the car sales data.
- `src/main/resources/car_prices.csv`: Sample input data file.
- `env/`: Contains Docker and Vagrant configuration files for setting up the Hadoop cluster.

## Running the Job

1. **Build the Project**: Use Maven to build the project and create the JAR file.
    ```sh
    mvn clean install
    ```

2. **Start the Hadoop Cluster**: Use Vagrant and Docker Compose to start the Hadoop cluster.
    ```sh
    cd env
    vagrant up
    ```

3. **Copy the JAR File**: Copy the built JAR file to the Hadoop namenode.
    ```sh
    docker cp target/hadoop-map-reduce-examples-1.0-SNAPSHOT-jar-with-dependencies.jar namenode:/
    ```

4. **Run the Hadoop Job**: Execute the Hadoop job using the copied JAR file.
    ```sh
    docker exec namenode hadoop jar /hadoop-map-reduce-examples-1.0-SNAPSHOT-jar-with-dependencies.jar
    ```

5. **View the Output**: Check the output of the job.
    ```sh
    docker exec namenode hdfs dfs -text /user/hdfs/output/part-r-00000 | head -100
    ```
