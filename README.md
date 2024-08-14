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
2. Materials for test purposes are stored in the subfolder "text4test"

*During this process, I also used the Miro Board to guide my steps and drew workflow to explain this process to colleagues.*

## Stage 2: 2024 Spring
### Step 1: Accessing Data
In this step, I focused on accessing and downloading files from Invenio API; extracting text data from all downloaded files. Since the downloaded files come in different formats (pdf, word, jpg, mp3, etc.), I developed a strategy to extract text based on various file format.

These steps can be found in the script "apiinvenio-9th.py" (in folder "stage2").

### Step 2: Data Preprocessing
I clean all the extracted text using natural language processing methods, save them in a csv file, and prepare them for machine learning. During this step, many decisions were made based on 

## Stage 3: 2024 Summer/Fall

### Step 1:
This stage is built on the csv file created in Stage 2. The 

