# NLP Laboratory Experiments

A collection of Natural Language Processing experiments conducted during my college studies. This repository contains practical implementations of various NLP techniques and concepts.

## Table of Contents

1. [Introduction](#introduction)
2. [Experiments](#experiments)
   - [Experiment 1: Text Preprocessing](#experiment-1-text-preprocessing)
   - [Experiment 2: Tokenization](#experiment-2-tokenization)
   - [Experiment 3: Part-of-Speech Tagging](#experiment-3-part-of-speech-tagging)
   - [Experiment 4: Named Entity Recognition](#experiment-4-named-entity-recognition)
   - [Experiment 5: Sentiment Analysis](#experiment-5-sentiment-analysis)
   - [Experiment 6: Text Classification](#experiment-6-text-classification)
   - [Experiment 7: Word Embeddings](#experiment-7-word-embeddings)
   - [Experiment 8: Topic Modeling](#experiment-8-topic-modeling)
   - [Experiment 9: Text Summarization](#experiment-9-text-summarization)
   - [Experiment 10: Machine Translation](#experiment-10-machine-translation)
   - [Experiment 11: Question Answering System](#experiment-11-question-answering-system)
   - [Experiment 12: Chatbot Implementation](#experiment-12-chatbot-implementation)
3. [Setup and Requirements](#setup-and-requirements)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

This repository contains a series of NLP experiments that demonstrate fundamental concepts and practical applications in Natural Language Processing. Each experiment focuses on a specific aspect of NLP, providing hands-on experience with various techniques and tools.

## Experiments

### Experiment 1: Text Preprocessing
- **Description**: Implementation of basic text preprocessing techniques including:
  - Lowercasing
  - Removing special characters
  - Handling whitespace
  - Basic text cleaning
- **Technologies**: Python, Regular Expressions
- **Directory**: `exp1/`

### Experiment 2: Tokenization
- **Description**: Implementation of different tokenization methods:
  - Word tokenization
  - Sentence tokenization
  - Custom tokenization rules
- **Technologies**: NLTK, spaCy
- **Directory**: `exp2/`

### Experiment 3: Part-of-Speech Tagging
- **Description**: Implementation of POS tagging using:
  - Rule-based approaches
  - Statistical models
  - Deep learning models
- **Technologies**: NLTK, spaCy
- **Directory**: `exp3/`

### Experiment 4: Named Entity Recognition
- **Description**: Building NER systems to identify:
  - Person names
  - Organization names
  - Locations
  - Dates
- **Technologies**: spaCy, BERT
- **Directory**: `exp4/`

### Experiment 5: Sentiment Analysis
- **Description**: Implementation of sentiment analysis using:
  - Traditional machine learning
  - Deep learning approaches
  - Pre-trained models
- **Technologies**: scikit-learn, TensorFlow
- **Directory**: `exp5/`

### Experiment 6: Text Classification
- **Description**: Building text classification models for:
  - Document categorization
  - Spam detection
  - Topic classification
- **Technologies**: scikit-learn, TensorFlow
- **Directory**: `exp6/`

### Experiment 7: Word Embeddings
- **Description**: Implementation and usage of:
  - Word2Vec
  - GloVe
  - FastText
- **Technologies**: Gensim, TensorFlow
- **Directory**: `exp7/`

### Experiment 8: Topic Modeling
- **Description**: Implementation of topic modeling using:
  - Latent Dirichlet Allocation (LDA)
  - Non-negative Matrix Factorization (NMF)
- **Technologies**: Gensim, scikit-learn
- **Directory**: `exp8/`

### Experiment 9: Text Summarization
- **Description**: Building text summarization systems:
  - Extractive summarization
  - Abstractive summarization
- **Technologies**: Transformers, Hugging Face
- **Directory**: `exp9/`

### Experiment 10: Machine Translation
- **Description**: Implementation of machine translation using:
  - Statistical machine translation
  - Neural machine translation
- **Technologies**: OpenNMT, Transformers
- **Directory**: `exp10/`

### Experiment 11: Question Answering System
- **Description**: Building a QA system using:
  - Information retrieval
  - Reading comprehension
  - Knowledge-based approaches
- **Technologies**: BERT, Transformers
- **Directory**: `exp11/`

### Experiment 12: Chatbot Implementation
- **Description**: Development of a chatbot with:
  - Rule-based responses
  - Machine learning-based responses
  - Integration with messaging platforms
- **Technologies**: Rasa, Dialogflow
- **Directory**: `exp12/`

## Setup and Requirements

Each experiment directory contains its own requirements.txt file with specific dependencies. Common requirements include:

- Python 3.7+
- NLTK
- spaCy
- scikit-learn
- TensorFlow/PyTorch
- Transformers
- Gensim

## Usage

1. Clone the repository:
```bash
git clone https://github.com/ahmedkurov/nlp-lab.git
cd nlp-lab
```

2. Navigate to the specific experiment directory:
```bash
cd exp<number>
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the experiment:
```bash
python main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details. 