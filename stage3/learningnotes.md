# ML Learning Notes
Date: May 2024
Author: Titi KH

## I. Vectorization
**Definition:** it broadly defined the process of converting non-numeric data into numeric format so we can apply ML algorithms later on.

The data does not have to be in text, it can be multimodel. For the sake of this project, we will discuss text data only.

## II. Embeddings
**Definition:** embeddings are data that have been transformed into n-dimensional matricies for use in deep learning computations.

Embeddings are more sophisticated vectorization. Embeddings are representations that preserve semantic meaning. Embeddings can represent words, phrases, or even the entire document.

### Primary Methods of Vectorization
1. **[BASIC-1]Bag of Words** (count vectorization):
e.g. Chop each word into its original format, give them 1. Ignore grammar, weight, semantic meaning.
Article 1: I used to study at MSU in East Lansing, MI.
Article 1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Article 2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
Article 3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
**Most importantly**: BoW measures measures the frequency of each word in the document.

2. **[BASIC2]TF-IDF** Vectorization(Term-Frequency-Inverse Document Frequency)
**TF** T=term D=one specific document: if I see MSU once, in a sentence/document that has 10 words, then TF=1/10.
**DF** D=Document F=Frequency: here we are talking about the number of documents that contain this term. It does not matter how many times this term was used, ONLY **the count of the documents**. df(apple)=1(MSU only appeared once across all documents)
**IDF** =log(N/df): logarithm helps in scaling down numbers. e.g. N=3, df=1, IDF('MSU')=log(3/1)=0.477.

*Adjusting IDF calculation* this is something I found interesting and is a good learning moment! There are different ways of adjusting this:
- incrementing denominator: IDF(term)=log(10/0+1)=log(10)
(Use this one when the dataset is static, don't change much.)
- adding 1 to the result:
IDF(term)= log(10/0)+1
additional check needed.
(Use this if data is dynamic)

**!** So the goal is to avoid having 0 in the equation but if a term is not even in the documents (which is how there might be a 0 in the equation), why do we care?
- **corpus of documents can change**
- **when using pre-trained models** and we are applying these models to different datasets.

3. **[BASIC-3]One-Hot Encoding**

4. **[BASIC-4]N-gram**
This extends BoW, it is useful when word order impacts meaning.
Google's famous Ngram Viewer: https://books.google.com/ngrams/

5. **[ADVANCED/also known as Word Embeddings-1] Word2Vec**
Developed by Google.
It is a neural network-based model that learns word associations from a large corpus of text.

6. **[ADVANCED-2] GloVe**


7. **[ADVANCED-3] FastText**

8. **[ADVANCED-CONTEXTUAL Embeddings/MODELS-1] BERT**:
Bidirectional Encoder Representations from Transformers
Generates embeddings that consider the full context of a word (both left and right contexts).
Useful for tasks requiring a deep understanding of word meaning based on surrounding text.

9. **[ADVANCED-CONTEXTUAL Embeddings/MODELS-2] GPT**:
Generative Pre-trained Transformer
Focuses on predicting the next word in a sequence, useful for text generation.

10. **[ADVANCED-CONTEXTUAL Embeddings/MODELS-3] Transformer Variants**:
- e.g., RoBERTa, T5, DistilBERT


**SUMMARY**:
- I think I am getting somewhere--> spaCy's language models did *word embeddings* but not *document embeddings*. For instance, 'en_core_web_lg' are static and it uses item 6 'GloVe'. Each instance of a word maps to the same pre-trained vector regardless of its surrounding text. So it's useful for overall meaning of words, but not contextual nuances.
'en_core_web_lg' specifically uses GloVe vectors that have been pre-trained on a large corpus of text from the Common Crawl dataset. 
- It does not differentiate meanings of one word if it spells the same, e.g. bank: a. financial institute or b. bank of a river
- It runs quickly, no need to involve GPU.
*However*
- If we want to build dynamic model, we have to go with more advanced embeddings models like transformer models, e.g. BERT, mBERT.
- ***BUT***, spaCy also level up its game and now we can use transformers: READ THIS: https://spacy.io/usage/embeddings-transformers

## III. Large Language Models
**Definition**: Advanced models built on the principles of contextual embeddings but at a much larger scale. They are trained on vast amounts of text and can understand and generate human-like text.

Starting with basic embeddings, move to contextual models that provide embeddings sensitive to textual context, and reach LLMs, which use these principles but at a scale and versatility that allows them to perform comprehensive language tasks.

- BERT: both an embedding model and a LLM:
As an embedding model, BERT’s role is to provide vector representations of text data that capture the complexity and variability of language in context.
As a Large Language Model, BERT’s role extends to directly solving language-related tasks, leveraging its pre-trained capabilities and fine-tuning them to specific requirements.

## IV. Transformer Architecture
- Transformer creates what are known as contextual embeddings, where the representation of each word is influenced by every other word in the sentence.
- Transformer is the backbone of many LLMs, e.g. BERT, GPT, RoBERTA.
[More readings need to be done here for transformers]
- Check out that super famous paper: "Attention is All You Need" by Vaswani et al. in 2017

## V. Applications
I personally think we will benefit a lot from learning and testing spacyllm: https://github.com/explosion/spacy-llm
1. a. Cosine Similarity Computing: https://www.datatechnotes.com/2023/10/cosine-similarity-computing-example_24.html
b. Word Vectors and Similarity: https://www.machinelearningplus.com/spacy-tutorial-nlp/#wordvectorsandsimilarity
**Promising way** At this point, it seems like cosine similarity is something we need to do if we want to improve search or offer better recommendations.
2. Topic Modeling: most topic modeling project stoped once they get the modeling results. So I don't really know how we can build on top of tm results. https://medium.com/nlplanet/text-analysis-topic-modelling-with-spacy-gensim-4cd92ef06e06#3363
3. Sentiment Analysis with Textblob: https://pythonology.eu/text-analysis-in-python-spacy-and-textblob/#sentiment-analysis-with-textblob I personally think this is too shallow.
4. Text Classificiation: https://towardsdatascience.com/machine-learning-for-text-classification-using-spacy-in-python-b276b4051a49
