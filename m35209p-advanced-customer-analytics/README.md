# Advanced Customer Analytics

Course repository for Advanced Customer Analytics at Athens University of Economics and Business (AUEB).

**Student**: Michail Theophanopoulos
**Trimester**: 4
**Institution**: AUEB

---

## 📚 Course Projects

### 1. [Interpretable Predictions](./interpretable-predictions/)

Machine learning models with interpretability focus using Steam game reviews.

**Key Topics**: Sentiment analysis, model interpretability, SHAP values, feature importance

**Technologies**: scikit-learn, SHAP, pandas, matplotlib

**Dataset**: 18.5 MB Steam reviews with multi-class sentiment

### 2. [Visual Data Predictions](./visual-data-predictions/)

Computer vision models for predicting Pokemon card attributes from images.

**Key Topics**: Image classification, feature extraction, CNNs, transfer learning

**Technologies**: TensorFlow/PyTorch, OpenCV, PIL

**Dataset**: 6000 Pokemon card images with metadata

### 3. [Retrieval-Augmented Generation (RAG)](./retrieval-augmented-generation/)

End-to-end RAG pipeline for climate change Q&A using semantic search and LLMs.

**Key Topics**: RAG, embeddings, FAISS, semantic search, prompt engineering

**Technologies**: sentence-transformers, FAISS, llama-cpp-python, NLTK

**Performance**: 84% answer similarity, 77% retrieval quality

**Dataset**: 10 climate documents, 44 Q&A pairs

---

## 📓 Lecture Notebooks

The [`notebooks/`](./notebooks/) folder contains working notebooks from lectures 1-9, including demonstrations, exercises, and reference code.

---

## 🛠️ Tech Stack

### Machine Learning
- scikit-learn
- TensorFlow / PyTorch
- XGBoost / LightGBM

### NLP & LLMs
- sentence-transformers
- llama-cpp-python
- NLTK
- FAISS

### Computer Vision
- OpenCV
- PIL / Pillow

### Data & Visualization
- pandas
- numpy
- matplotlib
- seaborn

### Model Interpretability
- SHAP

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.8+
python --version

# Jupyter
pip install jupyter
```

### Installation

Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd advanced-customer-analytics

# Install common dependencies
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# For specific projects, see individual README files
```

### Running Projects

Each project has its own README with specific instructions:

```bash
# Example: Run RAG project
cd retrieval-augmented-generation
jupyter notebook retrieval-augmented-generation.ipynb
```

---

## 📊 Project Summary

| Project | Focus Area | Key Technique | Dataset Size |
|---------|-----------|---------------|--------------|
| Interpretable Predictions | NLP + ML | Model Interpretability | 18.5 MB |
| Visual Data Predictions | Computer Vision | Image Classification | 6000 images |
| RAG Pipeline | NLP + GenAI | Semantic Search + LLM | 10 docs + 44 Q&A |

---

## 📂 Repository Structure

```
advanced-customer-analytics/
├── interpretable-predictions/
│   ├── interpretable_predictions.ipynb
│   ├── steam_reviews_multi.csv
│   └── README.md
│
├── visual-data-predictions/
│   ├── visual-data-predictions.ipynb
│   ├── pokemon_cards/
│   │   ├── images/ (6000 images)
│   │   └── pokemon_cards_metadata.csv
│   └── README.md
│
├── retrieval-augmented-generation/
│   ├── retrieval-augmented-generation.ipynb
│   ├── rag_docs.zip
│   ├── reference_qa.csv
│   └── README.md
│
├── notebooks/
│   ├── lecture1/ through lecture9/
│   └── README.md
│
└── README.md (this file)
```

---

## 🎯 Learning Outcomes

This course covered:

1. **Interpretable ML**: Building models that explain their predictions
2. **Computer Vision**: Working with image data for predictions
3. **RAG Systems**: Combining retrieval with language generation
4. **Model Evaluation**: Proper metrics and validation techniques
5. **Production Considerations**: Scalability, interpretability, deployment

---

## 📝 Notes

- Large files (models, datasets >100MB) are not tracked in git
- See `.gitignore` for excluded files
- Each project can run independently
- Some projects auto-download required models on first run

---

## 🏆 Course Completion

This repository represents the complete coursework for Advanced Customer Analytics at AUEB, demonstrating proficiency in:
- Traditional machine learning with interpretability
- Deep learning for computer vision
- Modern NLP and generative AI (RAG)
- Production-ready implementations
- Comprehensive evaluation methodologies

---

## 📧 Contact

**Michail Theophanopoulos**
Athens University of Economics and Business (AUEB)

---

*Repository last updated: January 2026*
