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
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.log4j.Logger;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

/**
 * Label propagation for community detection
 */
@Algorithm(name = "Label propagation", description = "Community detection using label propagation")
public class SimpleLabelPropagationComputation
        extends
        BasicComputation<LongWritable, LongWritable, NullWritable, LongWritable> {

    private static final Logger LOG = Logger
            .getLogger(SimpleLabelPropagationComputation.class);

    private static final int MAX_ITERATIONS = 50;

    @Override
    public void compute(
            Vertex<LongWritable, LongWritable, NullWritable> vertex,
            Iterable<LongWritable> messages) throws IOException {

        LOG.info(vertex.getId() + ": " + getSuperstep());

        // First iteration: initialize with own id
        if (getSuperstep() == 0) {
            vertex.setValue(vertex.getId());
            sendMessageToAllEdges(vertex, vertex.getValue());
            return;
        }

        // Stop after max iterations
        if (getSuperstep() >= MAX_ITERATIONS) {
            vertex.voteToHalt();
            return;
        }

        // Count how many times each label appears
        Map<Long, Integer> counts = new HashMap<Long, Integer>();
        for (LongWritable msg : messages) {
            long label = msg.get();
            if (counts.containsKey(label)) {
                counts.put(label, counts.get(label) + 1);
            } else {
                counts.put(label, 1);
            }
        }

        // Find most common label, break ties with smallest value
        long bestLabel = vertex.getValue().get();
        int bestCount = 0;

        for (Map.Entry<Long, Integer> entry : counts.entrySet()) {
            long label = entry.getKey();
            int count = entry.getValue();

            if (count > bestCount || (count == bestCount && label < bestLabel)) {
                bestLabel = label;
                bestCount = count;
            }
        }

        // Special case: single neighbor
        if (counts.size() == 1) {
            long neighborLabel = counts.keySet().iterator().next();
            if (neighborLabel < vertex.getValue().get()) {
                bestLabel = neighborLabel;
            } else {
                bestLabel = vertex.getValue().get();
            }
        }

        // Update if changed
        if (bestLabel != vertex.getValue().get()) {
            vertex.setValue(new LongWritable(bestLabel));
            sendMessageToAllEdges(vertex, vertex.getValue());
        } else {
            vertex.voteToHalt();
        }
    }

}
