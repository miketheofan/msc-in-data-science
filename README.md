# Social Media Sanctions Analysis

This repository contains analysis code examining political differences in misinformation sharing on social media, based on the research by Mohsen Mosleh et al. published in Nature.

## Overview

The analysis investigates whether social media sanctions show political bias or if differences in sanction rates reflect actual differences in misinformation sharing behaviors between users of different political beliefs. The research suggests that users with conservative political beliefs are more likely to share questionable or misinformation material.

## Contents

- `differences_misinformation.ipynb` - Jupyter notebook containing the full analysis
- `mosleh_et_al_data.csv` - Dataset from the original research

## Key Analyses

The notebook includes:

- Analysis of low-quality news sharing patterns across political groups
- Statistical testing using t-tests and effect size calculations
- PCA analysis of political orientation variables
- Visualization of sharing behavior distributions
- Log transformations of engagement metrics

## Dependencies

The analysis requires the following Python libraries:

- pandas
- numpy
- seaborn
- statsmodels
- scipy
- scikit-learn
- matplotlib

## Usage

Open and run the Jupyter notebook to replicate the analysis. The notebook contains detailed documentation of the methodology and findings.
