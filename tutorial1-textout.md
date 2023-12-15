# Tutorial 1: Text Extraction
This document demonstrates the process of selecting .py libraries for text extraction.

Creator: Tianyi Kou-Herrema; November 2023

## Introduction
With the variety types of files hosted on Invenio, it is essential to come up with a suitable plan to extract texts and other information, based on file types.
The normal types of files we consider include (Top4-current focus):
- PDF
- DOCX
- PPTX
- CSV
- EPUB
- RTF
- LaTeX
- Markdown
- JSON

Let's start to look at them one by one!

Noted: all libraries are judged based on (from most to least important):
- Document Quality
- Ease to Learn
- Community Support (maintenance; up-to-date)
- Performance Metrics

### 1. PDF (Portable Document Format)
There are two types of PDF files we encounter in our usage:
- Text-Based PDF
- Image-Based PDF

For **Text-Based PDF**, there are different libraries, e.g. *PyPDF2* (simple), *PDFMiner* (deep learning curve), *PyMuPDF(fitz)*, *Textract*. Just in case in the future whichever lib selected here doesn't fit anymore, feel free to test others.

#### 1.1 For Text-based PDF: PyMuPDF
After comparing all results, I eventually selected **PyMuPDF(fitz)** for performance and versatility.

*Remember to install packages first, `pip install PyMuPDF`.*

```python
import fitz
import timeit

# Switch this path to your own file path
def process_pdf():
    with fitz.open('text4test/paper.pdf') as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            print(page.get_text())

# People do multiple times and then find average. I just use 1.
number_of_executions = 1

# Use timeit to measure the execution time
execution_time = timeit.timeit('process_pdf()', setup='from __main__ import process_pdf', number=number_of_executions)

print(f"Execution time: {execution_time} seconds")
```

#### Main checkpoints:
- Footnotes: included
- Forms/Tables: if the table is in embedded, than it's fine; image won't work
- Citations: good

#### 1.2 For Image-based PDF: PyTesseract
This process involves two steps: OCR & parse text from OCR results. So we will start with a PDF processing library, such as **PyMuPDF(fitz)**. Then we will use **PyTesseract** because the Tesseract community is well-maintained.

There are different ways to approach this process. Here I provide code that does the following things: 1. OCR progress normally takes longer, in case user wasn't sure what is going on, you can get a better sense with the **progress bar**; 2. In case certain pages do not work, there is an **error warning message**. You will see "An error occured on page X"; 3. **Page Indicator** There is a line saying "--- End of Page X ---" to help identify potential issues; 4. Terminal will only show partial text if the file is large (e.g testing file is 11.5M). It's better to have an **output file**, named 'pdf-img-extext.txt'. 5. Time calculation


*Remember to install packages first, `pip install PyMuPDF Pytesseract Pillow`.*

```python
import fitz
import pytesseract
from PIL import Image
import io
import timeit

def update_progress(progress):
    bar_length = 50
    block = int(round(bar_length * progress))
    text = "\rProgress: [{0}] {1}%".format("#" * block + "-" * (bar_length - block), round(progress * 100, 2))
    print(text, end='')

def extract_text_ocr(pdf_path, output_path):
    text = ''

    with fitz.open(pdf_path) as doc:
        total_pages = len(doc)
        for page_num in range(total_pages):
            page = doc.load_page(page_num)
            image_list = page.get_images(full=True)
            total_images = len(image_list)

            for image_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image = Image.open(io.BytesIO(image_bytes))
                    text += pytesseract.image_to_string(image)
                except Exception as e:
                    print(f"\nAn error occurred on page {page_num + 1}, image {image_index + 1}: {e}")

                # Update progress bar
                current_progress = ((page_num * total_images + image_index + 1) / (total_pages * total_images))
                update_progress(current_progress)

            text += f"\n----- End of Page {page_num + 1} -----\n"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    pdf_path = 'text4test/paper-img.pdf' #replace with your own path
    output_path = 'pdf-img-extext.txt' #or give it another name
    extract_text_ocr(pdf_path, output_path)

# Time the execution of the main function, with my test document, it took 54 seconds. Anticipate it to be long if your scanned document is large.
execution_time = timeit.timeit('main()', setup='from __main__ import main', number=1)
print(f"\nExecution time: {execution_time} seconds")

```

