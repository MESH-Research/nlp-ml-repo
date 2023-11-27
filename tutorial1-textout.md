# Tutorial 1: Text Extraction
This document demonstrates the process of selecting .py libraries for text extraction.

Creator: Tianyi Kou-Herrema; November 2023

## Introduction
With the variety types of files hosted on Invenio, it is essential to come up with a suitable plan to extract texts and other information, based on file types.
The normal types of files we consider include (Top4-current focus):
- PDF
- DOCX
- PPT
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

For **Image-Based PDF**, there are different libraries: e.g.

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

There are different ways to approach this process. Here I provide code that does the following things: 1. OCR progress normally takes longer, in case user wasn't sure what is going on, you can get a better sense with the **progress bar**; 2. In case certain pages do not work, there is an **error warning message**. You will see "An error occured on page X"; 3. **Page Indicator** There is a line saying "--- End of Page X ---" to help identify potential issues; 4. Terminal will only show partial text if the file is large (e.g testing file is 11.5M). It's better to have an **output file**, named 'paper-img-extext.txt'. 5. Time calculation


*Remember to install packages first, `pip install PyMuPDF Pytesseract Pillow`.*

```python
import fitz
import pytesseract
from PIL import Image
import io
import timeit

def update_progress(progress):
    bar_length = 50  # Length of the progress bar
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
    pdf_path = 'text4test/paper-img.pdf'
    output_path = 'paper-img-extext.txt'
    extract_text_ocr(pdf_path, output_path)

# Time the execution of the main function
execution_time = timeit.timeit('main()', setup='from __main__ import main', number=1)
print(f"\nExecution time: {execution_time} seconds")

```

#### Main checkpoints:
- Footnotes: works
- Forms/Tables: tables will lose its form but the textual information can be extracted
- Citations: works

### 2. DOCX
The "X" in DOCX stands for XML (eXtensible Markup Language), which is used in the file format specification. DOCX files are based on Open XML format and this makes DOCX more efficient, reliable, and reduces the risk of file corruption compared to older binary formats like DOC. *The file tested in this section contains the same content as the one used in section 1/PDF.

There are different libraries, e.g. *docx-simple*, *docx2text*, *python-docx*, *Mammoth*. Just in case in the future whichever lib selected here doesn't fit anymore, feel free to test others.
