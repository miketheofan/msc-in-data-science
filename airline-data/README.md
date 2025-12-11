# Team E: MCO vs MIA Airport Analysis (2004-2008)

**Simple, clean analysis comparing Orlando (MCO) and Miami (MIA) airports.**

## Project Structure

```
airline-data/
├── code/
│   ├── 01_data_loading.ipynb    # Download & filter data from web
│   └── 02_data_cleaning.ipynb   # Clean data & create derived columns
├── data/processed/              # Filtered data saved here
├── visualizations/              # PNG outputs
├── tableau/                     # Power BI/Tableau files
├── report/                      # Report & presentation
└── requirements.txt
```

## Quick Start

### 1. Install

```bash
pip install -r requirements.txt
```

### 2. Configure Dropbox Links

Your .bz2 files are in: https://www.dropbox.com/home/airline-data-2004-2008

For each file, get the direct download link:
1. Click Share → Create link
2. Replace `www.dropbox.com` with `dl.dropboxusercontent.com`
3. Paste into notebook 01 DROPBOX_URLS section

### 3. Run Notebooks

```bash
cd code
jupyter notebook
```

**Notebook 01:** Reads .bz2 files from Dropbox & filters for MCO/MIA
- Reads compressed files directly (no extraction needed)
- Chunk processing - never loads full dataset into memory
- Saves only filtered data (~50MB/year)

**Notebook 02:** Cleans data & creates derived columns
- On-time performance, delay categories, etc.
- Saves to `mco_mia_clean.csv`

### 4. Next Steps

- Create visualizations (12+ plots needed)
- Build Power BI/Tableau dashboards
- Write report & presentation

## Key Features

✅ Reads .bz2 files directly from Dropbox
✅ Automatic decompression (pandas handles .bz2)
✅ Chunk processing (never loads full dataset)
✅ Filtered data only (~250MB total vs ~35GB raw)
✅ Clean, professional code

## Project Requirements

- Minimum 12 visualizations
- At least 1 map
- At least 1 interactive visualization
- Use Python + Power BI/Tableau
- Compare MCO (Orlando) vs MIA (Miami)
- Years: 2004-2008

## Team Members

- [Name] - [Role]
- [Name] - [Role]
- [Name] - [Role]
- [Name] - [Role]
