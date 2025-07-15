package gr.aueb.mapreduce.carsales;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class CarSales {
    public static class CountMapper extends Mapper<LongWritable, Text, Text, Text> {
        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String[] fields = value.toString().split(",");

            // Condition for header or row with missing data
            if (key.get() == 0 || fields.length != 16) {
                return;
            }

            // Get the seller from the String
            String seller = fields[12];

            // Parse the date string to get year and month
            String dateString = fields[15];
            String[] dateParts = dateString.split(" ");

            // If date is missing or wrong formatted skip row
            if(dateParts.length != 7) {
                return;
            }

            String year = dateParts[3];
            String month = CountMapper.getMonthFromString(dateParts[1]);
            String date = year + "-" + month;

            // Get prices
            double sellingPrice = Double.parseDouble(fields[13]);
            double mmr = Double.parseDouble(fields[14]);
            double diff = sellingPrice - mmr;

            // Extract car model (fields 2 and 3 combined)
            String carModel = fields[1] + " " + fields[2];

            Text outputKey = new Text(seller.toLowerCase() + ":" + date);
            Text outputValue = new Text(carModel + ":" + diff);

            context.write(outputKey, outputValue);
        }

        // Method that gets as input the code of a month and returns the number (in String)
        // needed for the outputKey format.
        public static String getMonthFromString(String month) {
            switch (month.toLowerCase()) {
                case ("jan"): return String.valueOf(1);
                case ("feb"): return String.valueOf(2);
                case ("mar"): return String.valueOf(3);
                case ("apr"): return String.valueOf(4);
                case ("may"): return String.valueOf(5);
                case ("jun"): return String.valueOf(6);
                case ("jul"): return String.valueOf(7);
                case ("aug"): return String.valueOf(8);
                case ("sep"): return String.valueOf(9);
                case ("oct"): return String.valueOf(10);
                case ("nov"): return String.valueOf(11);
                case ("dec"): return String.valueOf(12);
                default: return String.valueOf(0);
            }
        }
    }

    public static class CountReducer extends Reducer<Text, Text, Text, Text> {
        @Override
        public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            double maxDiff = Double.NEGATIVE_INFINITY;
            String maxDiffCar = "";
            double sumDiff = 0.0;
            int count = 0;

            // First pass: calculate all statistics
            for (Text value: values) {
                String[] parts = value.toString().split(":");
                String carModel = parts[0];
                double diff = Double.parseDouble(parts[1]);

                // Update max difference values if applicable
                if (diff > maxDiff) {
                    maxDiff = diff;
                    maxDiffCar = carModel;
                }

                // Update variables needed for average
                sumDiff += diff;
                count++;
            }

            // Calculate the average outside the loop
            double avgDiff = count != 0 ? sumDiff / count : 0;

            // Format output: "CarModel: difference, avg: average_difference"
            String output = String.format("%s: %.2f, avg: %.2f", maxDiffCar, maxDiff, avgDiff);

            // Write output only once per key
            context.write(key, new Text(output));
        }
    }
}
