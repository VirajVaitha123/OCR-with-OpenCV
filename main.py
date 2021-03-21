import numpy as np
import cv2
import pytesseract

# C:\Program Files\Tesseract-OCR

pytesseract.pytesseract.Tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import os
cwd = os.getcwd()
print(cwd)

ImgQ = cv2.imread("C:/Users/Viraj/Repos/OCR-with-OpenCV/Images/Query_Image.png")
cv2.imshow("Output",ImgQ)
#cv2.waitKey(0)