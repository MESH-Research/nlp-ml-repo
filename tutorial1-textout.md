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
#replace this path
#!!! This is what I need to check keyword"with"? context manager?: with open(myfile) as myfile_obj:
# In this case, no need to close file anymore. once I leave the indented, open function knows I am done.
doc = fitz.open('test1.pdf')
page = doc.loadPage(0)
text = page.getText()
print(text)
doc.close
```
#### Main checkpoints:
- Footnotes
- Forms/Tables (two types: normal table and visualizations)
- Citations

#### 1.2 For Image-based PDF: PyTesseract
This process involves two steps: OCR & parse text from OCR results. So we will start with a PDF processing library, such as **PyMuPDF(fitz)**. Then we will use **PyTesseract** because the Tesseract community is well-maintained.

*Remember to install packages first, `pip install tesseract-ocr`.*

Here I provide two scripts: the first one is more efficient as it process images in memory; the second one create images and then deletes them. If the file is relatively straightforward and clean, take the first approach. If the file is very complex and requires potentially handle error later on, use the second method.

 **Method I**


```python
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Define the path to your PDF file, please replace this with your own
pdf_path = '/home/tippy/Downloads/Paper4test-type2.pdf'

# Open the PDF file
doc = fitz.open(pdf_path)

# Iterate over each page
for page_number in range(len(doc)):
    page = doc.load_page(page_number)  # Load the current page
    pix = page.get_pixmap()  # Render page to an image (pixmap)

    # Convert the pixmap to a PIL Image
    img = Image.open(io.BytesIO(pix.tobytes()))

    # Perform OCR using Pytesseract
    text = pytesseract.image_to_string(img)

    # Print or process the extracted text
    print(f"Text from page {page_number + 1}:\n{text}\n")

# Close the document
doc.close()
```

**Method II**

```python
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)

    text = ''
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image to disk temporarily
        image_file = f"page_{page_num + 1}.png"
        image.save(image_file)

        # Perform OCR and append extracted text
        extracted_text = pytesseract.image_to_string(image)
        text += extracted_text

        # Remove the generated image file after extraction
        import os
        os.remove(image_file)

    pdf_document.close()
    return text

if __name__ == "__main__":
     pdf_path = '/home/tippy/Downloads/Paper4test-type2.pdf'  # Replace with your file path
     extracted_text = extract_text_from_pdf(pdf_path)
     print(extracted_text)
```

#### Main checkpoints:
- Footnotes
- Forms/Tables (two types: normal table and visualizations)
- Citations

### 2. DOCX
The "X" in DOCX stands for XML (eXtensible Markup Language), which is used in the file format specification. DOCX files are based on Open XML format and this makes DOCX more efficient, reliable, and reduces the risk of file corruption compared to older binary formats like DOC.
