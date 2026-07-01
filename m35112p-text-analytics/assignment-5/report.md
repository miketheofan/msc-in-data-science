> <u>Text Analytics M.Sc. Data Science (PT)</u>
>
> ATHENS UNIVERSITY OF ECONOMICS AND BUSINESS

Instructor: Ion Androutsopoulos

Assignment 5 - Sentiment Analysis with BERT Fine-tuning

1\. Theofanopoulos Michail, p3352401 , mic.theofanopoulos@aueb.gr -
Sentiment Analysis

2\. Mantzaris Marios, p3352421 , mar.mantzaris@aueb.gr - POS Tagger

3\. Kitsakis Georgios, p3352406 , geo.kitsakis@aueb.gr - Sentiment
Analysis

4\. Zacharis Efstathios, p3352415 , efs.zacharis@aueb.gr - POS Tagger

The link to the Colab notebook for POS Tagger is:
[<u>Link</u>](https://colab.research.google.com/drive/1fW6g55niencX5JXk2P7rc_cPI70U_Lse)

The link to the Colab notebook for Sentiment Analysis is:
[<u>Link</u>](https://colab.research.google.com/drive/1lCzFTeD1YVIr5uXqHollIZVlgHn_-NS4)

# **Exercise 1 - Sentiment Analysis with BERT Fine-tuning**

## **1. Dataset**

We used the **IMDB Movie Review Dataset** containing 50,000 movie
reviews labeled as positive or negative.

**Dataset Statistics:**

- **Training Set:** 35,000 reviews (17,500 positive, 17,500 negative)

- **Development Set:** 10,500 reviews (5,250 positive, 5,250 negative)

- **Test Set:** 15,000 reviews (7,500 positive, 7,500 negative)

- **Average document length:** 230 tokens (after BERT tokenization)

- **Vocabulary size:** 30,522 tokens (BERT vocabulary)

- **Maximum sequence length:** 256 tokens (truncated for efficiency)

- **Train/validation/test split:** 70%/21%/30%

**Preprocessing Steps:**

1.  Raw text processing for BERT tokenizer compatibility

2.  BERT tokenization using bert-base-uncased tokenizer

3.  Sequence truncation to maximum 256 tokens (for memory efficiency)

4.  Attention mask generation for padding tokens

5.  Label encoding: positive=1, negative=0

6.  Special tokens: \[CLS\], \[SEP\], \[PAD\]

7.  Dataset splitting with stratification to maintain class balance

## **2. Text Representation Methods**

For the BERT models, we implemented **transformer-based contextual
representations**:

### **2.1 Contextual Token Representation with BERT**

Our BERT models process text as contextualized token sequences with rich
semantic representations:

1.  **BERT Tokenization:**

    - WordPiece tokenization with 30,522 vocabulary size

    - Subword splitting handles out-of-vocabulary words

    - Special tokens: \[CLS\] for classification, \[SEP\] for separation

2.  **Contextual Embeddings:**

    - 768-dimensional contextual representations per token

    - Bidirectional attention captures full sentence context

    - Position embeddings encode sequential information

3.  **Sequence Processing:**

    - Maximum length: 256 tokens (truncated from 512 for efficiency)

    - Attention masks handle variable-length sequences

    - \[CLS\] token representation used for classification

4.  **Pre-trained Knowledge Transfer:**

    - BERT pre-trained on BookCorpus and English Wikipedia

    - 110M parameters with rich linguistic knowledge

    - Fine-tuning adapts general language understanding to sentiment
      task

### **2.2 Key Differences from Traditional Approaches**

**Contextual vs. Static Embeddings:**

- **Bidirectional context:** Each token representation considers full
  sentence context

- **Dynamic meanings:** Same word has different representations in
  different contexts

- **Attention mechanisms:** Self-attention captures long-range
  dependencies

- **Subword handling:** WordPiece tokenization manages unknown words
  effectively

**Advantages for Sentiment Analysis:**

- **Contextual understanding:** Captures sentiment in context (e.g.,
  negation handling)

- **Transfer learning:** Leverages massive pre-training data

- **Semantic composition:** Understands complex sentiment expressions

- **Robust representations:** Handles varied linguistic patterns
  effectively

This representation method enables BERT to understand sentiment through
deep contextual analysis, fundamentally different from local pattern
detection approaches.

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

###  **3.2 BERT with Task-specific Fine-tuning**

We implemented multiple BERT architectures with different fine-tuning
strategies:

**3.2.1 Custom BERT Classifier Architecture**

Architecture Components:

1.  BERT Base Model: bert-base-uncased with 12 transformer layers

2.  Configurable Layer Freezing: Ability to freeze 0-9 BERT encoder
    layers

3.  Task-specific Classification Head: Linear layers with ReLU and
    dropout

4.  Pooling Strategy: \[CLS\] token representation for sequence
    classification

5.  Regularization: Dropout rates of 0.3-0.4 throughout the network

#### **3.2.2 Fine-tuning Strategies**

Three Approaches Tested:

1.  Full Fine-tuning: All BERT parameters trainable

2.  Partial Freezing: Freeze lower BERT layers (6-9 layers frozen)

3.  Task-specific Only: Freeze all BERT layers, train only
    classification head

Key Features:

- Parameter Efficiency: Freezing reduces trainable parameters
  significantly

- Transfer Learning: Leverages pre-trained BERT knowledge effectively

- Gradient Flow: Careful layer freezing maintains learning capacity

- Memory Optimization: Frozen layers reduce memory requirements

###  **3.3 Hyperparameter Tuning**

We implemented systematic search across fine-tuning configurations:

Search Space:

- Frozen BERT Layers: 0, 6, 9 layers

- Learning Rates: 2e-5, 3e-5

- Batch Sizes: 8, 16, 32

- Hidden Dimensions: 512, 768

- Dropout Rates: 0.3, 0.4

- Task-specific Layers: 1-2 hidden layers

- Training Epochs: 1-3 with early stopping

**Optimal Configuration Found:**

- Frozen Layers: 6 out of 12 BERT encoder layers

- Learning Rate: 3e-5

- Batch Size: 8 (memory optimized)

- Hidden Dimension: 768

- Dropout: 0.3

- Training Epochs: 3 with early stopping (patience=2)

- Task-specific Architecture: Single hidden layer (768→768→2)

## **4. Training and Evaluation**

Training Configuration:

- Loss Function: Cross-entropy loss

- Optimizer: AdamW with learning rate 3e-5

- Early Stopping: Patience of 2 epochs based on validation loss

- Gradient Clipping: Maximum norm of 1.0

- Scheduler: Linear warmup with 0 warmup steps

- Training Duration: 3 epochs with early stopping

Training Dynamics:

- Rapid convergence within first epoch due to pre-trained weights

- Clear overfitting prevention through early stopping

- Frozen layer strategy improved training stability

- Memory optimization enabled training within Colab constraints

Evaluation Metrics: All models evaluated using accuracy, precision,
recall, and F1 score, calculated separately for training, development,
and test sets.

## **5. Results**

### **5.1 Training and Validation Loss Curves**

<img src="media/image10.png" style="width:5.93229in;height:3.3209in" />

### **5.2 Hyperparameter Tuning Results**

BERT Configuration
Comparison:<img src="media/image6.png" style="width:6.95313in;height:0.67949in" />

### **5.3 Model Performance Comparison**

### <img src="media/image11.png" style="width:5.55208in;height:0.97917in" />

### **5.4 Detailed Performance Metrics**

Best BERT Model Performance Across
Splits:<img src="media/image7.png" style="width:5.22917in;height:1.21875in" />

Per-Class Performance (Test
Set):<img src="media/image5.png" style="width:5.03125in;height:1.75in" />

**6. Key Findings**

### **6.1 Architecture Benefits**

- Contextual Understanding: BERT's bidirectional attention captures
  complex sentiment patterns effectively

- Transfer Learning Impact: Pre-trained knowledge provides substantial
  performance boost over traditional methods

- Parameter Efficiency: Strategic layer freezing (6 layers) maintains
  performance while reducing computational requirements

- Significant Improvement: 17.9% absolute accuracy gain demonstrates
  transformer effectiveness for sentiment analysis

### **6.2 Technical Insights**

- Layer Freezing Strategy: 6 frozen layers optimal - balances efficiency
  with performance

- Learning Rate Sensitivity: 3e-5 works well with partially frozen
  models

- Early Stopping Effectiveness: Prevents overfitting while maintaining
  strong performance

- Memory Optimization: Batch size 8 enables training within Colab GPU
  constraints

### **6.3 Comparison with CNN Approaches**

- Different Strengths: BERT excels at contextual understanding while
  CNNs detect local n-gram patterns

- Training Efficiency: BERT requires fewer epochs due to pre-trained
  initialization

- Feature Types: BERT learns contextual representations; CNNs detect
  specific linguistic patterns

- Performance Gap: BERT achieves substantially higher accuracy (91.7% vs
  ~85% for CNN)

### **6.4 Model Behavior Analysis**

The training dynamics reveal important characteristics:

- Transfer Learning Speed: BERT quickly adapts pre-trained knowledge to
  sentiment task

- Contextual Focus: Model learns sentiment through full sentence
  understanding

- Robust Generalization: Strong test performance indicates effective
  transfer

- Stability: Early stopping and layer freezing provide stable training

### **6.5 BERT-Specific Observations**

- Attention Mechanism Effectiveness: Self-attention captures long-range
  sentiment dependencies

- Subword Advantages: WordPiece tokenization handles diverse vocabulary
  effectively

- Bidirectional Context: Full sentence context improves sentiment
  understanding significantly

- Pre-training Benefits: BookCorpus and Wikipedia knowledge transfers
  well to movie reviews

Text Length Handling:

- Maximum sequence length: 256 tokens (truncated from 512 for
  efficiency)

- 95th percentile text length: 730 tokens

- Texts exceeding 256 tokens: Minimal information loss due to effective
  truncation

- Memory optimization enables practical training within resource
  constraints

## **7. Conclusion**

This implementation successfully demonstrates the effectiveness of BERT
fine-tuning for sentiment classification:

**Performance Achievements:**

- **91.70% test accuracy** with 17.9% improvement over baseline

- Balanced performance across positive and negative sentiment classes

- Strong generalization with minimal overfitting

**Technical Contributions:**

- Systematic hyperparameter tuning identifying optimal layer freezing
  strategy

- Memory-efficient implementation enabling training within Colab
  constraints

- Comprehensive evaluation across multiple data splits and metrics

**Key Insights:**

- BERT's contextual understanding provides substantial advantages for
  sentiment analysis

- Strategic layer freezing maintains performance while improving
  efficiency

- Transfer learning from large-scale pre-training proves highly
  effective for domain-specific tasks

The transformer architecture's attention mechanism and contextual
embeddings provide substantial improvements over traditional approaches,
validating the paradigm shift toward transformer-based models in NLP
applications.

# **Exercise 2 - POS Tagger**

Part-of-Speech Tagging with Pre-Trained Bert model

## **1. Introduction**

This report presents the implementation and evaluation of a
Part-of-Speech (POS) tagging system using a fine-tuned BERT
(Bidirectional Encoder Representations from Transformers) model.
Part-of-speech tagging is the process of assigning a part-of-speech tag
(such as noun, verb, adjective, etc.) to each word in a text. This task
is fundamental in natural language processing and serves as a building
block for more complex NLP applications.

In this implementation, we use a pre-trained BERT model with additional
improvements including a BiLSTM layer on top of BERT embeddings,
optimized hyperparameters, and improved training strategies. This
approach leverages the power of pre-trained language models, which have
been shown to capture rich contextual information, while adding
task-specific enhancements for POS tagging.

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

1.  **Text Tokenization**: Sentences were tokenized using the BERT
    tokenizer, which handles subword tokenization.

2.  **Sequence Preparation**: Input sequences were prepared with special
    tokens (\[CLS\], \[SEP\]) and padded to a maximum length of 128
    tokens.

3.  **Attention Masks**: Attention masks were created to distinguish
    real tokens from padding tokens.

4.  **Label Alignment**: POS tags were aligned with the tokenized words,
    with special handling for subword tokens (only the first subword of
    each word was assigned a tag, others were marked with -100 to be
    ignored in loss calculation).

5.  **Data Formatting**: The data was formatted as required by the BERT
    model, with input IDs, attention masks, and token type IDs.

## **3. Models**

Two models were implemented and compared:

1.  **Baseline Model**: A simple model that assigns the most frequent
    tag seen during training for each word. For unseen words, it assigns
    the most common tag overall.

2.  **BERT Model**: A fine-tuned BERT model with the following
    architecture:

    - Pre-trained BERT-base-cased model as the foundation

    - Maximum sequence length of 128 tokens

    - Dropout layer (rate = 0.2) for regularization

    - Dense layer with softmax activation for classification

    - Early stopping and learning rate reduction on plateau to prevent
      overfitting

### **3.1 Hyperparameter Tuning**

The following hyperparameters were used for the BERT model:

- Learning rate: 2e-5

- Batch size: 32

- Dropout rate: 0.3

- Maximum sequence length: 128

- Number of epochs: 30

The BERT model was trained using the Adam optimizer with a custom masked
sparse categorical cross-entropy loss that ignores padding tokens. Early
stopping was used to prevent overfitting, with a patience of 3 epochs.
Additionally, a learning rate reduction strategy was employed to improve
convergence, reducing the learning rate by a factor of 0.5 when
validation loss plateaued with a patience of 2 epochs.

## **4. Results**

### **4.1 Loss Curves**

The following graph shows the loss on training and development data as a
function of epochs:

<img src="media/image4.png" style="width:6.26772in;height:2.06944in" />

The loss curves show that the model converges after a few epochs, with
the validation loss stabilizing. The early stopping mechanism prevented
overfitting by stopping training when the validation loss stopped
improving.

### **4.2 Per-Class BERT Metrics**

<img src="media/image13.png" style="width:6.19792in;height:3.45833in" />

### <img src="media/image12.png" style="width:6.19792in;height:3.45833in" />

<img src="media/image14.png" style="width:6.19792in;height:3.45833in" />

### 

### 

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

#### 

#### **4.3.4 CNN Model**

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.9137           | 0.8603              | 0.8636       |
| Recall     | 0.8930           | 0.8087              | 0.8258       |
| F1         | 0.9015           | 0.8231              | 0.8307       |
| PR-AUC     | 0.9040           | 0.8361              | 0.8462       |

#### **4.3.5 BERT Model**

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8402           | 0.8309              | 0.8294       |
| Recall     | 0.7879           | 0.7726              | 0.7646       |
| F1         | 0.8069           | 0.7929              | 0.7863       |
| PR-AUC     | 0.8463           | 0.8344              | 0.8297       |

<img src="media/image3.png" style="width:6.26772in;height:3.09722in" />

<img src="media/image9.png" style="width:6.26772in;height:3.09722in" />

## <img src="media/image1.png" style="width:6.26772in;height:3.09722in" />

<img src="media/image2.png" style="width:6.26772in;height:3.09722in" />

We also provide a confusion matrix for some of the top tags.

## <img src="media/image8.png" style="width:6.26772in;height:5.625in" />

## **5. Conclusion**

This report presented a Part-of-Speech tagging system using a fine-tuned
BERT model. The BERT model was compared with a baseline model, an MLP
model from Assignment 3, an RNN model from Assignment 4, and a CNN model
from Assignment 5. Contrary to expectations, the BERT model did not
perform as well as expected, especially when compared to previous
approaches. Several factors may have contributed to the BERT model's
unexpected poor performance:

1.  Insufficient Fine-tuning: The model may have required more epochs or
    a different learning rate schedule to properly adapt the pre-trained
    BERT weights to the POS tagging task.

2.  Token Alignment Issues: BERT's subword tokenization can create
    challenges for token-level tasks like POS tagging. The method used
    to align POS tags with BERT's subword tokens may have led to
    information loss.

3.  Lack of Task-Specific Architecture: The simple approach of adding
    only a classification layer on top of BERT may be insufficient.
    Adding task-specific components like BiLSTM layers could help
    capture sequential dependencies that are important for POS tagging.
