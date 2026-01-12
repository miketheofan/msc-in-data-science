# Visual Data Predictions

This project implements machine learning models that work with visual data (images) to make predictions about Pokemon card attributes.

## Overview

The notebook demonstrates how to process image data, extract features, and build predictive models using computer vision techniques.

## Dataset

- **Source**: Pokemon Trading Card Game cards
- **Images**: 6000 card images in `pokemon_cards/images/`
- **Metadata**: `pokemon_cards/pokemon_cards_metadata.csv` (~4 MB)
- **Content**: Pokemon card images with associated metadata (rarity, type, HP, etc.)

## Notebook Contents

- Image data loading and preprocessing
- Visual feature extraction
- Exploratory data analysis with images
- Model training for card attribute prediction
- Performance evaluation and visualization

## Requirements

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
pip install pillow opencv-python  # For image processing
pip install tensorflow  # Or pytorch, depending on implementation
```

## Usage

Open `visual-data-predictions.ipynb` in Jupyter Notebook:

```bash
jupyter notebook visual-data-predictions.ipynb
```

## Key Concepts

- **Computer Vision**: Processing and analyzing images
- **Feature Extraction**: Converting images to numerical features
- **Image Classification**: Predicting categories from images
- **Deep Learning**: CNNs for visual data
- **Transfer Learning**: Using pre-trained models

## Dataset Structure

```
pokemon_cards/
├── images/           # 6000 Pokemon card images
└── pokemon_cards_metadata.csv  # Card attributes and labels
```

## Student

Michail Theophanopoulos
Advanced Customer Analytics - AUEB