#### Main checkpoints:
- Footnotes: works
- Forms/Tables: tables will lose its form but the textual information can be extracted
- Citations: works

### 2. DOCX
The "X" in DOCX stands for XML (eXtensible Markup Language), which is used in the file format specification. DOCX files are based on Open XML format and this makes DOCX more efficient, reliable, and reduces the risk of file corruption compared to older binary formats like DOC. *The file tested in this section contains the same content as the one used in section 1/PDF.

There are different libraries, e.g. *docx-simple*, *docx2txt*, *python-docx*, *Mammoth*. Just in case in the future whichever lib selected here doesn't fit anymore, feel free to test others.

#### 2.1 Python-docx Library
*Remember to install packages first, `pip install python-docx`.*

```Python
import docx
import timeit

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

if __name__ == "__main__":
    docx_file = "text4test/paper.docx"  # Replace with your DOCX file's path

    # Measure execution time
    execution_time = timeit.timeit(
        stmt=lambda: extract_text_from_docx(docx_file),
        number=1  # You can change the number of iterations if needed
    )

    extracted_text = extract_text_from_docx(docx_file)

    print("Extracted Text:") #You don't necessarily need this
    print(extracted_text)

    print(f"Execution Time: {execution_time:.4f} seconds")

```
#### Main checkpoints:
- Footnotes: not included
- Forms/Tables: if the table is in embedded, than it's fine; image won't work
- Citations: good

#### 2.2 Docx2txt Library
*Remember to install packages first, `pip install docx2txt`.*

```Python
#this library also doesn't show any footnotes, but it can read images that has texts, which is a surprise.

import docx2txt
import timeit

def extract_text_from_docx(docx_file):
    text = docx2txt.process(docx_file)
    return text

if __name__ == "__main__":
    docx_file = "text4test/paper.docx"  # Replace with your DOCX file's path
    output_file = "docx-extext.txt"  # Replace with the desired output file path

    # Measure execution time
    execution_time = timeit.timeit(stmt=lambda: extract_text_from_docx(docx_file),number=1)

    extracted_text = extract_text_from_docx(docx_file)

    # Save extracted text to the output file
    with open(output_file, "w", encoding="utf-8") as output:
        output.write(extracted_text)

    print("Extracted Text:")
    print(extracted_text)

    print(f"Execution Time: {execution_time:.4f} seconds")
    print(f"Extracted text saved to {output_file}")
```
#### Main checkpoints:
- Footnotes: still not included
- Forms/Tables: if the table is in embedded, than it's fine; Magically! Image can be read without writing new codes!!!
- Citations: good

#### 2.3 Mammoth library
The Mammoth library is designed to convert .docx into HTML or plain text while perserving some of the formatting.

*Remember to install packages first, `pip install mammoth beautifulsoup4`.*

```Python
import mammoth
from bs4 import BeautifulSoup
import timeit

# Function to extract text from .docx file
def extract_text(docx_file):
    with open(docx_file, "rb") as docx:
        result = mammoth.convert_to_html(docx)
        html_content = result.value  # The extracted HTML
        messages = result.messages #Whatever messages might occur during this process, you can later print(messages) to double check

    soup = BeautifulSoup(html_content, "html.parser") #use bs to parse HTML content
    text = soup.get_text(separator='\n', strip=True) #stripping extra whitespace
    return text

# You can switch this to your file path
docx_file = "text4test/paper.docx"

# Timing the execution of the extract_text function
execution_time = timeit.timeit(lambda: extract_text(docx_file), number=1)

print("\nExtracted Text:")
print(extract_text(docx_file))
print(f"Execution time: {execution_time} seconds")
```

#### Main checkpoints:
- Footnotes: Finally included!
- Forms/Tables: if the table has embedded text, then the text will be extracted; if the table/other visualization is image, then it will be ignored.
- Citations: good

### 3. PPTX
.pptx files are often used for conference talks and contain a mix of text, images, captions, speaker notes, and references.

*Remember to install packages first, `pip install python-pptx tersseract`.*

