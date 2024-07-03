#This is modified script to process large 'extracted text'. The designning idea is: filter, seperate large text; process them differently; aggregate them before modeling

import spacy
import pandas as pd
import logging
import psutil
import gc
from memory_profiler import profile

logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

def log_memory_usage(message):
    memory = psutil.virtual_memory()
    logging.debug(f"{message} - Memory usage: {memory.percent}% used, {memory.available // (1024 * 1024)} MB available")

#selecting language models
languages_to_process = ['eng', 'spa','deu','por','fra']
model_names = ['en_core_web_sm','es_core_news_sm','de_core_news_sm','pt_core_news_sm','fr_core_news_sm']
nlp_models = {}
for lang, model_name in zip(languages_to_process, model_names):
    try:
        nlp_models[lang] = spacy.load(model_name, disable=['parser','tagger','ner'])
        logging.debug(f"Loaded {model_name} for language {lang}")
    except Exception as e:
        logging.error(f"Failed to loda model {model_name} for language {lang}: {e}")

#Set 'max_length' back to default: 1 million
for lang in nlp_models:
    try:
        nlp_models[lang].max_length = 1000000
        logging.debug(f"Set max_length for model for language {lang} to 1000000")
    except Exception as e:
        logging.error(f"Error setting max_length for {lang}: {e}")

def separate_large_texts(df, column_name='Extracted Text', max_length=1000000):
    normal_texts = df[df[column_name].str.len() <= max_length]
    large_texts = df[df[column_name].str.len() > max_length]
    return normal_texts, large_texts

def chunk_text(text, chunk_size=10000):
    """Yield successive chunk_size chunks from text."""
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]

def process_large_text(text, lang_model):
    """Process a large text by chunking it first."""
    chunks = chunk_text(text)
    processed_chunks = []
    for chunk in chunks:
        processed_chunk = preprocess_text(chunk, lang_model)
        processed_chunks.append(processed_chunk)
    return ''.join(processed_chunks)


#Tokenization, then lemmatization, convert to lowercase, remove stop words and punctuation. Send everything to a single string.
#This is the step using a lot of mem, so I added the @profile
@profile
def preprocess_text(text, lang_model):
    try:
        doc = lang_model(text)
        clean_tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        result = "".join(clean_tokens)
        return result
    except Exception as e:
        snippet = text[:50] #log first 50 characters of the failed text
        logging.error(f"Failed to preprocess text: {e}")
        return ""

#filters the df by languages and then apply 'preprocess_text' function to each row based on their lang. Put processed data into a new dataframe
def filter_and_preprocess(df, languages, nlp_models):
    all_processed_data = []
    for lang in languages:
        if lang in nlp_models:
            if lang in nlp_models:
                normal_texts, large_texts = separate_large_texts(df[df['Languages'] == lang], 'Extracted Text')
                normal_texts['Processed Text'] = normal_texts['Extracted Text'].apply(lambda text: preprocess_text(text, nlp_models[lang]))
                large_texts['Processed Text'] = large_texts['Extracted Text'].apply(lambda text: preprocess_text(text, nlp_models[lang]))
                all_processed_data.append(pd.concat([normal_texts, large_texts], ignore_index=True))
        else:
            logging.warning(f"No model available for language {lang}")
    return pd.concat(all_processed_data, ignore_index=True) if all_processed_data else pd.DataFrame()

def process_in_batches(filepath, batch_size, languages, nlp_models):
    chunk_number = 0
    try:
        for chunk in pd.read_csv(filepath, chunksize=batch_size):
            chunk_number += 1
            log_memory_usage(f"Before processing batch {chunk_number}")
            processed_chunk = filter_and_preprocess(chunk, languages, nlp_models)
            if chunk_number ==1:
                processed_chunk.to_csv('processed_output.csv', index=False)
            else:
                processed_chunk.to_csv('processed_output.csv', index=False, mode='a', header=False)

            logging.debug(f"Finished processing batch {chunk_number} with {len(processed_chunk)} records")
            log_memory_usage(f"After processing batch {chunk_number}")

            # Explicitly call garbage collection
            gc.collect()
            log_memory_usage(f"After garbage collection post-batch {chunk_number}")
    except Exception as e:
        logging.error(f"Failed during processing batch {chunk_number}: {e}")
        raise

try:
    batch_size = 1
    clean_df = process_in_batches('output9clean.csv', batch_size, languages_to_process, nlp_models)
    logging.info("Data processing complete")
except Exception as e:
    logging.error(f"Failed during batch processing: {e}")
