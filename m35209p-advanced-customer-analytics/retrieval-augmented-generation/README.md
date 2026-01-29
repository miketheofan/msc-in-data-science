# Retrieval-Augmented Generation (RAG) Pipeline

This project implements an end-to-end RAG pipeline for answering questions about climate change using semantic search and language generation.

## Overview

The pipeline combines document retrieval (finding relevant information) with text generation (creating natural language answers) to build an intelligent Q&A system that grounds its responses in provided documents.

## Architecture

```
Documents → Sentence Chunks → Embeddings → FAISS Index
                                              ↓
User Question → Embedding → Retrieval → Context → LLM → Answer
```

## Components

1. **Document Processing**: 10 climate change documents chunked into 613 sentences
2. **Embeddings**: all-MiniLM-L6-v2 (384-dimensional semantic vectors)
3. **Vector Database**: FAISS IndexFlatIP for fast similarity search
4. **Language Model**: TinyLlama 1.1B for answer generation
5. **Evaluation**: 44 Q&A pairs with similarity metrics

## Files

- `retrieval-augmented-generation.ipynb` - Main notebook
- `rag_docs.zip` - Climate change documents (auto-extracted)
- `reference_qa.csv` - Reference Q&A pairs for evaluation
- `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` - Language model (637 MB, auto-downloaded)

## Requirements

```bash
# Core dependencies
pip install sentence-transformers faiss-cpu nltk
pip install llama-cpp-python pandas numpy tqdm matplotlib seaborn

# For M2 Mac (Metal acceleration):
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/metal
```

## Usage

1. Open the notebook:
```bash
jupyter notebook retrieval-augmented-generation.ipynb
```

2. Run all cells - the notebook will:
   - Auto-extract documents from `rag_docs.zip`
   - Auto-download TinyLlama model (~700 MB, first run only)
   - Process documents and build FAISS index
   - Evaluate on 44 reference questions

## Performance

- **Answer Similarity**: 84% average similarity with reference answers
- **Retrieval Quality**: 77% average top-1 similarity score
- **Perfect Scores**: 3 questions with 100% similarity
- **Evaluation Size**: 44 questions

## Key Concepts

- **RAG (Retrieval-Augmented Generation)**: Combining retrieval with generation
- **Semantic Search**: Finding relevant text by meaning, not keywords
- **Embeddings**: Converting text to numerical vectors
- **FAISS**: Fast similarity search at scale
- **Prompt Engineering**: Crafting effective prompts for small LLMs

## Technical Details

- **Chunking Strategy**: Sentence-level with NLTK punkt tokenizer
- **Embedding Model**: all-MiniLM-L6-v2 (22M params, 384 dims)
- **Retrieval**: k=7 chunks, cosine similarity via inner product
- **Generation**: TinyLlama 1.1B, temperature=0.3, max_tokens=150
- **Prompt Format**: Simple "Context → Question → Answer" structure

## Limitations

- TinyLlama (1.1B params) occasionally produces spelling errors
- Sentence-level chunks may miss broader context
- No chunk overlap or re-ranking
- Embedding similarity is an imperfect quality metric

## Future Improvements

- Use larger models (Llama 3 8B, Mistral 7B)
- Implement hybrid search (semantic + keyword/BM25)
- Add chunk overlap and cross-encoder re-ranking
- Include source citations in generated answers

## Student

Michail Theophanopoulos
Advanced Customer Analytics - AUEB
