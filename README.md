docker exec namenode hdfs dfs -rm -r /user/hdfs/output/
docker cp target/hadoop-map-reduce-examples-1.0-SNAPSHOT-jar-with-dependencies.jar namenode:/
docker exec namenode hadoop jar /hadoop-map-reduce-examples-1.0-SNAPSHOT-jar-with-dependencies.jar

docker exec namenode hdfs dfs -text /user/hdfs/output/part-r-00000 | head -100
