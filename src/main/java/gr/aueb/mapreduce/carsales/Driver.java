package gr.aueb.mapreduce.carsales;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Driver {
    public static  void main(String[] args) throws Exception {

        System.setProperty("hadoop.home.dir", "/");

        // instantiate a configuration
        Configuration configuration = new Configuration();

        // instantiate a job
        Job job = Job.getInstance(configuration, "Word Count");

        // set job parameters
        job.setJarByClass(WordCount.class);
        job.setMapperClass(WordCount.CountMapper.class);

        // Set the data types for the output key-value pairs
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        // Set the data types for the map output key-value pairs
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        /* We will not use a combiner in this implementation since:
            1. We need to calculate the average difference for all cars from a seller in a given month.
            2. If we used a combiner it would combine each result and get the average after every chunk.
            3. We need to do the reduce functionality only once and at the end of the execution.
         */
    //        job.setCombinerClass(WordCount.CountReducer.class);

        job.setReducerClass(WordCount.CountReducer.class);

        // set io paths
        FileOutputFormat.setOutputPath(job, new Path("/user/hdfs/output/"));
        FileInputFormat.addInputPath(job, new Path("/user/hdfs/input/car_prices.csv"));

        System.exit(job.waitForCompletion(true)? 0 : 1);
    }
}
