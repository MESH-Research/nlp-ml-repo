# nlp-ml-repo
## Introduction
This repository documents stages of a project using computational methods in natural language processing and machine learning to support the Knowledge Commons. The project covers steps like data acquisition, text extraction, preprocessing, and vectorization. The end goal is to improve search functionality, offer related record recommendations, and implement subject tagging. Future steps, such as the validation of vectorization and its implementation to achieve these end goals, are left for future endeavor.

## Stage 1: Data acquisition and testing python libraries

### 1.1: Basics about InvenioRDM, API, Docker
- InvenioRDM: Read InvenioRDM [documentations](https://inveniordm.docs.cern.ch/)
- Using API to access files and stats: [Postman](https://www.postman.com/) & [Rest API](https://inveniordm.docs.cern.ch/reference/rest_api_index/)
- Docker environments

### 1.2: Testing libraries for the next step: text extraction
As part of the overall process, extracting textual data from the data source plays a crucial role. Since the files come in various formats, it is essential to test different Python libraries to determine which ones are most effective for text extraction.

#### Deliverables:
1. **Markdown file**: `tutorial1-textout.md` - a comparison of text extraction using various Python libraries across different file formats.
2. **Testing materials**: located in the `text4test` folder within the `stage1` subfolder.

## Stage 2: Text extraction and validation
Stage 2 focuses on extracting metadata and textual information from Invenio RDM. This involves accessing files via API, downloading them, converting files from various formats into text, and removing processed files locally. Any files that cannot be processed are flagged and stored separately for further review. The converted data is then evaluated to ensure quality, and a clean DataFrame is produced for subsequent processing steps.

### 2.1: Text extraction
This step involves accessing and downloading files from the Invenio API and extracting text data from the downloaded files. Since the files come in various formats (e.g., PDF, DOCX, PPTX, JPG, etc.), I developed a tailored strategy for text extraction based on each format. To optimize local storage, successfully processed files are deleted afterward.

#### Deliverables:
1. **Script**: `apiinvenio-9th.py` - used for text extraction.
2. **CSV file**: `output9clean.csv` - stored in OneDrive for data security.
3. **Files that cannot be processed**: stored under the folder `download_files` in OneDrive for data security.

### 2.2: Validation: checking the quality of the output
This step involves examining the CSV file generated in the previous stage to understand its data structure, identify any missing values, and review files that could not be processed.
***Note: Invenio imposes a strict limit of 10,000 records, which will be addressed in future steps.***

#### Deliverable:
1. **Markdown file**: `examine-output9.md` - documents the validation process and findings.

## Stage 3: Initial exploration of data; light data preprocessing and validation
At this stage, I received a CSV file from the previous stage. Traditional data preprocessing tasks at this point often include tokenization, lemmatization, stop word and punctuation removal, lowercasing, and combining results into a single preprocessed string. This was exactly what I did using SpaCy library. However, as I continued to learn, I realized that some of these steps (e.g., stop word removal or lemmatization) might not be necessary for models like BERT, which handle raw text effectively. I have documented the preprocessing process here to provide future researchers with flexibility in deciding what steps are most relevant for their work.

### 3.1: Data preprocessing
After comparing NLTK and SpaCy for data preprocessing, I chose SpaCy due to its lightweight design, up-to-date features, and manageable learning curve. The goal of this step was to produce a clean, processed CSV file for future use. Since some files contained over 3 million tokens, I developed strategies to process them in chunks, preventing out-of-memory (OOM) errors.

#### Deliverables:
1. **Script**: `csv-preprocessing2.py` - used for data preprocessing.
2. **CSV file**: `processed_output.csv` - stored in OneDrive for data security.

### 3.2: Validation: examine the preprocessed output
This step validates the preprocessed dataset for quality and consistency. Key tasks included checking for missing or null values in the Processed Text column and analyzing the text length distribution to identify potential outliers or anomalies. Additionally, the dataset’s language distribution was examined to verify that the processed records align with the intended multilingual scope. For further analysis, specific records were investigated based on their Record ID to ensure accurate processing and traceability. These validation steps ensure that the preprocessed data is ready for downstream applications.

#### Deliverables:
1. **Script**: `examineprocessed_outputcsv.py` - used for validating preprocessed data.

## Stage 4: Vectorization (learning and testing on a subset)
At this stage, I worked on applying vectorization to the preprocessed output to enable the development of future applications. Embedding/vectorization is a complex field, and I have been learning and testing along the way. To keep the process manageable, I focused on a subset of 100 records for initial testing.

### 4.1: Learning about vectorization
I studied embeddings and vectorization from a theoretical perspective to gain a deeper understanding of what happens behind the scenes. This approach helped me avoid applying tools without comprehension. While I initially considered continuing with SpaCy for vectorization, I decided to move forward with the BERT method due to SpaCy’s limitations in this area.

#### Deliverable:
1. **Markdown file**: `learningnotes.md` - contains notes on different types of embeddings.

### 4.2: Applying vectorization to the testing subset
Vectorization is computationally intensive and time-consuming. To optimize this stage, I created a subset of 100 records to test and evaluate the vectorization process.

#### Deliverable:
1. **Script**: `ml-step1.py` - used to apply vectorization to the subset.

### 4.3: Quality check of the results from 4.2
This step marks the point where my work on vectorization concluded. I performed initial quality checks on the subset results, leaving room for future researchers to expand upon this work. Once the subset passes a full quality check, the process can be scaled to train the entire dataset.


## Acknowledgements and Reflection
### Acknowledgements
Author Tianyi (Titi) Kou-Herrema is a German Studies PhD candidate who is interested in applying computational methods to assist scholarly work. She was hired as a research assistant for the Knowledge Commons (KC) Project from Summer 2023 to Fall 2024 where she developed this project while primarily working with Ian Scott and Stephanie Vasko (with much support from the rest of the tech team including Mike Thicke, Cassie Lem, Dimitrios Tzouris, and Bonnie Russell).

### Reflection
While computational methods were central to this project, the significant role of human decisions at each step cannot be overlooked. As a trained humanist, Titi has developed her coding skills through hands-on experience. Some early steps may, in hindsight, appear naive; however, they reflect the knowledge and tools available to her at the time. This document illustrates how she navigated learning curves, made thoughtful decisions, and continuously refined her approach.