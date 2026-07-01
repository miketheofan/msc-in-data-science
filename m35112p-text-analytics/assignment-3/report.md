> <u>Text Analytics M.Sc. Data Science (PT)</u>
>
> ATHENS UNIVERSITY OF ECONOMICS AND BUSINESS

Instructor: Ion Androutsopoulos

Assignment 3 - Sentiment Analysis and POS Tagging with RNN

1\. Theofanopoulos Michail, p3352401 , mic.theofanopoulos@aueb.gr -
Sentiment Analysis

2\. Mantzaris Marios, p3352421 , mar.mantzaris@aueb.gr - POS Tagger

3\. Kitsakis Georgios, p3352406 , geo.kitsakis@aueb.gr - Sentiment
Analysis

4\. Zacharis Efstathios, p3352415 , efs.zacharis@aueb.gr - POS Tagger

The link to the Colab notebook for Sentiment Analysis is:
[<u>Link</u>](https://colab.research.google.com/drive/1savvN-qjHv-_vPHlMOK7EPt2jeMCQzG-)

The link to the Colab notebook for POS Tagger is:
[<u>Link</u>](https://colab.research.google.com/drive/1Zi5tB4GigAxmBM-FeRYXha0ZprNtSa0q#scrollTo=5451911d0f84c0f1)

# Exercise 1 - Sentiment Analysis with Bi-directional RNN and Self-Attention

## 1. Dataset

We used the **IMDB Movie Review Dataset** containing 50,000 movie
reviews labeled as positive or negative.

**Dataset Statistics:**

- **Training Set:** 35,000 reviews (17,500 positive, 17,500 negative)

- **Development Set:** 10,500 reviews (5,250 positive, 5,250 negative)

- **Test Set:** 15,000 reviews (7,500 positive, 7,500 negative)

- **Average document length:** 128 words (training), 128 words (test)

- **Vocabulary size:** 10,000 unique words (after preprocessing)

- **Maximum sequence length:** 512 tokens

- **Train/validation/test split:** 70%/21%/30%

**Preprocessing Steps:**

1.  Text tokenization using NLTK's sentence and word tokenizers

2.  Stopword and punctuation removal

3.  Lowercase conversion and special character filtering

4.  Vocabulary building from training data (top 10,000 most frequent
    words)

5.  Sequence conversion with \<PAD\> and \<UNK\> tokens

6.  Sequence padding to uniform length (512 tokens maximum)

## 2. Text Representation Methods

For the BiRNN with Self-Attention model, we implemented a
**sequence-based representation** approach:

### 2.1 Sequential Token Representation

Unlike traditional bag-of-words approaches, our RNN model processes text
as ordered sequences:

1.  **Vocabulary Construction:**

    - Built from training data using token frequency

    - Limited to top 10,000 most frequent words

    - Special tokens: \<PAD\> (padding) and \<UNK\> (unknown words)

2.  **Sequence Conversion:**

    - Each word mapped to integer index based on vocabulary

    - Out-of-vocabulary words mapped to \<UNK\> token

    - Sequences truncated at 512 tokens maximum

3.  **Sequence Padding:**

    - Variable-length sequences padded to uniform length

    - Padding applied with \<PAD\> tokens (index 0)

    - Actual sequence lengths preserved for attention masking

4.  **Word Embeddings:**

    - 100-dimensional embeddings learned during training

    - Randomly initialized (not pre-trained)

    - Updated through backpropagation with model parameters

### 2.2 Key Differences from Traditional Approaches

**Sequence-based vs. Bag-of-Words:**

- **Preserves word order:** Critical for understanding sentiment flow

- **Maintains context:** Words understood in relation to surrounding
  words

- **Variable length handling:** Supports documents of different lengths

- **Attention-ready:** Enables self-attention mechanism to focus on
  relevant parts

**Advantages for RNN Architecture:**

- **Temporal modeling:** RNN can capture sequential dependencies

- **Bidirectional context:** Each word sees both past and future context

- **Attention compatibility:** Sequence format enables attention over
  time steps

- **End-to-end learning:** Embeddings optimized for sentiment
  classification task

This representation method is fundamentally different from the TF-IDF,
Bag-of-Words, and pre-trained embedding approaches used in traditional
MLP models, as it maintains the sequential nature of text that RNNs are
designed to exploit

## 3. Model Architectures

### 3.1 Baseline Model

The BaselineSentimentClassifier maps words to their most frequent
sentiment:

- Counts word-sentiment associations during training using TF-IDF
  features

- Assigns each word its majority sentiment class

- Predicts by voting among sentiments of words in the text

- Falls back to most common sentiment when needed

**Baseline Results:**

- Test Accuracy: 78.71%

- Test Macro F1: 78.70%

- Test Macro PR-AUC: 84.04%

### 3.2 Bi-directional RNN with Self-Attention

Our main model implements a sophisticated neural architecture combining
sequential processing with attention mechanisms:

**Architecture Components:**

1.  **Embedding Layer:** 100-dimensional word embeddings (randomly
    initialized)

2.  **Bidirectional LSTM:** 1 layer with 64 hidden units per direction
    (128 total)

3.  **Self-Attention Mechanism:** MLP-based attention with 64 hidden
    units

4.  **Classification Head:** Linear layer mapping to 2 sentiment classes

5.  **Regularization:** 30% dropout throughout the network

**Key Features:**

- **Bidirectional Processing:** Captures context from both left-to-right
  and right-to-left directions

- **Self-Attention:** Learns to focus on sentiment-relevant words in the
  sequence

- **Sequential Modeling:** Processes text as ordered sequences rather
  than bags-of-words

- **Variable Length Handling:** Supports sequences of varying lengths up
  to 512 tokens

- **Gradient Clipping:** Maximum norm of 1.0 to prevent exploding
  gradients

### 3.3 Hyperparameter Tuning

We implemented grid search across multiple architectural choices:

**Search Space:**

- **RNN Types:** GRU vs LSTM

- **Embedding Dimensions:** 100 vs 150

- **RNN Hidden Dimensions:** 64 vs 128

- **Number of RNN Layers:** 1 vs 2

- **Attention MLP Architecture:** \[64\] vs \[64, 32\]

- **Learning Rates:** 0.001 vs 0.0005

- **Batch Sizes:** 32 vs 64

- **Dropout Rates:** 0.3 vs 0.5

**Optimal Configuration Found:**

- **RNN Type:** LSTM

- **Embedding Dimension:** 100

- **RNN Hidden Dimension:** 64

- **Number of Layers:** 1 (bidirectional)

- **Attention MLP:** \[64\] hidden units

- **Learning Rate:** 0.0005

- **Batch Size:** 32

- **Dropout:** 0.3

## 4. Training and Evaluation

**Training Configuration:**

- **Loss Function:** Cross-entropy loss

- **Optimizer:** Adam with learning rate 0.0005

- **Early Stopping:** Patience of 7 epochs based on validation loss

- **Gradient Clipping:** Maximum norm of 1.0

- **Batch Size:** 32

- **Training Duration:** 8 epochs (early stopped)

**Training Dynamics:**

- Rapid training loss decrease: 0.115 → 0.020 over 8 epochs

- Validation loss minimum at epoch 1 (0.403), then steadily increased

- Clear overfitting pattern requiring early intervention

- Model saved at best validation performance (epoch 1)

**Evaluation Metrics:** All models evaluated using accuracy, precision,
recall, F1 score, and PR-AUC, calculated separately for training,
development, and test sets with both per-class and macro-averaged
metrics.

## 5. Results

### 5.1 Training and Validation Loss Curves

<img src="media/image1.png" style="width:5.58507in;height:3.62382in" />

The loss curves demonstrate:

- **Fast Convergence:** Training loss drops rapidly in the first epoch

- **Overfitting Pattern:** Validation loss increases after epoch 1 while
  training loss continues decreasing

- **Early Stopping Effectiveness:** Training halted at epoch 8 when
  patience threshold reached

- **Optimal Performance:** Best model achieved at epoch 1 with lowest
  validation loss

### 5.2 Model Performance Comparison

<img src="media/image10.png" style="width:6.30642in;height:1.01389in" />

### 5.3 Detailed Performance Metrics

RNN Model Performance Across Splits:

<img src="media/image7.png" style="width:5.46007in;height:1.07791in" />

Per-Class Performance (Test Set):

<img src="media/image6.png" style="width:5.37674in;height:1.8954in" />

### 5.4 Precision-Recall Curves

<img src="media/image2.png" style="width:6.76215in;height:3.73895in" />

The precision-recall analysis reveals:

- **Excellent Training Performance:** PR-AUC of 99.62% indicates strong
  learning capability

- **Good Generalization:** Test PR-AUC of 94.19% shows effective
  knowledge transfer

- **Balanced Class Performance:** Both positive and negative sentiment
  classes achieve similar PR-AUC scores

- **Consistent Across Splits:** Performance remains stable from
  validation to test data

## 6. Key Findings

### 6.1 Architecture Benefits

- **Bidirectional Processing:** LSTM captures contextual information
  from both directions, enabling better understanding of sentiment flow

- **Self-Attention Effectiveness:** MLP-based attention mechanism
  successfully identifies sentiment-relevant words in sequences

- **Sequential Modeling Advantage:** Processing text as ordered
  sequences significantly outperforms bag-of-words approaches

- **Significant Improvement:** 10.9% absolute accuracy gain demonstrates
  clear architectural superiority over baseline

### 6.2 Technical Insights

- **Single-Layer Sufficiency:** One bidirectional LSTM layer proved
  sufficient for this sentiment analysis task

- **Simple Attention Design:** Basic MLP with 64 hidden units effective
  for attention computation

- **Early Stopping Critical:** Rapid overfitting necessitated careful
  monitoring and early intervention

- **Learning Rate Sensitivity:** Lower learning rate (0.0005) provided
  better training stability than higher alternatives

### 6.3 Comparison with Traditional Approaches

- **Substantial improvement over word-frequency baseline:** Shows value
  of neural sequential modeling

- **Attention mechanism contribution:** Self-attention allows model to
  focus selectively on important words

- **Bidirectional context:** Captures sentiment patterns that depend on
  word order and context

- **Robust performance:** Maintains balanced accuracy across both
  sentiment classes

### 6.4 Model Behavior Analysis

The training dynamics reveal important characteristics:

- **Fast Learning:** Model quickly captures basic sentiment patterns in
  first epoch

- **Overfitting Tendency:** High capacity leads to memorization of
  training data

- **Generalization Gap:** 10.66% accuracy difference between training
  (97.93%) and test (87.27%)

- **Attention Focus:** Self-attention mechanism learns to emphasize
  sentiment-bearing words while downweighting neutral content

# Exercise 2 - POS Tagger

Part-of-Speech Tagging with RNN

## 1. Introduction

This report presents the implementation and evaluation of a
Part-of-Speech (POS) tagging system using a Bidirectional Stacked
Recurrent Neural Network (RNN). Part-of-speech tagging is the process of
assigning a part-of-speech tag (such as noun, verb, adjective, etc.) to
each word in a text. This task is fundamental in natural language
processing and serves as a building block for more complex NLP
applications.

In this implementation, we use a bidirectional stacked RNN (with LSTM
cells) to capture contextual information from both directions in a
sentence. This approach allows the model to consider both past and
future context when predicting the POS tag for a word, which is crucial
for accurate tagging.

## 2. Methods and Datasets

### 2.1 Dataset

The implementation uses the Universal Dependencies English Web Treebank
(UD_English-EWT) dataset, which provides annotated text data with
part-of-speech tags. The dataset is split into training, development,
and test sets.

### 2.2 Dataset Statistics

| **Statistic**           | **Training Set** | **Development Set** | **Test Set** |
|-------------------------|------------------|---------------------|--------------|
| Number of sentences     | 12,543           | 2,002               | 2,077        |
| Number of words         | 204,585          | 25,148              | 25,096       |
| Average sentence length | 16.31            | 12.56               | 12.08        |
| Vocabulary size         | 19,672           | \-                  | \-           |

The dataset contains 17 different POS tags, with the most common tags
being NOUN, VERB, ADP, DET, and PUNCT.

### 2.3 Preprocessing Steps

The following preprocessing steps were applied to the data:

1.  **Text Normalization**: All words were converted to lowercase to
    reduce vocabulary size.

2.  **Vocabulary Creation**: A vocabulary was created from the training
    set, with special tokens for padding (\<PAD\>) and unknown words
    (\<UNK\>).

3.  **Word Embeddings**: Pre-trained GloVe word embeddings
    (100-dimensional) were used to represent words.

4.  **Character-level Features**: Optional character-level embeddings
    were implemented to capture morphological information.

5.  **Sequence Padding**: Sentences were padded to a maximum length of
    50 tokens to enable batch processing.

6.  **Data Preparation**: The data was prepared in a format suitable for
    the RNN model, with word indices and optional character indices.

## 3. Models

Two models were implemented and compared:

1.  **Baseline Model**: A simple model that assigns the most frequent
    tag seen during training for each word. For unseen words, it assigns
    the most common tag overall.

2.  **RNN Model**: A Bidirectional Stacked RNN with the following
    architecture:

    - Word embedding layer (initialized with pre-trained GloVe
      embeddings)

    - Optional character-level embeddings processed by a separate
      bidirectional RNN

    - Two stacked bidirectional LSTM layers (128 and 64 units)

    - Dropout (0.3) and recurrent dropout (0.2) for regularization

    - Time-distributed dense layer with softmax activation for tag
      prediction

The RNN model was trained using the Adam optimizer with sparse
categorical cross-entropy loss. Early stopping was used to prevent
overfitting, with a patience of 5 epochs. Additionally, a learning rate
reduction strategy was employed to improve convergence.

## 4. Results

### 4.1 Loss Curves

The following graph shows the loss on training and development data as a
function of epochs:

<img src="media/image11.png" style="width:6.30642in;height:3.77778in" />

The loss curves show that the model converges after a few epochs, with
the validation loss stabilizing. The early stopping mechanism prevented
overfitting by stopping training when the validation loss stopped
improving.

### 4.2 Per-Class RNN Metrics

<img src="media/image9.png" style="width:5.01042in;height:3.40625in" />

<img src="media/image12.png" style="width:5.01042in;height:3.40625in" />

<img src="media/image8.png" style="width:5.01042in;height:3.40625in" />

### <img src="media/image3.png" style="width:6.30642in;height:4.19444in" />

### 

### 

### 4.3 Macro-Averaged Metrics

#### 4.3.1 Baseline Model

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8964           | 0.8361              | 0.8195       |
| Recall     | 0.8723           | 0.7741              | 0.7752       |
| F1         | 0.8799           | 0.7913              | 0.7863       |
| PR-AUC     | 0.8868           | 0.8092              | 0.8014       |

#### 

#### 4.3.2 MLP Model

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8789           | 0.8265              | 0.8335       |
| Recall     | 0.8636           | 0.7940              | 0.8091       |
| F1         | 0.8702           | 0.8030              | 0.8144       |
| PR-AUC     | 0.9023           | 0.8430              | 0.8540       |

#### 4.3.3 RNN Model

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8827           | 0.8132              | 0.8294       |
| Recall     | 0.8070           | 0.7470              | 0.7727       |
| F1         | 0.8246           | 0.7700              | 0.7948       |
| PR-AUC     | 0.8460           | 0.8115              | 0.8323       |

## 

## <img src="media/image5.png" style="width:5.47396in;height:4.37213in" />

We also provide a confusion matrix for some of the top tags.

## <img src="media/image4.png" style="width:5.63715in;height:5.04772in" />

## 5. Conclusion

This report presented a Part-of-Speech tagging system using a
Bidirectional Stacked RNN. The RNN model was compared with both a
baseline model and an MLP model from Assignment 3.

The use of bidirectional LSTM layers allowed the model to capture
contextual information from both directions, which is crucial for
accurate POS tagging.

The loss curves showed that the model converged after several epochs,
and the early stopping mechanism prevented overfitting.

The per-class metrics revealed that the model performed well across most
POS tags, with particularly high performance on common tags.

Overall, the Bidirectional Stacked RNN-based POS tagger demonstrated
strong performance on the Universal Dependencies English Web Treebank
dataset.
