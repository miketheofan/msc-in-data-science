# Exercise 3 – N-gram Language Models & Context-Aware Spelling Correction

This exercise consists of building and evaluating bigram and trigram language models, using them to generate text and correct corrupted sentences.

---

### 1. Train Language Models

- Implement a **bigram** and a **trigram** language model.
- Use **Laplace smoothing** (or optionally **Kneser-Ney**).
- Add special tokens:
  - Bigram: `*start*`, `*end*`
  - Trigram: `*start1*`, `*start2*`, `*end*`
- Use a training subset of a corpus (e.g., from NLTK).
- Keep only words that occur at least a threshold number of times (e.g., 10); replace others with `*UNK*`.

---

### 2. Evaluate Cross-Entropy and Perplexity

- Evaluate the trained models on a test subset.
- Treat the test set as one long sequence of sentences.
- Exclude probabilities of start tokens from calculations.
- Include `*end*` tokens in both probability computation and total token count.
- Report:
  - **Cross-Entropy**
  - **Perplexity**

---

### 3. Sentence Autocompletion

- Use the models to complete a partial sentence (e.g., `"I would like to commend the"`).
- Generate continuations by:
  - Selecting the most probable next word (greedy), or
  - (Optionally) using beam search, top-K, or nucleus sampling.
- Compare the fluency of completions between the bigram and trigram models.

---

### 4. Spelling Correction via Noisy Channel

- Implement a **context-aware spelling corrector**:
  - Use inverse Levenshtein distance to estimate `P(w|t)`
    \[
    P(w|t) = \frac{1}{LD(w, t) + 1}
    \]
  - Combine with the language model:
    \[
    \hat{t} = \arg\max_t \lambda_1 \log P(t) + \lambda_2 \log P(w|t)
    \]
  - Use **beam search** for decoding.

---

### 5. Create a Corrupted Test Set

- Take test sentences and randomly modify characters in non-space positions.
- E.g., `"This is a test"` → `"Thiz is a tezt"`
- Use the original sentence as the reference.

---

### 6. Evaluate Correction Quality

- Use the original sentence as ground truth.
- Compare to the corrected output using:
  - **Word Error Rate (WER)**
  - **Character Error Rate (CER)**

---

## 📌 Deliverables

Include in your report:

- Cross-entropy & perplexity for both models
- Sentence completion examples (good + bad)
- Spelling correction examples
- WER and CER scores (averaged over the test set)
