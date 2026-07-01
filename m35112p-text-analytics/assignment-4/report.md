> <u>Text Analytics M.Sc. Data Science (PT)</u>
>
> ATHENS UNIVERSITY OF ECONOMICS AND BUSINESS

Instructor: Ion Androutsopoulos

Assignment 4 - Sentiment Analysis and POS Tagging with CNN

1\. Theofanopoulos Michail, p3352401 , mic.theofanopoulos@aueb.gr -
Sentiment Analysis

2\. Mantzaris Marios, p3352421 , mar.mantzaris@aueb.gr - POS Tagger

3\. Kitsakis Georgios, p3352406 , geo.kitsakis@aueb.gr - Sentiment
Analysis

4\. Zacharis Efstathios, p3352415 , efs.zacharis@aueb.gr - POS Tagger

The link to the Colab notebook for Sentiment Analysis is:
[<u>Link</u>](https://colab.research.google.com/drive/1obCSdHwv_TaJpgLhmAn6KWfdTD4BfaqE)

The link to the Colab notebook for POS Tagger is:
[<u>Link</u>](https://colab.research.google.com/drive/1XO8pVamLIG53eCGd6UFeOOpq56TTVnfH)

# 

# 

# 

# 

# 

# **Exercise 2 - Sentiment Analysis with Convolutional Neural Networks and N-gram Filters**

## **1. Dataset**

We used the **IMDB Movie Review Dataset** containing 50,000 movie
reviews labeled as positive or negative.

**Dataset Statistics:**

- **Training Set:** 35,000 reviews (17,500 positive, 17,500 negative)

- **Development Set:** 10,500 reviews (5,250 positive, 5,250 negative)

- **Test Set:** 15,000 reviews (7,500 positive, 7,500 negative)

- **Average document length:** 129.7 words (training), 132.7 words
  (test)

- **Vocabulary size:** 10,000 unique words (after preprocessing)

- **Maximum sequence length:** 256 tokens

- **Train/validation/test split:** 70%/21%/30%

**Preprocessing Steps:**

1.  Text tokenization using NLTK's sentence and word tokenizers

2.  Stopword and punctuation removal

3.  Lowercase conversion and special character filtering

4.  Vocabulary building from training data (top 10,000 most frequent
    words)

5.  Sequence conversion with \<PAD\> and \<UNK\> tokens

6.  Sequence padding to uniform length (256 tokens maximum)

7.  Pre-trained Word2Vec/GloVe embeddings integration (300 dimensions)

## **2. Text Representation Methods**

For the CNN models, we implemented a **sequence-based representation**
with pre-trained embeddings:

### **2.1 Sequential Token Representation with Pre-trained Embeddings**

Our CNN models process text as ordered sequences with rich semantic
representations:

1.  **Vocabulary Construction:**

    - Built from training data using token frequency

    - Limited to top 10,000 most frequent words

    - Special tokens: \<PAD\> (padding) and \<UNK\> (unknown words)

2.  **Sequence Conversion:**

    - Each word mapped to integer index based on vocabulary

    - Out-of-vocabulary words mapped to \<UNK\> token

    - Sequences truncated at 256 tokens maximum

3.  **Sequence Padding:**

    - Variable-length sequences padded to uniform length

    - Padding applied with \<PAD\> tokens (index 0)

    - Maintains spatial structure for convolutional processing

4.  **Pre-trained Word Embeddings:**

    - 300-dimensional Word2Vec embeddings from Google News corpus

    - 9,109 out of 10,000 vocabulary words found in pre-trained
      embeddings

    - Embeddings fine-tuned during training (not frozen)

    - Significant semantic knowledge transfer from large corpus

### **2.2 Key Differences from Traditional Approaches**

**Sequence-based vs. Bag-of-Words:**

- **Preserves spatial structure:** Critical for convolutional filters to
  capture n-gram patterns

- **Maintains local context:** Words understood in relation to
  neighboring words

- **N-gram pattern recognition:** Enables detection of local sentiment
  patterns

- **Position-aware processing:** Convolutional filters scan across
  sequential positions

**Advantages for CNN Architecture:**

- **Local pattern detection:** Convolutional filters capture n-gram
  features (2,3,4-grams)

- **Translation invariance:** Same patterns detected regardless of
  position in text

- **Hierarchical feature learning:** Stacked layers build complex
  patterns from simple ones

- **Parallel processing:** Multiple filters operate simultaneously on
  different pattern types

This representation method enables CNNs to detect local linguistic
patterns while leveraging pre-trained semantic knowledge, fundamentally
different from the sequential processing approach used in RNN models.

## **3. Model Architectures**

### **3.1 Baseline Model**

The BaselineSentimentClassifier maps words to their most frequent
sentiment:

- Uses TF-IDF vectorization with maximum 2,000 features

- Assigns each word its majority sentiment class from training data

- Predicts by voting among sentiments of words in the text

- Falls back to most common sentiment for unknown words

**Baseline Results:**

- Test Accuracy: 78.15%

- Test Macro F1: 78.14%

- Test Macro PR-AUC: 83.64%

### **3.2 Convolutional Neural Networks with N-gram Filters**

We implemented multiple CNN architectures with different design choices:

#### **3.2.1 Single Filter CNN Architecture**

**Architecture Components:**

1.  **Embedding Layer:** 300-dimensional pre-trained Word2Vec embeddings

2.  **Stacked Convolutional Layers:** 1-3 layers with configurable
    n-gram filters (2, 3, or 4-gram)

3.  **Residual Connections:** Skip connections between convolutional
    layers

4.  **Batch Normalization:** Applied after each convolutional layer

5.  **Global Max-Pooling or Self-Attention:** Sequence aggregation
    mechanism

6.  **Classification Head:** Linear layer mapping to 2 sentiment classes

7.  **Regularization:** 30-50% dropout throughout the network

#### **3.2.2 Multi-Filter CNN Architecture**

**Enhanced Design:**

1.  **Parallel N-gram Filters:** Simultaneous 2-gram, 3-gram, and 4-gram
    processing

2.  **Independent Filter Paths:** Separate processing for each n-gram
    size

3.  **Feature Concatenation:** Combining outputs from all filter types

4.  **Residual Connections:** Within each filter path for gradient flow

5.  **Attention or Max-Pooling:** Choice of aggregation mechanism

**Key Features:**

- **Multiple N-gram Captures:** Detects patterns of varying
  granularities simultaneously

- **Residual Learning:** Enables training of deeper networks

- **Pre-trained Initialization:** Leverages semantic knowledge from
  large corpora

- **Flexible Aggregation:** Max-pooling focuses on strongest features;
  attention provides weighted combination

### **3.3 Hyperparameter Tuning**

We implemented systematic search across architectural configurations:

**Search Space:**

- **Model Types:** Single-filter vs Multi-filter CNN

- **N-gram Filter Sizes:** 2, 3, 4 (for single-filter models)

- **Number of Filters:** 64 vs 100 per layer

- **Network Depth:** 1-3 convolutional layers

- **Aggregation Method:** Global max-pooling vs Self-attention

- **Learning Rates:** 0.001 vs 0.0005

- **Batch Sizes:** 32 vs 64

- **Dropout Rates:** 0.3, 0.4, 0.5

- **Embedding Training:** Frozen vs trainable pre-trained embeddings

**Optimal Configuration Found:**

- **Model Type:** Single-filter CNN

- **N-gram Size:** 3 (trigram filters)

- **Number of Filters:** 64

- **Network Depth:** 3 convolutional layers

- **Aggregation:** Self-attention mechanism

- **Learning Rate:** 0.0005

- **Batch Size:** 64

- **Dropout:** 0.4

- **Embeddings:** Frozen pre-trained Word2Vec

## **4. Training and Evaluation**

**Training Configuration:**

- **Loss Function:** Cross-entropy loss

- **Optimizer:** Adam with learning rate 0.0005

- **Early Stopping:** Patience of 7 epochs based on validation loss

- **Gradient Clipping:** Maximum norm of 1.0

- **Batch Size:** 32

- **Training Duration:** Variable per model (5-15 epochs with early
  stopping)

**Training Dynamics:**

- Rapid convergence within first 5 epochs for most models

- Clear overfitting patterns requiring early intervention

- Residual connections improved training stability

- Pre-trained embeddings accelerated convergence

**Evaluation Metrics:** All models evaluated using accuracy, precision,
recall, F1 score, and PR-AUC, calculated separately for training,
development, and test sets with both per-class and macro-averaged
metrics.

## **5. Results**

### **5.1 Training and Validation Loss Curves**

<img src="media/image7.png" style="width:6.26772in;height:4.01389in" />

Training and validation loss curves for the best CNN model
(CNN_Trigram_Attention) showing convergence behavior over 20 epochs. The
model achieved best validation loss at epoch 13 before early stopping.

<img src="media/image1.png" style="width:6.26772in;height:4.18056in" />

Comparison of training and validation loss curves across all CNN
architectures. The curves demonstrate:

- **Fast Convergence:** Most models converge within 2-3 epochs due to
  pre-trained embeddings

- **Overfitting Patterns:** Clear divergence between training and
  validation losses across all architectures

- **Architecture Differences:** Attention-based models (brown/cyan
  lines) show more stable validation curves compared to max-pooling
  variants

- **Early Stopping Effectiveness:** All models stopped training when
  validation loss plateaued or increased, preventing severe overfitting

**Key insights from the comparison:**

- **MultiFilter models** (yellow/pink lines): Show the fastest training
  convergence

- **Attention models** (brown/cyan lines): More stable validation
  performance

- **MaxPool models** (green/red lines): Rapid overfitting after epoch
  2-3

- **Residual connections** enable stable gradient flow across all
  architectures

<!-- -->

- 

### **5.2 Model Performance Comparison**

<img src="media/image13.png" style="width:6.26772in;height:0.98611in" />

<img src="media/image11.png" style="width:6.26772in;height:1.54167in" />

### **5.3 Detailed Performance Metrics**

**Best CNN Model Performance Across Splits:**

<img src="media/image8.png" style="width:6.26772in;height:1.09722in" />

**Per-Class Performance (Test Set):**

<img src="media/image6.png" style="width:6.26772in;height:1.97222in" />

### **5.4 Precision-Recall Curves**

<img src="media/image2.png" style="width:6.49479in;height:3.59263in" />

The precision-recall analysis reveals:

- **Strong Pattern Recognition:** CNN models effectively capture n-gram
  sentiment patterns

- **Balanced Performance:** Both sentiment classes achieve similar
  performance

- **Pre-trained Boost:** Word2Vec embeddings provide significant
  semantic understanding

- **Architecture Effectiveness:** Multi-filter models capture diverse
  pattern types

## **6. Key Findings**

### **6.1 Architecture Benefits**

- **N-gram Filter Effectiveness:** Convolutional filters successfully
  capture local sentiment patterns of different granularities

- **Residual Connection Value:** Skip connections enable training of
  deeper networks and improve gradient flow

- **Pre-trained Embedding Impact:** Word2Vec initialization provides
  substantial performance boost over random initialization

- **Significant Improvement:** 14.3% absolute accuracy gain demonstrates
  CNN effectiveness for text classification

### **6.2 Technical Insights**

- **Filter Size Optimization:** Trigram filters proved most effective
  for this sentiment analysis task

- **Depth vs Width Trade-off:** Deeper networks (3 layers) with
  attention outperformed shallower alternatives

- **Aggregation Method Comparison:** Self-attention consistently
  outperformed max-pooling across architectures

- **Multi-Filter Architecture:** Parallel n-gram processing captures
  complementary features effectively

### **6.3 Comparison with RNN Approaches**

- **Different Strengths:** CNNs excel at local pattern detection while
  RNNs capture long-range dependencies

- **Training Efficiency:** CNNs train faster due to parallel processing
  of n-gram patterns

- **Feature Types:** CNN filters detect specific linguistic patterns;
  RNNs model sequential dependencies

- **Pre-trained Benefits:** Both architectures benefit significantly
  from pre-trained embeddings

### **6.4 Model Behavior Analysis**

The training dynamics reveal important characteristics:

- **Pattern Recognition Speed:** CNNs quickly learn discriminative
  n-gram features

- **Local Focus:** Filters specialize in detecting sentiment-bearing
  phrases

- **Composition Benefits:** Multiple filter sizes capture different
  aspects of sentiment expression

- **Stability:** Residual connections and batch normalization provide
  stable training

### **6.5 CNN-Specific Observations**

- **Filter Specialization:** Different n-gram sizes capture distinct
  types of sentiment patterns:

  - 2-grams: Negations, simple sentiment pairs

  - 3-grams: Short sentiment phrases

  - 4-grams: Complex sentiment expressions

- **Max-pooling Effectiveness:** Global max-pooling successfully
  identifies the strongest sentiment indicators

- **Attention Alternative:** Self-attention provides interpretable
  feature weighting as alternative to max-pooling

- **Residual Learning:** Skip connections crucial for training deeper
  CNN architectures on text

# **Exercise 3 - POS Tagger**

Part-of-Speech Tagging with CNN

## **1. Introduction**

This report presents the implementation and evaluation of a
Part-of-Speech (POS) tagging system using Convolutional Neural Networks
(CNNs). Part-of-speech tagging is the process of assigning a
part-of-speech tag (such as noun, verb, adjective, etc.) to each word in
a text. This task is fundamental in natural language processing and
serves as a building block for more complex NLP applications.

In this implementation, we use a stacked CNN with n-gram filters (n = 2,
3, 4), residual connections, and a dense layer with softmax at the top
layer for POS tagging. This approach allows the model to capture local
patterns in the text, which is particularly useful for tasks like POS
tagging where local context is important.

## **2. Methods and Datasets**

### **2.1 Dataset**

The implementation uses the Universal Dependencies English Web Treebank
(UD_English-EWT) dataset, which provides annotated text data with
part-of-speech tags. The dataset is split into training, development,
and test sets.

### **2.2 Dataset Statistics**

| **Statistic**           | **Training Set** | **Development Set** | **Test Set** |
|-------------------------|------------------|---------------------|--------------|
| Number of sentences     | 12,543           | 2,002               | 2,077        |
| Number of words         | 204,585          | 25,148              | 25,096       |
| Average sentence length | 16.31            | 12.56               | 12.08        |
| Vocabulary size         | 19,672           | \-                  | \-           |

The dataset contains 17 different POS tags, with the most common tags
being NOUN, VERB, ADP, DET, and PUNCT.

### **2.3 Preprocessing Steps**

The following preprocessing steps were applied to the data:

1.  **Text Normalization**: All words were converted to lowercase to
    reduce vocabulary size.

2.  **Vocabulary Creation**: A vocabulary was created from the training
    set, with special tokens for padding (\<PAD\>) and unknown words
    (\<UNK\>).

3.  **Word Embeddings**: Pre-trained GloVe word embeddings
    (100-dimensional) were used to represent words.

4.  **Character-level Features**: Character-level embeddings were
    implemented to capture morphological information.

5.  **Sequence Padding**: Sentences were padded to a maximum length of
    50 tokens to enable batch processing.

6.  **Data Preparation**: The data was prepared in a format suitable for
    the CNN model, with word indices and character indices.

## **3. Models**

Two models were implemented and compared:

1.  **Baseline Model**: A simple model that assigns the most frequent
    tag seen during training for each word. For unseen words, it assigns
    the most common tag overall.

2.  **CNN Model:** A Multi-filter CNN with residual connections with the
    following architecture:

    - Word embedding layer (initialized with pre-trained GloVe
      embeddings)

    - Character-level embeddings processed by a separate CNN

    - Multiple parallel convolutional layers with different filter sizes
      (2, 3, and 4) to capture n-gram patterns

    - Residual connections between convolutional layers to facilitate
      training of deeper networks

    - Dropout (0.3) for regularization

    - Time-distributed dense layer with softmax activation for tag
      prediction

### **3.1 Hyperparameter Tuning**

A grid search approach was used to tune the following hyperparameters:

- Number of CNN filters: \[64, 128, 256\]

- Number of CNN layers: \[1, 2, 3\]

- Dropout rate: \[0.3, 0.5\]

The best hyperparameters were:

Number of CNN filters: 256

Number of CNN layers: 3

Dropout rate: 0.3

The CNN model was trained using the Adam optimizer with sparse
categorical cross-entropy loss. Early stopping was used to prevent
overfitting, with a patience of 5 epochs. Additionally, a learning rate
reduction strategy was employed to improve convergence.

## **4. Results**

### **4.1 Loss Curves**

The following graph shows the loss on training and development data as a
function of epochs:

<img src="media/image4.png" style="width:6.26772in;height:4.01389in" />

The loss curves show that the model converges after a few epochs, with
the validation loss stabilizing. The early stopping mechanism prevented
overfitting by stopping training when the validation loss stopped
improving.

**4.2 Per-Class CNN Metrics**

### <img src="media/image16.png" style="width:6.14583in;height:3.375in" />

<img src="media/image15.png" style="width:6.14583in;height:3.375in" />

### <img src="media/image12.png" style="width:5.87755in;height:3.32813in" />

### **4.3 Macro-Averaged Metrics**

#### **4.3.1 Baseline Model**

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8964           | 0.8361              | 0.8195       |
| Recall     | 0.8723           | 0.7741              | 0.7752       |
| F1         | 0.8799           | 0.7913              | 0.7863       |
| PR-AUC     | 0.8868           | 0.8092              | 0.8014       |

#### 

#### **4.3.2 MLP Model**

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8789           | 0.8265              | 0.8335       |
| Recall     | 0.8636           | 0.7940              | 0.8091       |
| F1         | 0.8702           | 0.8030              | 0.8144       |
| PR-AUC     | 0.9023           | 0.8430              | 0.8540       |

#### **4.3.3 RNN Model**

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8827           | 0.8132              | 0.8294       |
| Recall     | 0.8070           | 0.7470              | 0.7727       |
| F1         | 0.8246           | 0.7700              | 0.7948       |
| PR-AUC     | 0.8460           | 0.8115              | 0.8323       |

#### **4.3.4 CNN Model**

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.9137           | 0.8603              | 0.8636       |
| Recall     | 0.8930           | 0.8087              | 0.8258       |
| F1         | 0.9015           | 0.8231              | 0.8307       |
| PR-AUC     | 0.9040           | 0.8361              | 0.8462       |

<img src="media/image3.png" style="width:6.26772in;height:3.11111in" />

<img src="media/image14.png" style="width:5.53273in;height:2.75521in" />

## <img src="media/image10.png" style="width:6.26772in;height:3.11111in" />

<img src="media/image5.png" style="width:6.18229in;height:3.06473in" />

We also provide a confusion matrix for some of the top tags.

## <img src="media/image9.png" style="width:6.26772in;height:5.625in" />

## **5. Conclusion**

This report presented a Part-of-Speech tagging system using a
Convolutional Neural Network with n-gram filters and residual
connections. The CNN model was compared with a baseline model, an MLP
model from Assignment 3, and an RNN model from Assignment 4.

**Key findings:**

- The CNN model with n-gram filters (n = 2, 3, 4) and residual
  connections performs well for POS tagging.

- The use of character-level embeddings helps capture morphological
  information.

- Residual connections help in training deeper networks by addressing
  the vanishing gradient problem.

- The CNN model is faster to train than RNNs while still capturing local
  patterns effectively.
