## Notes for this project
Develop a pipeline for performing NLP tasks in the Invenio RDM for Commons.

### To-Dos
- create a script that iterate through but ignore whatever was already processed for future useage;
- set up dev environment in my local env with Invenio (Docker)

### Initial observations
- See script 'apiinvenio-9th' for best result when extracting data
- 'investigation9.csv' contains 515 records that can not be processed with script 'apiinvenio-9th.py'. Details of 'investigation9.csv' will be written and provided
- Moving forward: 'output-9.csv' is being loaded into a dataframe.

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
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   Record ID       9487 non-null   object
 1   Languages       9472 non-null   object #some columns don't have language
 2   File Name       9487 non-null   object
 3   Extracted Text  9473 non-null   object #same here
dtypes: object(4)
memory usage: 296.6+ KB

Results: 1. no missing ID entries 2. 9487-9472=15 missing or null for 'languages' 3. 9487-9473=14 missing for 'extracted text'

**Statistical summary**
```python
print(df.describe())
```
          Record ID Languages     File Name Extracted Text
count          9487      9472          9487           9473
unique         9486        33          9412           9289
top     3s8nm-wg257       eng  document.pdf      OK Google
freq              2      7800            14             32

Here I might also have to restructure the dataframe based on file type? So I can handle audio files together. The "ok google" might be something happened during the mp3 conversion

**Unique values in columns** 
```python
print(df['Languages'].value_counts())
```
Languages
eng        7800
spa         448
deu         417
por         314
fra         116
ita          84
nld          52
rus          43
hin          34
heb          19
hun          19
tur          19
srp          14
cat          12
ell           9
ara           9
zho           8
jpn           8
fin           7
hrv           6
ces           6
urd           6
ind           5
ron           4
pol           3
bod           2
fra,eng       2
lat           1
fil           1
swe           1
fas           1
pes           1
cmn           1

**See length of extracted text**
```python
df['text_length'] = df['Extracted Text'].astype(str).apply(len)
print(df['text_length'].describe())
```
count    9.487000e+03
mean     7.335554e+04
std      4.015815e+05
min      2.000000e+00
25%      1.079650e+04
50%      3.276800e+04
75%      6.124550e+04
max      2.588425e+07

The min one only has two characters. Need to check!
The max one is a bit scary, and might need me to look into it...
Overall the csv feels normal to me.

#### Task 1 Missing values the dataframe
From the previous step, we now know that there are null value in the dataframe. Let's take a closer look.

```python
print(df.isnull().sum())
```
Record ID          0
Languages         15
File Name          0
Extracted Text    14

##### 1.1 Empty value under **'Languages'**:
```python
empty_languages = df[df['Languages'].isnull()]
print(empty_languages)
```

        Record ID  ...                                     Extracted Text
2     sdnj1-bkr82  ...   \n1 \nInvenio: A Group \nProcess  \nStephanie...
4     fsvjw-qnp62  ...   \n1 \nInvenio: A Group \nProcess  \nStephanie...
1388  9nqxt-n5q41  ...  El herrero del refranero  \n \nTyler Fisher \n...
1502  ts5a8-c3605  ...  !"#$"%&'()'($*'+%,-.&*$'*&)*&'/'0%,1'+,,2*'-)....
1770  mbyde-0ph51  ...  THE GAURI SHANKAR\nAUTH ANCOR: NI OF.\n\n \n\n...
2102  s3p8t-gnz33  ...       \n \n\n \n\n« [http //firgoa.usc.es/drupa...
2533  trkxs-h8m14  ...  WW:Waxa6utquuosa, f].Pyctamos, f.Monos,\n_ &.P...
2918  8md37-3eg10  ...  Historiography and Identity II\n \n \n \n \n \...
4115  dh0q1-tx024  ...   \n\n \n
                                I\n1flft\ninca ‘jp cbtnJIkIflh aUItth...
4117  b7zas-0tg35  ...   \n
                           arget area GTA\n\nwert at\n
                                                      aoe FETE\n‘ere...
4659  zes2d-81614  ...  Tinctoris’s Minimum Opus\nRob C. Wegman\n(Prin...
4702  hvpv7-5wk81  ...  F o r u m\nThomas Hobbes’ horror vacui und Joh...
5338  xd01x-cxb47  ...  1\nbook review\nGeorge Y. Kohler, Kabbalah Res...
8061  jwqtv-dj355  ...  BUILDING ACCESS\nUniversal Design and the  \nP...
9384  n88vv-9rx80  ...  &\n?\n43\n43\nOrgan\nÓ.\nÓ.\n.˙Ó.\nÓ.\nŒ\n˙\n....

Obviously, most of them still have solid content. It's only the language part that's missing.
Should i investigate why they are missing in the Invenio database? I did.

| Record ID | Reason for missing languages |
|------------------------------------------|
| sdnj1-bkr82 | no 'languages' in metadata |
| ts5a8-c3605 | no 'languages' in metadata |
| mbyde-0ph51 | no 'languages' in metadata |
| s3p8t-gnz33 | no 'languages' in metadata |

> Question for Ian: What should we do here? "Languages" is sort of a 'must-have' because in task 3, I might need to write a function to clean the extracted text based on their 'Languages'

##### 1.2 Empty value under **'Extracted Text'**:
```python
empty_text = df[df['Extracted Text'].isnull()]
print(empty_text)
```
        Record ID Languages                                          File Name Extracted Text
1058  hvpcy-kyf18       eng     the-sensuous-and-the-sensual-in-aesthetics.pdf            NaN
1590  7sj3c-dj639       eng                                       sleaking.pdf            NaN
2898  6gwmw-gxf43       deu                     2012-nwk-wunddokumentation.pdf            NaN
3045  st28q-2vk75       eng            excavations-at-kinik-hoyuk_kst-40.2.pdf            NaN
5589  htbm9-gg648       eng                                  close2theedge.pdf            NaN
6684  4spw5-qxt86       eng  review-hinduism-and-hindu-nationalism-online-j...            NaN
7368  3x7cm-z3973       eng  review-unconditional-equality-ajay-skaria-read...            NaN
7389  1xwm9-a9a84       eng  review-new-models-of-religious-understanding-e...            NaN
7405  c9ttt-xzr30       eng  review-hinduism-in-the-modern-world-reading-re...            NaN
7633  ssh5p-wsz88       eng  swartz-pattern-and-decoration-and-feminism-in-...            NaN
7634  86715-7jd71       eng    swartz-the-pattern-and-decoration-zeitgeist.pdf            NaN
8718  jwmxx-m2v33       eng            jnt628768-corrected-horrell-wan.pdf.pdf            NaN
9315  7qcc7-zyr12       eng            anne_swartz_review_mickalene_thomas.pdf            NaN
9355  5x6pp-nde27       heb                                      megamot-4.pdf            NaN

This part confused me a bit: I found the articles on staging and am not sure why the pdf files can not be read by the function i wrote.


#### Task 2 Duplication
There are duplicated files in the dataframe. What would be the best approach to deduplicate?

#### Task 3 Check language accuracy
Is this step really necessary?

#### Task 4 


### Completed Tasks:
- rerun the script;
- add tuple for function 'extract-file'
- test 'textract' lib and decided to not use
- add things or notes about what other tools use: did not do because I ended up using my own approach
- Can't access more than 10k records using API. Error messages: 2024-03-21 05:52:26,524 - INFO - Completed page 100 HTTP error: 400 Client Error: BAD REQUEST for url: https://invenio-dev.hcommons-staging.org/api/records?size=100&page=101
This has already been addressed and it's a hard limit Invenio set. I will ignore now.
