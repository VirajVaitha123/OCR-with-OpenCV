# OCR-with-OpenCV


#### Introduction
This project focuses on using OCR to extract information from scanned documents. The documents may be in different orientations, and sizes.

#### Prerequistes
Packages:
1.) tesseract
Popular libary for OCR. Free, and reliable especially for printed fonts.

Requires external installation

<u> Step 1: Install tesseract-ocr </u>
Follow the link to https://github.com/UB-Mannheim/tesseract/wiki

Select the windows installation file: tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe (32 or 64 bit versions available)

<u> Step 2: Copy file path to main.py file </u>

2.) Opencv
Libary predominately used for processing image and videos

3.) numpy
Useful for storing data in arrays and access a large variety of methods to process this information efficiently

4.) pytesseract
Completes installation of tesseract. 

Conda install command used for all libaries except from tesseract (external installation) and pytesseract (pip install as not found via conda)