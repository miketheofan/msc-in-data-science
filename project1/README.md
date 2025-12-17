# Project 1: David Copperfield Word Network Analysis

**Course**: INF322 - Social Network Analysis
**Due**: December 21, 2025
**Instructor**: Katia Papakonstantinopoulou

---

## 📁 Project Structure

```
project1/
├── README.md                           # This file
├── project1.pdf                        # Assignment description
├── nodes.csv                           # Input: network nodes (words)
├── edges.csv                           # Input: network edges (adjacencies)
├── analysis.ipynb                      # Main Jupyter notebook (YOUR WORK HERE)
├── gephi_instructions.md               # Step-by-step Gephi guide
├── david_copperfield_network.gexf      # Generated: Export for Gephi
├── degree_distribution.png             # Generated: Visualization
├── network_communities.png             # Generated: Visualization
├── ego_network.png                     # Generated: Visualization
├── david_copperfield.gephi             # Generated: Gephi project file
└── sigma_export/                       # Generated: Web visualization
```

---

## 🚀 Getting Started

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

1. Open `analysis.ipynb` in Jupyter Lab/Notebook or VS Code
2. Run all cells in order (Cell → Run All)
3. **Important**: In Section 5 (Ego Network Analysis), choose your word:
   - Look at the suggested words printed
   - Pick one that interests you
   - Update the `selected_node` variable with the node ID
   - Re-run cells from that section onwards

### Step 3: Use Gephi

1. Install Gephi from: https://gephi.org/users/download/
2. Follow **ALL** steps in `gephi_instructions.md`
3. This will take about 30 minutes

---

## 📊 What the Notebook Does

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

## 📝 What You Need to Submit

### 1. Report (proj1.pdf)

Should include:

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

### 2. Compressed Folder

Should contain:
- `david_copperfield.gephi` (Gephi project file)
- `sigma_export/` folder (interactive web visualization)

---

## 🔍 Key Findings (Will be in Your Notebook Output)

After running the notebook, you'll see:

- **Basic Stats**: Number of nodes, edges, diameter
- **Top Nodes**: By degree, betweenness, PageRank
- **Communities**: How many, what words are in each
- **Ego Network**: Layers of connectivity around your chosen word

All of this goes into your report!

---

## ⏱️ Time Estimate

- Running notebook: **15-20 minutes**
- Choosing and analyzing word: **10 minutes**
- Gephi work: **30 minutes**
- Writing report: **1-2 hours**
- **Total: ~2.5-3 hours**

---

## 💡 Tips

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

## 🐛 Troubleshooting

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

## 📚 Resources

- **NetworkX Documentation**: https://networkx.org/documentation/stable/
- **Gephi Tutorial**: https://gephi.org/users/quick-start/
- **Louvain Algorithm**: https://en.wikipedia.org/wiki/Louvain_method
- **GEXF Format**: https://gexf.net/

---

## ✅ Checklist Before Submission

- [ ] Ran entire notebook successfully
- [ ] Chose interesting word for ego network
- [ ] Generated all visualizations (3 PNG files)
- [ ] Created GEXF file
- [ ] Installed Gephi
- [ ] Followed all Gephi instructions
- [ ] Exported to Sigma.js
- [ ] Tested Sigma export (opened in browser)
- [ ] Saved Gephi project file
- [ ] Wrote report (proj1.pdf)
- [ ] Compressed folder with .gephi file and sigma_export/
- [ ] Uploaded to eclass.aueb.gr

---

## 🎯 Learning Objectives

By completing this project, you will:

1. Understand how to analyze networks using Python (NetworkX)
2. Calculate important network metrics (centrality, communities)
3. Visualize networks effectively
4. Use professional network visualization tools (Gephi)
5. Interpret network structure in context (word co-occurrence)
6. Communicate findings through visualizations and reports

---

Good luck! 🚀

If you have questions, contact the instructor via eclass.aueb.gr
