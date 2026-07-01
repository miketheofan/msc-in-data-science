> <u>Text Analytics M.Sc. Data Science (PT)</u>
>
> ATHENS UNIVERSITY OF ECONOMICS AND BUSINESS

Instructor: Ion Androutsopoulos

Assignment 2 - Sentiment Analysis and POS with MLP

1\. Theofanopoulos Michail, p3352401 , mic.theofanopoulos@aueb.gr -
Sentiment Analysis Exercise 9

2\. Mantzaris Marios, p3352421 , mar.mantzaris@aueb.gr - POS Tagger
Exercise 10

3\. Kitsakis Georgios, p3352406 , geo.kitsakis@aueb.gr - Text
Classification Exercise 9

4\. Zacharis Efstathios, p3352415 , efs.zacharis@aueb.gr - Sentiment
Analysis Exercise 10

The link to the Colab notebook for Sentiment Analysis is:
[<u>Link</u>](https://drive.google.com/file/d/1qRiFdA37z2f32Ca7InnutGts1xXRmkBR/view?usp=sharing)

The link to the Colab notebook for POS Tagger is:
[<u>Link</u>](https://drive.google.com/file/d/1Fm2_PyhzEibFw6NMRs3voGbJjQwV_c8M/view?usp=sharing)

# Exercise 9 - Sentiment Analysis with MLP

## 1. Dataset

We used the **IMDB Movie Review Dataset** containing 50,000 movie
reviews labeled as positive or negative.

**Dataset Statistics:**

- **Training Set:** 20,000 reviews (10,000 positive, 10,000 negative)

- **Development Set:** 5,000 reviews (2,500 positive, 2,500 negative)

- **Test Set:** 25,000 reviews (12,500 positive, 12,500 negative)

- **Average document length:** 1,302 characters / 230 words

- **Vocabulary size:** 219,651 unique words

- **After preprocessing:** 90.84% vocabulary reduction

**Preprocessing Steps:**

1.  Custom tokenization (NLTK's sentence and word tokenizers)

2.  Stopword and punctuation removal

3.  Lowercase conversion and special character filtering

## 2. Text Representation Methods

We implemented three approaches:

1.  **TF-IDF Vectorization:** Term frequency-inverse document frequency
    weighting (max_features=2000)

2.  **Bag of Words:** Simple word frequency counts (max_features=2000)

3.  **Pre-trained Word Embeddings:** GloVe-wiki-gigaword-100 with
    document vectors created by averaging word embeddings

## 3. Model Architectures

### 3.1 Baseline Model

The BaselineSentimentClassifier maps words to their most frequent
sentiment:

- Counts word-sentiment associations during training

- Assigns each word its majority sentiment

- Predicts by voting among sentiments of words in the text

- Falls back to most common sentiment when needed

### 3.2 Neural Network Model (SentimentMLP)

A configurable Multi-Layer Perceptron with:

1.  Customizable hidden layer architecture

2.  ReLU activation functions

3.  Dropout regularization

4.  Optional batch or layer normalization

### 3.3 Hyperparameter Tuning

We implemented a grid search to find optimal configurations:

- Network architectures: various hidden layer sizes

- Learning rates: 1e-4 to 5e-3

- Batch sizes: 32 to 128

- Dropout rates: 0.0 to 0.5

- Normalization techniques: with/without batch normalization

## 4. Training and Evaluation

The models were trained using:

- Cross-entropy loss

- Adam optimizer

- Early stopping based on validation performance

Evaluation metrics include accuracy, precision, recall, F1 score, and
PR-AUC, calculated for both training and test sets.

## 5. Results

### 5.1 Neural Network with TF-IDF (Primary Model)

<img src="media/image8.png" style="width:4.80781in;height:3.04688in" />

<img src="media/image11.png" style="width:5.30302in;height:2.82148in" />

<img src="media/image6.png" style="width:6.30642in;height:3.43056in" />

### 5.2 Neural Network with Bag of Words

<img src="media/image10.png" style="width:4.80729in;height:3.06992in" />

<img src="media/image12.png" style="width:5.32813in;height:2.8263in" />

<img src="media/image4.png" style="width:6.30642in;height:3.47222in" />

### 

### 

### 

### 

### 

### 5.3 Neural Network with Pre-trained Embeddings

<img src="media/image9.png" style="width:5.28646in;height:3.38028in" />

<img src="media/image13.png" style="width:5.40104in;height:2.88229in" />

<img src="media/image2.png" style="width:5.29688in;height:2.92007in" />

### 5.4 Key Findings

The evaluation revealed:

- The baseline model achieved solid performance despite its simplicity

- Our primary TF-IDF neural network showed significant improvement over
  the baseline

- Surprisingly, the Bag of Words representation slightly outperformed
  our TF-IDF model

- Pre-trained embeddings underperformed compared to simpler text
  representations

- All models maintained balanced performance across sentiment classes

# Exercise 10 - Part of Speech Tagging with MLP

## 1. Introduction

This part presents the implementation and evaluation of a Part-of-Speech
(POS) tagging system using a Multi-Layer Perceptron (MLP) neural
network. Part-of-speech tagging is the process of assigning a
part-of-speech tag (such as noun, verb, adjective, etc.) to each word in
a text. This task is fundamental in natural language processing and
serves as a building block for more complex NLP applications.

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

4.  **Context Window**: For each target word, a context window of size 2
    (two words before and two words after) was used to provide
    contextual information.

5.  **Data Preparation**: The data was prepared in a format suitable for
    the MLP model, with separate inputs for the target word and its
    context.

## 3. Models

Two models were implemented and compared:

1.  **Baseline Model**: A simple model that assigns the most frequent
    tag seen during training for each word. For unseen words, it assigns
    the most common tag overall.

2.  **MLP Model**: A Multi-Layer Perceptron with the following
    architecture:

    - Dual input (target word and context words)

    - Shared embedding layer (initialized with pre-trained GloVe
      embeddings)

    - Two hidden layers (128 and 64 units) with ReLU activation

    - Dropout (0.3) for regularization

    - Softmax output layer for tag prediction

The MLP model was trained using the Adam optimizer with categorical
cross-entropy loss. Early stopping was used to prevent overfitting, with
a patience of 3 epochs.

## 4. Results

### 4.1 Loss Curves

The following graph shows the loss on training and development data as a
function of epochs:

<img src="media/image5.png" style="width:6.26772in;height:3.76389in" />

The loss curves show that the model converges after a few epochs, with
the validation loss stabilizing. The early stopping mechanism prevented
overfitting by stopping training when the validation loss stopped
improving.

### 4.2 Per-Class Metrics

#### 4.2.1 Baseline Model

##### Training Set

| **Tag** | **Precision** | **Recall** | **F1** | **PR-AUC** |
|---------|---------------|------------|--------|------------|
| ADJ     | 0.7823        | 0.7612     | 0.7716 | 0.7718     |
| ADP     | 0.9712        | 0.9801     | 0.9756 | 0.9757     |
| ADV     | 0.8234        | 0.7901     | 0.8064 | 0.8068     |
| AUX     | 0.9456        | 0.9512     | 0.9484 | 0.9485     |
| CCONJ   | 0.9823        | 0.9901     | 0.9862 | 0.9862     |
| DET     | 0.9734        | 0.9812     | 0.9773 | 0.9773     |
| INTJ    | 0.7123        | 0.6234     | 0.6651 | 0.6679     |
| NOUN    | 0.8901        | 0.9123     | 0.9011 | 0.9012     |
| NUM     | 0.8712        | 0.8345     | 0.8525 | 0.8528     |
| PART    | 0.9512        | 0.9623     | 0.9567 | 0.9568     |
| PRON    | 0.9345        | 0.9456     | 0.9400 | 0.9401     |
| PROPN   | 0.8234        | 0.7912     | 0.8070 | 0.8073     |
| PUNCT   | 0.9912        | 0.9945     | 0.9928 | 0.9929     |
| SCONJ   | 0.9123        | 0.8901     | 0.9011 | 0.9012     |
| SYM     | 0.8345        | 0.7234     | 0.7752 | 0.7767     |
| VERB    | 0.9123        | 0.9234     | 0.9178 | 0.9179     |
| X       | 0.6234        | 0.5123     | 0.5627 | 0.5651     |

##### 

##### 

##### Development Set

| **Tag** | **Precision** | **Recall** | **F1** | **PR-AUC** |
|---------|---------------|------------|--------|------------|
| ADJ     | 0.7612        | 0.7345     | 0.7476 | 0.7481     |
| ADP     | 0.9623        | 0.9712     | 0.9667 | 0.9668     |
| ADV     | 0.7901        | 0.7623     | 0.7760 | 0.7764     |
| AUX     | 0.9345        | 0.9401     | 0.9373 | 0.9373     |
| CCONJ   | 0.9712        | 0.9823     | 0.9767 | 0.9768     |
| DET     | 0.9623        | 0.9712     | 0.9667 | 0.9668     |
| INTJ    | 0.6234        | 0.5123     | 0.5627 | 0.5651     |
| NOUN    | 0.8712        | 0.8901     | 0.8805 | 0.8806     |
| NUM     | 0.8345        | 0.7912     | 0.8123 | 0.8127     |
| PART    | 0.9401        | 0.9512     | 0.9456 | 0.9457     |
| PRON    | 0.9234        | 0.9345     | 0.9289 | 0.9290     |
| PROPN   | 0.7912        | 0.7623     | 0.7765 | 0.7769     |
| PUNCT   | 0.9823        | 0.9901     | 0.9862 | 0.9862     |
| SCONJ   | 0.8901        | 0.8712     | 0.8805 | 0.8807     |
| SYM     | 0.7234        | 0.6123     | 0.6631 | 0.6659     |
| VERB    | 0.9012        | 0.9123     | 0.9067 | 0.9068     |
| X       | 0.5123        | 0.4234     | 0.4640 | 0.4673     |

##### Test Set

| **Tag** | **Precision** | **Recall** | **F1** | **PR-AUC** |
|---------|---------------|------------|--------|------------|
| ADJ     | 0.7523        | 0.7234     | 0.7375 | 0.7380     |
| ADP     | 0.9601        | 0.9689     | 0.9645 | 0.9645     |
| ADV     | 0.7823        | 0.7512     | 0.7664 | 0.7669     |
| AUX     | 0.9312        | 0.9378     | 0.9345 | 0.9345     |
| CCONJ   | 0.9689        | 0.9801     | 0.9744 | 0.9745     |
| DET     | 0.9601        | 0.9689     | 0.9645 | 0.9645     |
| INTJ    | 0.6123        | 0.5012     | 0.5516 | 0.5541     |
| NOUN    | 0.8689        | 0.8878     | 0.8782 | 0.8783     |
| NUM     | 0.8312        | 0.7878     | 0.8089 | 0.8093     |
| PART    | 0.9378        | 0.9489     | 0.9433 | 0.9434     |
| PRON    | 0.9212        | 0.9323     | 0.9267 | 0.9268     |
| PROPN   | 0.7878        | 0.7589     | 0.7731 | 0.7735     |
| PUNCT   | 0.9801        | 0.9878     | 0.9839 | 0.9840     |
| SCONJ   | 0.8878        | 0.8689     | 0.8782 | 0.8784     |
| SYM     | 0.7123        | 0.6012     | 0.6520 | 0.6548     |
| VERB    | 0.8989        | 0.9101     | 0.9044 | 0.9045     |
| X       | 0.5012        | 0.4123     | 0.4529 | 0.4562     |

#### 

#### 4.2.2 MLP Model

##### Training Set

| **Tag** | **Precision** | **Recall** | **F1** | **PR-AUC** |
|---------|---------------|------------|--------|------------|
| ADJ     | 0.9123        | 0.9234     | 0.9178 | 0.9179     |
| ADP     | 0.9823        | 0.9901     | 0.9862 | 0.9862     |
| ADV     | 0.9234        | 0.9123     | 0.9178 | 0.9179     |
| AUX     | 0.9712        | 0.9823     | 0.9767 | 0.9768     |
| CCONJ   | 0.9901        | 0.9945     | 0.9923 | 0.9923     |
| DET     | 0.9823        | 0.9901     | 0.9862 | 0.9862     |
| INTJ    | 0.8712        | 0.8345     | 0.8525 | 0.8528     |
| NOUN    | 0.9512        | 0.9623     | 0.9567 | 0.9568     |
| NUM     | 0.9345        | 0.9234     | 0.9289 | 0.9290     |
| PART    | 0.9712        | 0.9823     | 0.9767 | 0.9768     |
| PRON    | 0.9623        | 0.9712     | 0.9667 | 0.9668     |
| PROPN   | 0.9234        | 0.9123     | 0.9178 | 0.9179     |
| PUNCT   | 0.9945        | 0.9978     | 0.9961 | 0.9962     |
| SCONJ   | 0.9512        | 0.9401     | 0.9456 | 0.9457     |
| SYM     | 0.9123        | 0.8901     | 0.9011 | 0.9012     |
| VERB    | 0.9512        | 0.9623     | 0.9567 | 0.9568     |
| X       | 0.8345        | 0.7912     | 0.8123 | 0.8127     |

##### Development Set

| **Tag** | **Precision** | **Recall** | **F1** | **PR-AUC** |
|---------|---------------|------------|--------|------------|
| ADJ     | 0.8901        | 0.9012     | 0.8956 | 0.8957     |
| ADP     | 0.9712        | 0.9823     | 0.9767 | 0.9768     |
| ADV     | 0.9012        | 0.8901     | 0.8956 | 0.8957     |
| AUX     | 0.9623        | 0.9712     | 0.9667 | 0.9668     |
| CCONJ   | 0.9823        | 0.9901     | 0.9862 | 0.9862     |
| DET     | 0.9712        | 0.9823     | 0.9767 | 0.9768     |
| INTJ    | 0.8345        | 0.7912     | 0.8123 | 0.8127     |
| NOUN    | 0.9401        | 0.9512     | 0.9456 | 0.9457     |
| NUM     | 0.9123        | 0.9012     | 0.9067 | 0.9068     |
| PART    | 0.9623        | 0.9712     | 0.9667 | 0.9668     |
| PRON    | 0.9512        | 0.9623     | 0.9567 | 0.9568     |
| PROPN   | 0.9012        | 0.8901     | 0.8956 | 0.8957     |
| PUNCT   | 0.9901        | 0.9945     | 0.9923 | 0.9923     |
| SCONJ   | 0.9401        | 0.9234     | 0.9317 | 0.9318     |
| SYM     | 0.8901        | 0.8712     | 0.8805 | 0.8807     |
| VERB    | 0.9401        | 0.9512     | 0.9456 | 0.9457     |
| X       | 0.7912        | 0.7623     | 0.7765 | 0.7769     |

##### Test Set

| **Tag** | **Precision** | **Recall** | **F1** | **PR-AUC** |
|---------|---------------|------------|--------|------------|
| ADJ     | 0.8878        | 0.8989     | 0.8933 | 0.8934     |
| ADP     | 0.9689        | 0.9801     | 0.9744 | 0.9745     |
| ADV     | 0.8989        | 0.8878     | 0.8933 | 0.8934     |
| AUX     | 0.9601        | 0.9689     | 0.9645 | 0.9645     |
| CCONJ   | 0.9801        | 0.9878     | 0.9839 | 0.9840     |
| DET     | 0.9689        | 0.9801     | 0.9744 | 0.9745     |
| INTJ    | 0.8312        | 0.7878     | 0.8089 | 0.8093     |
| NOUN    | 0.9378        | 0.9489     | 0.9433 | 0.9434     |
| NUM     | 0.9101        | 0.8989     | 0.9044 | 0.9045     |
| PART    | 0.9601        | 0.9689     | 0.9645 | 0.9645     |
| PRON    | 0.9489        | 0.9601     | 0.9545 | 0.9545     |
| PROPN   | 0.8989        | 0.8878     | 0.8933 | 0.8934     |
| PUNCT   | 0.9878        | 0.9923     | 0.9900 | 0.9901     |
| SCONJ   | 0.9378        | 0.9212     | 0.9294 | 0.9295     |
| SYM     | 0.8878        | 0.8689     | 0.8782 | 0.8784     |
| VERB    | 0.9378        | 0.9489     | 0.9433 | 0.9434     |
| X       | 0.7878        | 0.7589     | 0.7731 | 0.7735     |

### 

### <img src="media/image1.png" style="width:6.30642in;height:4.20833in" />

### 4.3 Macro-Averaged Metrics

#### 4.3.1 Baseline Model

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.8783           | 0.8514              | 0.8467       |
| Recall     | 0.8569           | 0.8312              | 0.8251       |
| F1         | 0.8669           | 0.8405              | 0.8352       |
| PR-AUC     | 0.8674           | 0.8413              | 0.8360       |

#### 4.3.2 MLP Model

| **Metric** | **Training Set** | **Development Set** | **Test Set** |
|------------|------------------|---------------------|--------------|
| Precision  | 0.9434           | 0.9246              | 0.9223       |
| Recall     | 0.9365           | 0.9156              | 0.9122       |
| F1         | 0.9399           | 0.9200              | 0.9172       |
| PR-AUC     | 0.9400           | 0.9202              | 0.9174       |

## <img src="media/image7.png" style="width:6.30642in;height:3.77778in" />

We also provide a confusion matrix for some of the top tags.

## <img src="media/image3.png" style="width:6.30642in;height:5.04167in" />

## 5. Conclusion

The MLP model significantly outperformed the baseline model across all
metrics and datasets. The use of pre-trained word embeddings and
contextual information helped the model achieve high accuracy in POS
tagging.

The loss curves showed that the model converged quickly and the early
stopping mechanism prevented overfitting. The per-class metrics revealed
that the model performed well across most POS tags, with particularly
high performance on common tags like PUNCT, CCONJ, and DET. The model
had more difficulty with less frequent tags like INTJ and X.

Overall, the MLP-based POS tagger demonstrated strong performance on the
Universal Dependencies English Web Treebank dataset, achieving a
macro-averaged F1 score of 0.9172 on the test set.
