### Introduction
Follow scripts in foler 'stage2', you will be able to follow how data from Invenio was acquired and preprocessed for further ML usage.

### Main Steps/Goals
- Acquire useful meta data and text information from Invenio RDM (access via API, download, convert files to text, remove files locally and store files can not be processed)
- Convert multi formats data into textual data
- Evaluate data after convertion, provide clean dataframe
- Preprocess the clean dataframe for the future

### Deliverables
- one csv file with all the clean data (currently stored in our One Drive), 'output9clean.csv' (py script to match this step is 'apiinvenio-9th.py' and some small steps see 'examine-output9.md')
- one csv file after nlp process using spaCy's library (currently stored in our One Drive), 'processed_output.csv' (py scripts to match this stsep is 'csv-preprocessing1.py'and 'csv-preprocessing2.py')