```python
from pptx import Presentation
import timeit
import io
from PIL import Image
import pytesseract

def extract_content_from_pptx(pptx_file):
    prs = Presentation(pptx_file)
    extracted_content = []
    image_texts = []

    for slide in prs.slides:
        # Extracting text from each shape
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    extracted_content.append(paragraph.text.strip())
            elif shape.shape_type == 13:  # Shape type 13 corresponds to a picture
                image = shape.image
                image_bytes = io.BytesIO(image.blob)
                image_text = pytesseract.image_to_string(Image.open(image_bytes))
                image_texts.append(image_text.strip())

            # Extracting text from tables
            if shape.shape_type == 19:  # Shape type 19 corresponds to a table
                for row in shape.table.rows:
                    for cell in row.cells:
                        extracted_content.append(cell.text.strip())

        # Extracting speaker notes
        if slide.has_notes_slide:
            notes_slide = slide.notes_slide
            if notes_slide.notes_text_frame:
                for paragraph in notes_slide.notes_text_frame.paragraphs:
                    extracted_content.append(paragraph.text.strip())

    return '\n'.join(extracted_content), '\n'.join(image_texts)

# You can add your file path
pptx_file = 'text4test/talk.pptx'

# Measure execution time
execution_time = timeit.timeit(lambda: extract_content_from_pptx(pptx_file), number=1)

# Extract and print content
extracted_content, image_texts = extract_content_from_pptx(pptx_file)

print("\nExtracted Content:") # This might not be needed
print(extracted_content)
print("\nText from Images:") # This might not be needed
print(image_texts)
print(f"Execution time: {execution_time} seconds")
# Using my test file, around 8-9s.
```

#### Main checkpoints:
- Speakers note: Yes! In this code all speakers note are listed under content. You can also manipulate them to be listed seperately.
- Images: All images are processed by PyTesseract.
- Tables: Textual information from tables are extracted sucessfully.
- Special characters: Captured. Math equations, captured. Equations on images might be unclear.
- References (last page): Clear, good.

### 4. EPUB
EPUB is an e-book file format that uses the ".epub" file extension. The term is short for electronic publication and is sometimes styled ePub.

There are two commonly used libraries, e.g. *epub2txt*, *EbookLib*. Here I am using *EbookLib* because it can process both text and images.

*Remember to install packages first, `pip install ebooklib beautifulsoup4`.*

```Python
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extracted_text_epub(file_path):
  book = epub.read_epub(file_path)
  test=''

  for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
      soup= BeautifulSoup(item.content,'html.praser')
      text+=soup.get_text()+'\n'

  return text

file_path = 'paper.epub'
extracted_text = extracted_text_epub(file_path)
print(extracted_text)
```
#### Main checkpoints:
- Footnotes: Included and clear
- Forms/Tables: if the table has embedded text, then the text will be extracted; if the table/other visualization is image, then it will be ignored.
- Citations: clear and good

### 5. RTF
RTF stands for Rich Text Format. This file format allows you to exchange text files between different word processors in different operating systems.

There are two commonly used libraries, e.g. *Pyth RTF*, *striprtf*. However, I encountered problems trying both libraries. The attempt of converting .rtf to .xml and then extracting also yielded in failure due to lack of maintenance of the package. The way to work around it is to convert RTF to DOCX and then follow the .docx procedures. Install LibreOffice.


```console
libreoffice --convert-to docx Paperfortest1.rtf --headless
```

### 6. CSV
a CSV file is a text file that has a specific format which allows data to be saved in table structured format. CSV stands for comma-separated values.

Notes:
After testing different .csv files, I believe for best practice, we should treat .csv file seperately. This type of file is generally uploaded as a shared dataset, rather than published paper. (It might be part of a published paper. Including .csv file or not, should be decided based on our research goal.

Here I provide one proper way of handling .csv files using the most standard python library *pandas*

*Remember to install packages first, `pip install pandas`.*

```Python
import pandas as pd

#mental_health.csv has a very simple data structure; instrument_export.csv has more columns. This comparison is to show each csv file is very different and should be handled with more human judgement.

file_path='text4test/mental_health.csv'
#or file_path='text4test/instrument_export.csv' or your file
df = pd.read_csv(file_path)
print("Column names",df.columns.tolist())
#here you can see the columns printed out
columns_to_extract = ['selectedColumn1','selectedColumn2']

textual_data = df[columns_to_extract]

print(textual_data.head())
#here I only prnted head, but can also save the data into a new file.
```
