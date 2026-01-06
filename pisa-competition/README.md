# PISA 2018 Data Analysis

Analysis of PISA (Programme for International Student Assessment) 2018 educational assessment data with focus on Greece's performance compared to international standards.

## Overview

This project explores PISA 2018 data to understand educational performance across countries, with particular emphasis on Greece. The analysis includes performance comparisons across subjects (Math, Reading, Science), gender analysis, and socioeconomic factors.

## Dataset

- **Source**: PISA 2018 Assessment
- **Format**: R data file (pisa2018.Rdata)
- **Size**: 11.3 MB
- **Subjects**: Mathematics, Reading, Science
- **Focus**: Greece and international comparisons

## Project Structure

```
pisa-competition/
├── code.ipynb              # Main analysis notebook
├── pisa2018.Rdata         # PISA 2018 dataset
├── plots/                 # Generated visualizations (12 plots)
│   ├── plot1.png
│   ├── plot2.png
│   └── ...
├── presentation.pdf       # Project presentation
└── presentation.tex       # LaTeX source for presentation
```

## Analysis Components

- Student performance across countries
- Greece-specific analysis
- Subject comparisons (Math, Reading, Science)
- Gender performance gaps
- Socioeconomic factors (parental education)
- Cross-country benchmarking

## Installation

### Prerequisites

- Python 3.8+
- Jupyter Notebook/Lab

### Setup

1. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn pyreadr
```

2. Launch Jupyter:
```bash
jupyter notebook code.ipynb
```

## Key Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- pyreadr (for reading R data files)

## Outputs

- **Visualizations**: 12 plots comparing educational metrics
- **Presentation**: Analysis findings and insights (PDF)

## Usage

1. Open `code.ipynb` in Jupyter Notebook
2. Run the setup cell to load the data
3. Execute cells sequentially to generate analysis and plots
4. Plots are automatically saved to the `plots/` directory

## Key Metrics

The analysis examines:
- Average scores by country
- Performance distribution across subjects
- Gender-based performance differences
- Impact of parental education on student outcomes
- Greece's ranking in international context

## Notes

- Data is loaded from R format using `pyreadr`
- All plots are saved as PNG files
- Analysis includes missing data handling
- Focus on Greece's comparative performance

## License

Academic project - AUEB Data Visualization Course
