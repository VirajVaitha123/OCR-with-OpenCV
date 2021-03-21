import numpy as np
import cv2
import pytesseract
import os

# C:\Program Files\Tesseract-OCR
pytesseract.pytesseract.Tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#### 1. Working Directory Path 
cwd = os.getcwd()
Imgs = cwd + "/Images"
Query_Image = Imgs + "/Query_Image.png"

#### 2. Reading in Query Image
ImgQ = cv2.imread(Query_Image)
cv2.imshow("Output",ImgQ)                          # Output image
cv2.waitKey(0)                                     # waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).