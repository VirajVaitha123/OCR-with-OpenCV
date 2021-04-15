# OCR-with-OpenCV


#### Introduction
This project focuses on using OCR to extract information from scanned documents. The documents may be in different orientations, and sizes.
First we utilize the ORB algorithm for OpenCV. 


#### Theory

OpenCV ORB_create():
This algorithm is an effective alternative to SIFT or SURF (These alternatives cost
whereas ORB is free). 

- ORB is a fast keypoint detector and brief descriptor (two algorithms working together). 
- It applies FAST to find keypoints and harris corner measure to find top N points among them. (READ more into HARRIS)
FAST doesn't compute orientation.
- Keypoint is a small region in an image that is distinctive. Corner is where a pixel changes sharply
from bright to dark.

Algorithmic process:
1.  Firstly the algorithm take a pixel and compare its brightness to the neighbouring pixels. If consecutive pixels 
vary significantly it will identify it as a keypoint. 
    
2. TBC



#### Prerequistes <br>
##### Install Packages: <br>

1.) tesseract
Popular libary for OCR. Free, and reliable especially for printed fonts.

Requires external installation

##### Step 1: Install tesseract-ocr 
Follow the link to https://github.com/UB-Mannheim/tesseract/wiki

Select the windows installation file: tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe (32 or 64 bit versions available)

##### Step 2: Copy file path to main.py file

2.) Opencv
Libary predominately used for processing image and videos

3.) numpy
Useful for storing data in arrays and access a large variety of methods to process this information efficiently

4.) pytesseract
Completes installation of tesseract. 

pip install used for all libaries except from tesseract (external installation)

<b> Download Images: </b>
Query Image - Blank form
Test Images - Forms containing information to be extracted
Original Forms - ?????

Download via https://www.murtazahassan.com/courses/opencv-projects/lesson/complete-code-files/

https://www.youtube.com/watch?v=W9oRTI6mLnU 22:58


Finish Video
Add comments
Update ReadMe
Move to Part2