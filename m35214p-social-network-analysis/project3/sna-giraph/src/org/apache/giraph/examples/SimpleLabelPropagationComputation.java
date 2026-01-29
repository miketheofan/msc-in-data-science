/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
package org.apache.giraph.examples;

import org.apache.giraph.graph.BasicComputation;
import org.apache.giraph.graph.Vertex;
import org.apache.giraph.edge.Edge;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.log4j.Logger;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
 
/**
 * Demonstrates a basic Pregel label propagation implementation.
 */
@Algorithm(name = "Label propagation", description = "Sets the value of each vertex to the a label signifying its assigned community")
public class SimpleLabelPropagationComputation
        extends
        BasicComputation<LongWritable, LongWritable, NullWritable, LongWritable> {
 
    /** Class logger */
    private static final Logger LOG = Logger
            .getLogger(SimpleLabelPropagationComputation.class);

    /** Maximum number of iterations */
    private static final int MAX_SUPERSTEPS = 50;

    @Override
    public void compute(
            Vertex<LongWritable, LongWritable, NullWritable> vertex,
            Iterable<LongWritable> messages) throws IOException {

        LOG.info(vertex.getId() + ": " + getSuperstep());

        // Superstep 0: Initialize with own ID and send to neighbors
        if (getSuperstep() == 0) {
            vertex.setValue(vertex.getId());
            sendMessageToAllEdges(vertex, vertex.getValue());
            return;
        }

        // Check if max iterations reached
        if (getSuperstep() >= MAX_SUPERSTEPS) {
            vertex.voteToHalt();
            return;
        }

        // Count label frequencies from received messages
        Map<Long, Integer> labelCount = new HashMap<Long, Integer>();
        for (LongWritable message : messages) {
            long label = message.get();
            if (labelCount.containsKey(label)) {
                labelCount.put(label, labelCount.get(label) + 1);
            } else {
                labelCount.put(label, 1);
            }
        }

        // Find the most frequent label (ties broken by smallest value)
        long maxLabel = vertex.getValue().get();
        int maxCount = 0;

        for (Map.Entry<Long, Integer> entry : labelCount.entrySet()) {
            long label = entry.getKey();
            int count = entry.getValue();

            // Update if: higher count, OR same count but smaller label value
            if (count > maxCount || (count == maxCount && label < maxLabel)) {
                maxLabel = label;
                maxCount = count;
            }
        }

        // Special case: if only one neighbor, adopt if smaller
        if (labelCount.size() == 1) {
            long neighborLabel = labelCount.keySet().iterator().next();
            if (neighborLabel < vertex.getValue().get()) {
                maxLabel = neighborLabel;
            } else {
                maxLabel = vertex.getValue().get();
            }
        }

        // If label changed, update and propagate to neighbors
        if (maxLabel != vertex.getValue().get()) {
            vertex.setValue(new LongWritable(maxLabel));
            sendMessageToAllEdges(vertex, vertex.getValue());
        } else {
            // No change, vote to halt
            vertex.voteToHalt();
        }
    }

}
