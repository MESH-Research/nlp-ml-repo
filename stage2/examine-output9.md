## Examine 'output9.csv' to control output quality
In the previous step, we successfully created the csv file that contains data extracted from InvenioRDM, named it "output9.csv".

### Step 1: Read csv headers and count rows
**Check headers and rows**
```python
import csv
import sys

csv.field_size_limit(sys.maxsize)
 
def read_csv_headers_and_count_rows(file_path):
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
        # Skip any null bytes in the file
        csv_reader = csv.reader((line.replace('\0', '') for line in file))
        headers = next(csv_reader)  # Read the header row
        row_count = sum(1 for _ in csv_reader)  # Count the remaining rows
 
    return headers, row_count
 
file_path = 'output9.csv'
headers, row_count = read_csv_headers_and_count_rows(file_path)
print("Headers:", headers)
print("Number of rows:", row_count)
```
Headers: ['Record ID', 'Languages', 'File Name', 'Extracted Text']
Number of rows: 9487

### Step 2 Further Examination

**View details about this dataframe**
```python
import pandas
csv_file_path = '/home/tippy/Documents/stage2/output9.csv'
df = pd.read_csv(csv_file_path, encoding='utf-8')
print(df.head()) #first 5 rows
print(df.info()) #info about dataframe
```

RangeIndex: 9487 entries, 0 to 9486
Data columns (total 4 columns):
| #   | Column          | Non-Null Count | Dtype |
|-----|-----------------|----------------|-------|
| 0   | Record ID       | 9487 non-null  | object |
| 1   | Languages       | 9472 non-null  | object |
| 2   | File Name       | 9487 non-null  | object |
| 3   | Extracted Text  | 9473 non-null  | object |
memory usage: 296.6+ KB

Results: 
1. no missing ID entries
2. 9487-9472=15 missing or null for 'Languages'
3. 9487-9473=14 missing for 'Extracted Text'

**Statistical summary**
```python
print(df.describe())
```
| Column         | Count | Unique | Top           | Freq |
|----------------|-------|--------|---------------|------|
| Record ID      | 9487  | 9486   | 3s8nm-wg257   | 2    |
| Languages      | 9472  | 33     | eng           | 7800 |
| File Name      | 9487  | 9412   | document.pdf  | 14   |
| Extracted Text | 9473  | 9289   | OK Google     | 32   |

The "ok google" might be something happened during the mp3 conversion.

**Unique values in columns** 
```python
print(df['Languages'].value_counts())
```
| Language Code | Count |
|---------------|-------|
| eng           | 7800  |
| spa           | 448   |
| deu           | 417   |
| por           | 314   |
| fra           | 116   |
| ita           | 84    |
| nld           | 52    |
| rus           | 43    |
| hin           | 34    |
| heb           | 19    |
| hun           | 19    |
| tur           | 19    |
| srp           | 14    |
| cat           | 12    |
| ell           | 9     |
| ara           | 9     |
| zho           | 8     |
| jpn           | 8     |
| fin           | 7     |
| hrv           | 6     |
| ces           | 6     |
| urd           | 6     |
| ind           | 5     |
| ron           | 4     |
| pol           | 3     |
| bod           | 2     |
| fra,eng       | 2     |
| lat           | 1     |
| fil           | 1     |
| swe           | 1     |
| fas           | 1     |
| pes           | 1     |
| cmn           | 1     |

**See length of extracted text**
```python
df['text_length'] = df['Extracted Text'].astype(str).apply(len)
print(df['text_length'].describe())
```
| Statistic | Value       |
|-----------|-------------|
| Count     | 9487.000    |
| Mean      | 73,355.54   |
| Std       | 401,581.5   |
| Min       | 2.00        |
| 25%       | 10,796.50   |
| 50%       | 32,768.00   |
| 75%       | 61,245.50   |
| Max       | 25,884,250  |

Overall the csv feels normal to me.

#### Step 2: Task 1 Missing values the dataframe
From the previous step, we now know that there are null value in the dataframe. Let's take a closer look.

```python
print(df.isnull().sum())
```
| Column          | Missing Values |
|-----------------|----------------|
| Record ID       | 0              |
| Languages       | 15             |
| File Name       | 0              |
| Extracted Text  | 14             |

