# Social Network Analysis - Course Projects

**Course**: INF322 - Social Network Analysis
**Institution**: Athens University of Economics and Business (AUEB)
**Semester**: Trimester 4 (Fall 2025)
**Instructor**: Katia Papakonstantinopoulou

---

## Repository Overview

This repository contains all projects and assignments for the Social Network Analysis course. The course explores graph theory, network metrics, community detection, and visualization techniques applied to real-world networks.

---

## Projects

### Project 1: David Copperfield Word Network Analysis

**Status**: Completed
**Due Date**: December 21, 2025

**Description**: Analysis of word co-occurrence networks from Charles Dickens' "David Copperfield". This project involves:
- Network construction from word adjacency data
- Centrality metrics calculation (degree, betweenness, PageRank)
- Community detection using the Louvain algorithm
- Ego network analysis
- Interactive visualization using Gephi and Sigma.js

**Key Technologies**: Python, NetworkX, Gephi, Pandas, Matplotlib

**Deliverables**:
- Network analysis notebook ([analysis.ipynb](project1/analysis.ipynb))
- Written report ([report.pdf](project1/report.pdf))
- Gephi project file and web visualization
- Network visualizations and screenshots

[View Project 1 Details](project1/README.md)

---

### Project 2: SNAP Community Detection & Centrality

**Status**: Completed
**Due Date**: December 28, 2025

**Description**: Analysis of community detection algorithms and centrality measures using SNAP:
- Euler path/circuit detection
- Watts-Strogatz graph generation
- Community detection (Girvan-Newman, CNM)
- Centrality analysis (PageRank, Betweenness, HITS)
- Scalability comparison

**Key Technologies**: Python, SNAP, Pandas, Matplotlib

**Deliverables**:
- Analysis notebook ([project2.ipynb](project2/project2.ipynb))
- Standalone scripts ([project2-1.py](project2/project2-1.py), [project2-2.py](project2/project2-2.py))
- Final report ([project2.pdf](project2/project2.pdf))
- Visualization plots

[View Project 2 Details](project2/README.md)

---

### Project 3: Giraph Label Propagation

**Status**: Completed

**Description**: Distributed graph processing using Apache Giraph:
- Label propagation algorithm implementation
- Community detection on large graphs
- Docker deployment

**Key Technologies**: Java, Apache Giraph, Hadoop

[View Project 3 Details](project3/README.md)

---

## Technologies & Tools

- **Python**: NetworkX, SNAP, Pandas, Matplotlib, Seaborn
- **Java**: Apache Giraph, Hadoop
- **Visualization**: Gephi, Sigma.js
- **Analysis**: Jupyter Notebooks
- **Version Control**: Git

---

## Learning Outcomes

Through these projects, the following concepts are explored:

1. **Network Construction**: Building graphs from real-world data
2. **Network Metrics**: Degree centrality, betweenness centrality, PageRank
3. **Community Detection**: Louvain method, modularity optimization
4. **Ego Networks**: Analyzing local network structure
5. **Network Visualization**: Layout algorithms, color coding, interactive displays
6. **Domain Applications**: Text analysis, social networks, information networks

---

## Course Topics

- Graph theory fundamentals
- Network properties and metrics
- Centrality measures
- Community detection algorithms
- Network models (random, small-world, scale-free)
- Information diffusion
- Link prediction
- Network visualization

---

## Getting Started

### Prerequisites

```bash
# Install required Python packages
pip install networkx pandas matplotlib seaborn python-louvain jupyter

# Or using conda
conda install networkx pandas matplotlib seaborn jupyter
pip install python-louvain
```

### Running Projects

Each project folder contains its own README with specific instructions:

```bash
# Navigate to project directory
cd project1/

# Launch Jupyter
jupyter notebook analysis.ipynb
```

---

## Academic Integrity

These projects are completed as part of coursework at AUEB. All work is original and follows academic integrity guidelines.

---

## Contact

For questions about these projects, contact via eclass.aueb.gr

---

## Timeline

- **Project 1**: Completed December 21, 2025
- **Project 2**: Completed December 28, 2025
- **Project 3**: Completed

---

## Timeline

- **Project 1**: Completed December 21, 2025
- **Project 2**: Completed December 28, 2025
- **Project 3**: Completed

---

**Last Updated**: December 2025
