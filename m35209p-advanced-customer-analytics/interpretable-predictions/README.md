# Interpretable Predictions

This project focuses on building interpretable machine learning models for sentiment analysis using Steam game reviews.

## Overview

The notebook explores various techniques for creating models that are both accurate and interpretable, which is crucial for understanding why models make certain predictions.

## Dataset

- **Source**: Steam game reviews
- **File**: `steam_reviews_multi.csv`
- **Size**: ~18.5 MB
- **Content**: Multi-class sentiment data from Steam platform reviews

## Notebook Contents

- Data exploration and preprocessing
- Feature engineering for text data
- Model training with interpretability focus
- Evaluation metrics
- Model interpretation and explanation

## Requirements

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
pip install shap  # For model interpretability
```

## Usage

Open `interpretable_predictions.ipynb` in Jupyter Notebook or JupyterLab:

```bash
jupyter notebook interpretable_predictions.ipynb
```

## Key Concepts

- **Interpretability**: Understanding model decisions
- **Sentiment Analysis**: Classifying text sentiment
- **Feature Importance**: Identifying key predictive features
- **Model Explanation**: SHAP values, feature weights, decision rules

## Student

Michail Theophanopoulos
Advanced Customer Analytics - AUEB
