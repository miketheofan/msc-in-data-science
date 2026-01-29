# Project 1: Word Network Analysis

## Overview

Network analysis of word co-occurrences from Charles Dickens' "David Copperfield".

## Technologies

Python, NetworkX, Gephi, Pandas, Matplotlib, Seaborn

## Project Structure

```
project1/
├── README.md                           # This file
├── project1.pdf                        # Assignment description
├── nodes.csv                           # Input: network nodes (words)
├── edges.csv                           # Input: network edges (adjacencies)
├── analysis.ipynb                      # Main Jupyter notebook with all analysis
├── requirements.txt                    # Python package dependencies
├── instructions/                       # Guides and instructions
├── david_copperfield_network.gexf      # Generated: Export for Gephi
├── david_copperfield_network.gephi     # Generated: Gephi project file
├── screenshots/                        # Generated: Network visualizations
├── network/                            # Generated: Sigma.js web export
└── report.pdf                          # Final project report
```

---

## Getting Started

### Step 1: Install Required Python Packages

```bash
pip install networkx pandas matplotlib seaborn python-louvain
```

Or if you're using conda:

```bash
conda install networkx pandas matplotlib seaborn
pip install python-louvain
```

### Step 2: Run the Analysis

1. Open [analysis.ipynb](analysis.ipynb) in Jupyter Lab/Notebook or VS Code
2. Run all cells in order (Cell → Run All)
3. **Important**: In Section 5 (Ego Network Analysis), choose your word:
   - Look at the suggested words printed
   - Pick one that interests you
   - Update the `selected_node` variable with the node ID
   - Re-run cells from that section onwards

### Step 3: Use Gephi

1. Install Gephi from: https://gephi.org/users/download/
2. Follow the instructions in the [instructions/](instructions/) folder
3. Import the generated GEXF file and create visualizations

---

## What the Notebook Does

### Analysis Pipeline:

1. **Load Data** (nodes.csv, edges.csv)
2. **Create Network** (NetworkX Graph)
3. **Calculate Metrics**:
   - Degree centrality
   - Network diameter
   - Betweenness centrality
   - PageRank
   - Community detection (Louvain algorithm)
4. **Ego Network Analysis**:
   - Select interesting word
   - Find neighbors at depth 1, 2, 3+
5. **Visualizations**:
   - Degree distribution
   - Community network
   - Ego network
6. **Export to GEXF** (for Gephi import)

---

## Project Deliverables

### 1. Report ([report.pdf](report.pdf))

Includes:

- **Network Statistics**:
  - Number of nodes and edges
  - Network diameter
  - Node with largest betweenness centrality
  - Number of communities

- **Community Analysis**:
  - Observations about detected communities
  - Examples of semantically different nouns in same community
  - Explanation of why they're grouped together

- **Selected Word for Ego Network**:
  - The word you chose
  - Its degree
  - Its PageRank value
  - Why you chose it

- **Visualization Choices**:
  - Which layout algorithm you used in Gephi
  - Why you chose those colors
  - How you sized the nodes

- **Screenshots** from Gephi showing the final network

### 2. Visualizations & Files

Delivered files:
- [david_copperfield_network.gephi](david_copperfield_network.gephi) - Gephi project file
- [network/](network/) - Sigma.js interactive web visualization
- [screenshots/](screenshots/) - Network visualization screenshots
- [david_copperfield_network.gexf](david_copperfield_network.gexf) - Network data in GEXF format

---

## Key Findings

The analysis reveals:

- **Network Structure**: Complete graph statistics including nodes, edges, and diameter
- **Central Nodes**: Most important words identified by degree, betweenness, and PageRank
- **Communities**: Distinct word clusters detected using the Louvain algorithm
- **Ego Network**: Multi-layer connectivity patterns around selected focal word

Detailed findings are documented in [report.pdf](report.pdf) and visualized in [screenshots/](screenshots/).

---

## Time Estimate

- Running notebook: **15-20 minutes**
- Choosing and analyzing word: **10 minutes**
- Gephi work: **30 minutes**
- Writing report: **1-2 hours**
- **Total: ~2.5-3 hours**

---

## Tips

### Choosing a Word for Ego Network:

**Good choices**:
- Moderate degree (not highest, not lowest)
- Interesting semantic meaning
- Representative of a theme in the novel

**Why moderate degree?**
- Too high: Ego network will include almost all nodes (boring)
- Too low: Ego network will be tiny (also boring)
- Moderate: Shows interesting connectivity patterns

### Understanding Communities:

Communities are formed by **co-occurrence patterns**, not semantic similarity!

- Words in the same community appear near each other frequently
- Example: "old" and "man" might be together because "old man" appears often
- Different semantic words can cluster if they're used in similar contexts

### Gephi Tips:

- **Don't rush the layout**: Let ForceAtlas2 run for at least 30 seconds
- **Prevent overlap is crucial**: Make sure nodes don't overlap
- **Color contrast matters**: Communities should be clearly distinguishable
- **Test the Sigma export**: Open index.html to make sure it works

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'community'"
```bash
pip install python-louvain
```

### "Kernel died while running cell"
- You might need more RAM
- Try closing other applications
- The network is small, so this shouldn't happen

### "Cannot find file nodes.csv"
- Make sure you're running the notebook from the `project1/` directory
- Or use absolute paths

### Gephi won't import GEXF
- Make sure you ran the notebook completely
- Check that `david_copperfield_network.gexf` exists
- Try File → Import instead of File → Open

---

## Resources

- **NetworkX Documentation**: https://networkx.org/documentation/stable/
- **Gephi Tutorial**: https://gephi.org/users/quick-start/
- **Louvain Algorithm**: https://en.wikipedia.org/wiki/Louvain_method
- **GEXF Format**: https://gexf.net/

---

## Project Status

- [x] Ran entire notebook successfully
- [x] Chose interesting word for ego network
- [x] Generated all visualizations
- [x] Created GEXF file
- [x] Completed Gephi analysis
- [x] Exported to Sigma.js
- [x] Saved Gephi project file
- [x] Wrote final report
- [x] Created all deliverables
- [x] Project completed

---

## Learning Objectives

By completing this project, you will:

1. Understand how to analyze networks using Python (NetworkX)
2. Calculate important network metrics (centrality, communities)
3. Visualize networks effectively
4. Use professional network visualization tools (Gephi)
5. Interpret network structure in context (word co-occurrence)
6. Communicate findings through visualizations and reports

---

## Files

- **[analysis.ipynb](analysis.ipynb)** - Complete network analysis notebook
- **[report.pdf](report.pdf)** - Final written report
- **[project1.pdf](project1.pdf)** - Original assignment description
- **[requirements.txt](requirements.txt)** - Python dependencies

---

**Project Completed**: December 2025
**Course**: INF322 - Social Network Analysis, AUEB
