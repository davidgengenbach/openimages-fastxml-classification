package de.david.hadoop.test2;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.mapreduce.Reducer.Context;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;

public class LabelCount {

    public static class Map extends Mapper<Object, Text, Text, Text> {

        private final static Text LABEL = new Text();
        private final static Text ID = new Text();

        @Override
        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] line = value.toString().split(",");
            if(line[0].equals("ImageID")) {
                return;
            }
            
            ID.set(line[2]);
            LABEL.set(line[0]);
            context.write(ID, LABEL);
            context.write(LABEL, ID);
        }
    }

    public static class Reduce extends Reducer<Text, Text, Text, Text> {

        private MultipleOutputs mos;

        @Override
        public void setup(Context context) {
            System.out.println("Reducer.setup");
            mos = new MultipleOutputs(context);
        }

        @Override
        protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            StringBuilder sum = new StringBuilder();
            for (Text val : values) {
                if (val.toString().equals("")) {
                    continue;
                }
                if (val.find("|") != 0) {
                    sum.append("|");
                }

                sum.append(val.toString());
            }

            boolean isImage = key.toString().length() == 16;
            mos.write(isImage ? "image" : "label", key, new Text(sum.toString()));
        }
        
        

        @Override
        protected void cleanup(Context context) throws IOException, InterruptedException {
            mos.close();
            super.cleanup(context); //To change body of generated methods, choose Tools | Templates.
        }
    }
    
    public static class Map2 extends Mapper<Text, Text, Text, Text> {
        private final static Text OUT = new Text();

        @Override
        public void map(Text key, Text value, Context context) throws IOException, InterruptedException {
            boolean isImage = key.toString().length() == 16;
            OUT.set(key.toString() + "," + Integer.toString(value.toString().split("|").length));
            context.write(new Text(isImage ? "image" : "label"), OUT);
        }
    }

    public static class Reduce2 extends Reducer<Text, Text, IntWritable, IntWritable> {
        private static MultipleOutputs mos;

        @Override
        protected void setup(Context context) throws IOException, InterruptedException {
            System.out.println("Reducer2.setup");
            mos = new MultipleOutputs(context);
        }
        
        @Override
        public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            int count = 0;
            for(Text val : values) {
                //count += val.get();
            }
            
            mos.write(key.toString() + "2", key, new IntWritable(count));
        }
        
        @Override
        protected void cleanup(Context context) throws IOException, InterruptedException {
            mos.close();
            super.cleanup(context);
        }
    }
    

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();

        //conf.set("mapreduce.output.textoutputformat.separator", ",");
        
        FileSystem fs = FileSystem.get(conf);

        Path inputPath = new Path(args[0]);
        Path outputPath = new Path(args[1]);
        Path outputPath2 = new Path(args[2]);

        if (fs.exists(outputPath)) {
            fs.delete(outputPath, true);
        }

        if (fs.exists(outputPath2)) {
            fs.delete(outputPath2, true);
        }

        Job job = new Job(conf, "LabelCount");
        job.setJarByClass(LabelCount.class);

        job.setMapperClass(Map.class);
        job.setCombinerClass(Reduce.class);
        job.setReducerClass(Reduce.class);
        
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        MultipleOutputs.addNamedOutput(job, "label", TextOutputFormat.class, Text.class, Text.class);
        MultipleOutputs.addNamedOutput(job, "image", TextOutputFormat.class, Text.class, Text.class);

        TextInputFormat.addInputPath(job, inputPath);
        TextOutputFormat.setOutputPath(job, outputPath);

        job.waitForCompletion(false);

        Job job2 = new Job(new Configuration(), "LabelCount2");
        
        inputPath = new Path(args[1]);
        outputPath = new Path(args[2]);
        
        job2.setJarByClass(LabelCount.class);
        job2.setMapperClass(Map2.class);
        job2.setReducerClass(Reduce2.class);
        
        job2.setMapOutputKeyClass(Text.class);
        job2.setMapOutputValueClass(IntWritable.class);
        
        MultipleOutputs.addNamedOutput(job2, "label2", TextOutputFormat.class, IntWritable.class, IntWritable.class);
        MultipleOutputs.addNamedOutput(job2, "image2", TextOutputFormat.class, IntWritable.class, IntWritable.class);
        TextOutputFormat.setOutputPath(job2, outputPath);

        
        job2.setInputFormatClass(KeyValueTextInputFormat.class);
        KeyValueTextInputFormat.addInputPath(job2, inputPath);

        job2.waitForCompletion(false);
    }
}
