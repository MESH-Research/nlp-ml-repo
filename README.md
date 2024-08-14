# nlp-ml-repo
## Introduction
This repository contains tutorials, materials for testing purposes, and other documents relating to natural language processing and machine learning for the Knowledge Commons. Author Tianyi (Titi) Kou-Herrema is a German Studies PhD candidate who has a deep interest in applying computational methods to assist scholarly work. She is hired as a research assistant for the Knowledge Commons Project from Summer 2023 to Fall 2024 where she develops this project while primarily working with Ian Scott and Stephanie Vasko (with much support from the rest of the tech team including Mike Thicke, Cassie Lem, Dimitrios Tzouris, and Bonnie Russell).

This project comes in different **stages** and each stage contains various steps. The overall workflow follows the sequence: "data acquisition - data extraction - data preprocessing - subset training - evaluation - implementation." The three end goals are: improving search functionality; offering related record recommendations; and implementing subject tagging.

Another goal of this project is to demonstrate that, despite the use of computational methods to handle large quantities of textual data, human decisions were made at almost every step, many of which were based on my experience and knowledge. A common misconception is that we can feed data into a black box, and magic simply happens, producing beautiful and meaningful output on the other end. However, this is not the case. Developers and researchers make decisions based on their best judgment, learning and improving along the way. In hindsight, some of the steps taken early on may seem naive, but as a researcher, I was working with the knowledge I had at the time, which documents the process of acquiring expertise.

## Stage 1: 2023 Fall/Winter

### Step 1: Familiarizing Myself with the Basics
- InvenioRDM: Read InvenioRDM [documentations](https://inveniordm.docs.cern.ch/)
- Using API to access files and stats: [Postman](https://www.postman.com/) & [Rest API](https://inveniordm.docs.cern.ch/reference/rest_api_index/)
- Docker environments

### Step 2: Setting goals
- Short-term goals: testing .py libraries for extracting text from different types of deposited files
- Long-term goals: clean files and build (a) structured data frame(s); perform topic modeling or other analysis on the data at hand
  
#### Deliverables:
1. The script for text extraction comparison using different Python libraries on various file types: "stage1/tutorial1-textout.md"
2. Materials for test purposes are stored in the folder "text4test"

*During this process, I also used the Miro Board to guide my steps and drew workflow to explain this process to colleagues.*

## Stage 2: 2024 Spring
*You can also find detailed explanation in "guide.md" in folder "stage2"*

### Step 1: Accessing Data
Accessing and downloading files from the Invenio API, and extracting text data from all downloaded files. Since the files come in various formats (e.g., PDF, Word, JPG, MP3), I developed a strategy to extract text based on each format. To save local storage space, files that are successfully processed are deleted afterward.

#### Deliverable:
1. Script "apiinvenio-9th.py"
2. CSV file "output9clean.csv" (for data security stored elsewhere)

### Step 2: Quality Check of Output
Examine the csv file from the previous step, get a general ideas about what the data structure looks like, checking for missing value, checking files that can not be processed.
***Invenio set a hardcore limit of 10k, this will be addressed later on.***

#### Deliverable:
1. Markdown file "stage2/examine-output9.md"

### Step 3: Data Preprocessing
After comparing NLTK and SpaCy for data preprocessing, I decided to use SpaCy for initial cleaning because it’s lighter, more up-to-date, and has a manageable learning curve. The goal of this step is to produce a clean, processed CSV for future use. Some files contain over 3 million tokens, so I developed strategies to process them in chunks to avoid out-of-memory (OOM) errors.

#### Deliverable:
1. Script "csv-preprocessing2.py"
2. CSV file "processed_output.csv" (for data security stored elsewhere)

## Stage 3: 2024 Summer/Fall
As I wrapped up with the previous stage, I received a clean and processed CSV file. This stage is mainly about applying vectorization to the preprocessed output so I can further develop applications on this data. Embedding/Vectorization itself is a complicated field and I have done some learning. Notes can be found in deliverables.

### Step 1: Examine the Preprocessed Output & Vectorization Learning
Always examining and evaluating data acquired from the previous step is a good practice.
At the same time, I studied embeddings and vectorization from a theoretical level so I understand what happens behind the scene to avoid applying tools to data without comprehension. I have considered to continue work with SpaCy in this stage. However, after learning about SpaCy's functions and limitations, I decided to only use SpaCy in Stage 2 and move on with mBERT vectorization method in Stage 3.

#### Deliverables:
1. Script "examineprocessed_outputcsv.py"
2. Markdown file "stage3/learningnotes.md"

### Step 2: Applying Vectorization to Subset & Quality Check
Vectorization takes a long time to process. To be more sufficient, I created a subset that contains 100 records to test and evaluate.

#### Deliverables:
1. Script ""
