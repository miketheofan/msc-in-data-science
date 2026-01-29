# Project 3: Giraph Label Propagation

**Course**: INF322 - Social Network Analysis
**Status**: Completed

---

## Overview

Implementation of Label Propagation algorithm using Apache Giraph for distributed graph processing.

---

## Structure

```
project3/
├── sna-giraph/              # Apache Giraph project
│   ├── src/                 # Java source code
│   ├── lib/                 # JAR dependencies (~150 MB)
│   ├── bin/                 # Compiled classes
│   ├── Dockerfile           # Docker setup
│   ├── input_graph.txt      # Test input data
│   └── output_label_propagation.txt  # Results
└── project3.pdf             # Assignment specification
```

---

## Requirements

- Java JDK 8 or higher
- Apache Hadoop
- Apache Giraph libraries (included in `lib/`)
- Maven (optional, for rebuilding)

---

## Running

### Option 1: Using Docker
```bash
cd sna-giraph
docker build -t giraph-label-prop .
docker run giraph-label-prop
```

### Option 2: Direct Execution
```bash
cd sna-giraph
javac -cp "lib/*" -d bin src/*.java
java -cp "bin:lib/*" GiraphAppRunner
```

---

## Implementation

**Files:**
- `GiraphAppRunner.java` - Main application
- `SimpleLabelPropagationComputation.java` - Label propagation algorithm
- `LabelPropagationInputFormat.java` - Input format handler

**Algorithm**: Iterative label propagation for community detection in large graphs.

---

## Notes

All dependencies (JAR files) are included in git. After clone, compile and run.
