# European Cities Airbnb Analysis

An analysis of Airbnb data across 13 major European cities using Python and Jupyter notebooks.

## Overview

This project analyzes Airbnb listing data from:

- Amsterdam
- Athens
- Barcelona
- Berlin
- Copenhagen
- Dublin
- Lisbon
- London
- Madrid
- Paris
- Rome
- Venice
- Vienna

## Data Structure

The data is organized by city with each city folder containing:

- `listings.csv` - Detailed information about each Airbnb listing
- `calendar.csv.gz` - Availability and pricing data
- `neighbourhoods.csv` - Geographic neighborhood data
- `reviews.csv` - User reviews

## Analysis

The main analysis is in `airbnb.ipynb` which includes:

- Data cleaning and preprocessing
- Exploratory data analysis
- Occupancy rate analysis
- Price analysis
- Booking patterns
- Room type distribution
- Geographic analysis by neighborhood
- Interactive visualizations

## Key Features

- Full data processing pipeline
- Comprehensive data cleaning
- Advanced visualizations using matplotlib and seaborn
- Interactive city selection using ipywidgets
- Statistical analysis of Airbnb patterns

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- ipywidgets

Install requirements:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository
2. Install requirements
3. Open `airbnb.ipynb` in Jupyter
4. Run all cells to generate analysis

## Data Sources

Data sourced from InsideAirbnb.com for the latest 12 month period available for each city.
