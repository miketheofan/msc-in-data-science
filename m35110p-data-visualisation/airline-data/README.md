# Airline Data Analysis: MCO vs MIA

Flight data analysis project comparing Orlando International Airport (MCO) and Miami International Airport (MIA) from 1998-2008.

## Overview

This project analyzes over 3.4 million flight records to understand delay patterns, on-time performance, and operational differences between MCO and MIA airports. The analysis includes exploratory data analysis, delay pattern investigation, and correlations with external factors.

## Dataset

- **Source**: US Department of Transportation flight data
- **Period**: 1998-2008 (primary focus on 2004-2008)
- **Airports**: MCO (Orlando), MIA (Miami)
- **Records**: ~3.4 million flights (1998-2008), ~1.6 million flights (2004-2008)
- **Size**: 69.1 MB compressed (1998-2008)

## Project Structure

```
airline-data/
├── code/
│   ├── 01_data_loading.ipynb           # Data extraction and filtering
│   ├── 02_data_cleaning.ipynb          # Data cleaning and feature engineering
│   ├── 03_EDA.ipynb                    # Exploratory data analysis
│   ├── 04_Delay_Deep_Dive.ipynb        # Flight delay analysis
│   ├── 05_external_data_correlation.ipynb  # External data correlations
│   ├── COLUMN_REFERENCE.md             # Data dictionary
│   └── requirements.txt                # Python dependencies
├── data/
│   └── processed/                      # Cleaned and processed datasets
├── visualizations/                     # Generated plots and charts
├── presentation.pdf                    # Project presentation
└── report.pdf                          # Detailed analysis report
```

## Analysis Workflow

1. **Data Loading** - Extract and filter flight data for MCO/MIA airports
2. **Data Cleaning** - Handle missing values and create derived features
3. **Exploratory Data Analysis** - Investigate patterns and trends
4. **Delay Deep Dive** - Analyze delay causes and patterns
5. **External Correlations** - Correlate with external factors

## Key Features

- On-time performance analysis
- Delay pattern identification by time, season, and carrier
- Airport comparison (MCO vs MIA)
- Interactive visualizations with Plotly and Folium
- Statistical analysis of delay causes

## Installation

### Prerequisites

- Python 3.8+
- Jupyter Notebook/Lab

### Setup

1. Install dependencies:
```bash
pip install -r code/requirements.txt
```

2. Launch Jupyter:
```bash
jupyter notebook
```

3. Run notebooks in order (01 → 02 → 03 → 04 → 05)

## Dependencies

- pandas 2.1.4
- numpy 1.26.2
- matplotlib 3.8.2
- seaborn 0.13.0
- plotly 5.18.0
- folium 0.15.1
- openpyxl 3.1.2

## Key Findings

- **Overall On-Time Performance**: 78.25%
- **MCO Departures**: 78.88% on-time
- **MIA Departures**: 74.03% on-time
- **Cancellation Rate**: 1.22%
- **Average Delay**: 8.3 minutes

## Data Dictionary

See [COLUMN_REFERENCE.md](code/COLUMN_REFERENCE.md) for complete data dictionary including all original and derived columns.

## Outputs

- **Processed Data**: Cleaned datasets in `data/processed/`
- **Visualizations**: Charts and plots in `visualizations/`
- **Reports**: Final presentation and analysis report (PDF)

## Notes

- 2008 data is partial (January-April only)
- Flight times are in HHMM format (e.g., 1625 = 4:25 PM)
- Delay times are in minutes (negative values indicate early arrival)
- Raw data URLs are stored in `secrets.txt` (not included in repository)

## License

Academic project - AUEB Data Visualization Course
