# Team Setup Guide: MCO vs MIA Analysis

**Project:** Compare Orlando (MCO) vs Miami (MIA) airports using 2004-2008 flight data
**Team:** Team E
**Due Date:** January 5, 2025

---

## For New Team Members: Getting Started

### Step 1: Clone/Download the Project

If you received this via Google Drive or Dropbox:
1. Download the entire `airline-data/` folder
2. Extract to your working directory

If using Git:
```bash
git clone [repository-url]
cd airline-data
```

---

### Step 2: Install Dependencies

**Option A - Local Machine:**
```bash
pip install -r requirements.txt
```

**Option B - Google Colab:**
1. Upload the notebooks to Google Drive
2. Open in Google Colab
3. Run this cell first:
```python
!pip install pandas numpy matplotlib seaborn plotly folium openpyxl
```

---

### Step 3: Get the Cleaned Data

**You do NOT need to run notebook 01 (data loading)**

The clean data file has already been prepared and should be available from your team lead:
- **File:** `mco_mia_clean.csv.gz`
- **Size:** ~25MB (compressed)
- **Location:** Download from shared drive and place in `data/processed/`

**Download from team shared folder → Place in `data/processed/mco_mia_clean.csv.gz`**

---

### Step 4: Understand the Data

Read [COLUMN_REFERENCE.md](COLUMN_REFERENCE.md) to see:
- What columns are available
- What each column means
- Derived features (OnTime, DelayCategory, TimeOfDay, etc.)
- Key statistics

---

### Step 5: Start Your Visualizations

**Load the data:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('../data/processed/mco_mia_clean.csv.gz')

# Quick check
print(f"Loaded {len(df):,} flights")
print(f"Columns: {df.columns.tolist()}")
```

**See existing examples:**
- Open `code/02_data_cleaning.ipynb` to see 3 example visualizations
- Use the same styling for consistency

---

## Your Visualization Assignment

**Team needs:** Minimum 12 visualizations total
- At least 1 map (use folium or plotly)
- At least 1 interactive visualization (use plotly)

**Your assignment:** [To be assigned by team lead]

### Suggested Topics:

**Time Analysis:**
- Delays by hour of day
- Delays by day of week
- Delays by season
- Trend over years

**Airport Comparison:**
- MCO vs MIA on-time performance
- Departure vs arrival delays
- Cancellation rates
- Top routes for each airport

**Route Analysis:**
- Most popular routes
- Delays by distance
- Geographic map of routes

**Carrier Analysis:**
- Best/worst airlines
- Carrier market share
- Delays by carrier

---

## File Organization

**Save your work:**
```
visualizations/
├── [your-name]_plot1_delays_by_hour.png
├── [your-name]_plot2_mco_vs_mia.png
└── [your-name]_plot3_route_map.html
```

**Use descriptive names!**

---

## Styling Guidelines

Keep visualizations consistent with the existing style:

```python
# Apply this styling
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = '#f8f9fa'

# Use these sizes
fig, ax = plt.subplots(figsize=(12, 6))

# Add thousands separators
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

# Clean titles
ax.set_title('Your Title Here', fontsize=16, fontweight='bold', pad=20)
```

---

## Important Notes

- **2008 data is partial** - Only Jan-Apr (4 months)
- All times in 24-hour format
- Delays in minutes (negative = early)
- Check for missing values before plotting

---
