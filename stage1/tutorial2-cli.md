# Tutorial 2: Text Extraction + Cli
This document is an extension of "Tutorial 1".

Creator: Tianyi Kou-Herrema; December 2023

*!!! This script was created in 2023 with other plans in mind. As of Summer 2024, I am putting a pause on CLI and focusing on model training.*
*Ignore this file for now.*

## Introduction
After testing all libraries, the next step is to write cli so it can be applied easily by users.


### 1. Cli for text extraction of PDF document


#### 1.1 For Text-based PDF: PyMuPDF

```python
#pip install click PyMuPDF
import click
import fitz

@click.command()
@click.argument('pdf_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path')
def extract_text(pdf_file, output):
    def process_pdf():
        with fitz.open(pdf_file) as doc:
            text = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text += page.get_text()

            return text

    extracted_text = process_pdf()

    if output:
        with open(output, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)
    else:
        print(extracted_text)

if __name__ == '__main__':
    extract_text()

#In bash: ~/knowledge-commons-repository$ python pdftest-1-click.py /home/tippy/Downloads/paper.pdf -o output.txt
# replace the file path for this script as well as the file path for the pdf file. Rename the output file.
```

#### Notes:


#### 1.2 For Image-based PDF: PyTesseract
