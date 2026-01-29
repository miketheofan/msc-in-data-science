# Project 2: SNAP Network Analysis

**Course**: INF322 - Social Network Analysis
**Status**: ✅ Completed

---

## Overview

Two-part project using SNAP (Stanford Network Analysis Platform):
1. **Euler Paths/Circuits**: Detect Euler paths and circuits in graphs
2. **Community Detection**: Analyze centrality measures and community detection algorithms

---

## Files

- `project2.ipynb` - Main notebook with all analysis
- `project2-1.py` - Euler path/circuit functions
- `project2-2.py` - Community detection analysis
- `project2.pdf` - Final report
- `plot1_centrality.png` - Centrality comparison plot
- `plot2_hits.png` - PageRank vs HITS plot

---

## Setup

```bash
pip install snap-stanford pandas numpy matplotlib jupyter
```

**Note**: SNAP works best with Python 3.8 or 3.9

---

## Running

```bash
# Run full notebook
jupyter notebook project2.ipynb

# Or run standalone scripts
python project2-1.py  # Part 1
python project2-2.py  # Part 2
```

---

## Key Results

- Implemented Euler path/circuit detection (4 test cases)
- Analyzed Watts-Strogatz graphs (50, 500, 5000, 10000 nodes)
- Girvan-Newman times out at ~500 nodes (10+ minutes)
- Clauset-Newman-Moore scales much better
- Generated centrality comparison plots

---

## Requirements

After cloning from git, all code and data files are included. Just install dependencies and run.