##### 1.1 Empty value under **'Languages'**:
```python
empty_languages = df[df['Languages'].isnull()]
print(empty_languages)
```
| Record ID | Extracted Text                                                     |
|-----------|--------------------------------------------------------------------|
| sdnj1-bkr82 | \n1 \nInvenio: A Group \nProcess  \nStephanie...                  |
| fsvjw-qnp62 | \n1 \nInvenio: A Group \nProcess  \nStephanie...                  |
| 9nqxt-n5q41 | El herrero del refranero  \n \nTyler Fisher \n...                 |
| ts5a8-c3605 | !"#$"%&'()'($*'+%,-.&*$'*&)*&'/'0%,1'+,,2*'-)...                  |
| mbyde-0ph51 | THE GAURI SHANKAR\nAUTH ANCOR: NI OF.\n\n \n\n...                |
| s3p8t-gnz33 | \n \n\n \n\n« [http //firgoa.usc.es/drupa...                     |
| trkxs-h8m14 | WW:Waxa6utquuosa, f].Pyctamos, f.Monos,\n_ &.P...                 |
| 8md37-3eg10 | Historiography and Identity II\n \n \n \n \n \n...                |
| dh0q1-tx024 | \n\n \n\nI\n1flft\ninca ‘jp cbtnJIkIflh aUItth...                |
| b7zas-0tg35 | \narget area GTA\n\nwert at\n\naoe FETE\n‘ere...                 |
| zes2d-81614 | Tinctoris’s Minimum Opus\nRob C. Wegman\n(Prin...                 |
| hvpv7-5wk81 | F o r u m\nThomas Hobbes’ horror vacui und Joh...                 |
| xd01x-cxb47 | 1\nbook review\nGeorge Y. Kohler, Kabbalah Res...                 |
| jwqtv-dj355 | BUILDING ACCESS\nUniversal Design and the  \nP...                 |
| n88vv-9rx80 | &\n?\n43\n43\nOrgan\nÓ.\nÓ.\n.˙Ó.\nÓ.\nŒ\n˙\n....                 |

Obviously, most of them still have solid content. It's only the language part that's missing.
So i investigate why they are missing in the Invenio database:

| Record ID   | Reason for missing languages     |
|-------------|----------------------------------|
| sdnj1-bkr82 | no 'languages' in metadata       |
| ts5a8-c3605 | no 'languages' in metadata       |
| mbyde-0ph51 | no 'languages' in metadata       |
| s3p8t-gnz33 | no 'languages' in metadata       |

This might not affect our overall goal for the larger picture, so I chose to ignore for now.

##### 1.2 Empty value under **'Extracted Text'**:
```python
empty_text = df[df['Extracted Text'].isnull()]
print(empty_text)
```
| Record ID  | Languages | File Name                                                  | Extracted Text |
|------------|-----------|------------------------------------------------------------|----------------|
| hvpcy-kyf18 | eng       | the-sensuous-and-the-sensual-in-aesthetics.pdf             | NaN            |
| 7sj3c-dj639 | eng       | sleaking.pdf                                               | NaN            |
| 6gwmw-gxf43 | deu       | 2012-nwk-wunddokumentation.pdf                             | NaN            |
| st28q-2vk75 | eng       | excavations-at-kinik-hoyuk_kst-40.2.pdf                    | NaN            |
| htbm9-gg648 | eng       | close2theedge.pdf                                          | NaN            |
| 4spw5-qxt86 | eng       | review-hinduism-and-hindu-nationalism-online-j...          | NaN            |
| 3x7cm-z3973 | eng       | review-unconditional-equality-ajay-skaria-read...          | NaN            |
| 1xwm9-a9a84 | eng       | review-new-models-of-religious-understanding-e...          | NaN            |
| c9ttt-xzr30 | eng       | review-hinduism-in-the-modern-world-reading-re...          | NaN            |
| ssh5p-wsz88 | eng       | swartz-pattern-and-decoration-and-feminism-in-...          | NaN            |
| 86715-7jd71 | eng       | swartz-the-pattern-and-decoration-zeitgeist.pdf            | NaN            |
| jwmxx-m2v33 | eng       | jnt628768-corrected-horrell-wan.pdf.pdf                    | NaN            |
| 7qcc7-zyr12 | eng       | anne_swartz_review_mickalene_thomas.pdf                    | NaN            |
| 5x6pp-nde27 | heb       | megamot-4.pdf                                              | NaN            |

I found the articles on staging and am not sure why the pdf files can not be read by the function i wrote.

#### Step 2: Task 2 Duplication
There are duplicated files in the dataframe. Duplicated files should not affect our goals that much, hence I ignored here.

#### Step 2: Task 3 Check language accuracy
This step is not necessary at this point.

### Step 3: Remove all files with null value
To ensure we move forward with this project, I made the following decisions:
- ignore all entries with empty values because they can be investigated later
- keep output9.csv the way it is; create a new csv with clean dataframe for further process and call it "output9clean.csv"

```python
csv_file_path = '/home/tippy/Documents/stage2/output9.csv'
df = pd.read_csv(csv_file_path, encoding='utf-8')
#print("Column names:", df.columns.tolist())
#remove empty ones
filtered_df =df[df['Languages'].notna() & df['Extracted Text'].notna()]
#save it
filtered_df.to_csv('output9clean.csv', index=False)
#check the new file
df_clean = pd.read_csv('output9clean.csv')
print(df_clean.info())
```

RangeIndex: 9458 entries, 0 to 9457
Data columns (total 4 columns):
| #   | Column          | Non-Null Count | Dtype |
|-----|-----------------|----------------|-------|
| 0   | Record ID       | 9458 non-null  | object |
| 1   | Languages       | 9458 non-null  | object |
| 2   | File Name       | 9458 non-null  | object |
| 3   | Extracted Text  | 9458 non-null  | object |
memory usage: 295.7+ KB
 
Everything adds up. Can move on to the next step.

### Extra things I should look into later:
- Can't access more than 10k records using API. Error messages: 2024-03-21 05:52:26,524 - INFO - Completed page 100 HTTP error: 400 Client Error: BAD REQUEST for url: https://invenio-dev.hcommons-staging.org/api/records?size=100&page=101
This has already been addressed and it's a hard limit Invenio set. I will ignore now.
- 'investigation9.csv' contains 515 records that can not be processed with script 'apiinvenio-9th.py'. Details of 'investigation9.csv' will be written and provided.
