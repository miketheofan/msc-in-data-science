import java.io.*;
import java.util.*;

public class StandaloneLabelPropagation {

    static class Graph {
        Map<Long, Set<Long>> adjacencyList = new HashMap<>();
        Map<Long, Long> labels = new HashMap<>();

        void addVertex(long vertex) {
            adjacencyList.putIfAbsent(vertex, new HashSet<>());
            labels.put(vertex, vertex); // Initialize with own ID
        }

        void addEdge(long from, long to) {
            adjacencyList.get(from).add(to);
        }

        void labelPropagation(int maxIterations) {
            for (int iter = 0; iter < maxIterations; iter++) {
                boolean changed = false;
                Map<Long, Long> newLabels = new HashMap<>(labels);

                for (long vertex : adjacencyList.keySet()) {
                    Set<Long> neighbors = adjacencyList.get(vertex);
                    if (neighbors.isEmpty()) continue;

                    // Count label frequencies from neighbors
                    Map<Long, Integer> labelCount = new HashMap<>();
                    for (long neighbor : neighbors) {
                        long label = labels.get(neighbor);
                        labelCount.put(label, labelCount.getOrDefault(label, 0) + 1);
                    }

                    // Find most frequent label (ties broken by smallest value)
                    long maxLabel = labels.get(vertex);
                    int maxCount = 0;

                    for (Map.Entry<Long, Integer> entry : labelCount.entrySet()) {
                        long label = entry.getKey();
                        int count = entry.getValue();

                        if (count > maxCount || (count == maxCount && label < maxLabel)) {
                            maxLabel = label;
                            maxCount = count;
                        }
                    }

                    // Special case: if only one neighbor, adopt if smaller
                    if (labelCount.size() == 1) {
                        long neighborLabel = labelCount.keySet().iterator().next();
                        if (neighborLabel < labels.get(vertex)) {
                            maxLabel = neighborLabel;
                        } else {
                            maxLabel = labels.get(vertex);
                        }
                    }

                    if (maxLabel != labels.get(vertex)) {
                        newLabels.put(vertex, maxLabel);
                        changed = true;
                    }
                }

                labels = newLabels;
                System.out.println("Iteration " + (iter + 1) + " completed");

                if (!changed) {
                    System.out.println("Converged at iteration " + (iter + 1));
                    break;
                }
            }
        }

        void printResults() {
            List<Long> vertices = new ArrayList<>(labels.keySet());
            Collections.sort(vertices);
            for (long vertex : vertices) {
                System.out.println(vertex + "\t" + labels.get(vertex));
            }
        }

        void saveResults(String filename) throws IOException {
            PrintWriter writer = new PrintWriter(new FileWriter(filename));
            List<Long> vertices = new ArrayList<>(labels.keySet());
            Collections.sort(vertices);
            for (long vertex : vertices) {
                writer.println(vertex + "\t" + labels.get(vertex));
            }
            writer.close();
            System.out.println("Results saved to " + filename);
        }
    }

    public static void main(String[] args) throws IOException {
        String inputFile = "input_graph.txt";
        String outputFile = "output_label_propagation.txt";
        int maxIterations = 50;

        if (args.length > 0) inputFile = args[0];
        if (args.length > 1) outputFile = args[1];
        if (args.length > 2) maxIterations = Integer.parseInt(args[2]);

        System.out.println("Loading graph from " + inputFile);
        Graph graph = new Graph();

        BufferedReader reader = new BufferedReader(new FileReader(inputFile));
        String line;
        while ((line = reader.readLine()) != null) {
            String[] parts = line.trim().split("\\s+");
            if (parts.length == 0) continue;

            long vertex = Long.parseLong(parts[0]);
            graph.addVertex(vertex);

            for (int i = 1; i < parts.length; i++) {
                long neighbor = Long.parseLong(parts[i]);
                graph.addVertex(neighbor);
                graph.addEdge(vertex, neighbor);
            }
        }
        reader.close();

        System.out.println("Graph loaded with " + graph.adjacencyList.size() + " vertices");
        System.out.println("Running Label Propagation (max " + maxIterations + " iterations)...");

        graph.labelPropagation(maxIterations);

        System.out.println("\nFinal community assignments:");
        graph.printResults();

        graph.saveResults(outputFile);

        // Print _SUCCESS file
        PrintWriter success = new PrintWriter(new FileWriter("_SUCCESS"));
        success.close();
        System.out.println("_SUCCESS file created");
    }
}
