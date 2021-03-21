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
h,w,c = ImgQ.shape
ImgQ = cv2.resize(ImgQ, (w//3,h//3))               # Rescaling Image (Takes up less space)

#### 2. Preparing Detector
orb = cv2.ORB_create(1000)                         # Number of Key Points (May need to iterate and display to find a good number)            
kp1, des1 = orb.detectAndCompute(ImgQ,None)
impKp1 = cv2.drawKeypoints(ImgQ,kp1,None) 
#key_points and the unique points to the image, descriptors are the representation of these points making it easier to for the computer to understand



#### 3. Reading in Query Image
cv2.imshow("KeyPointsQuery",impKp1)         
cv2.imshow("Output",ImgQ)                          # Output image
cv2.waitKey(0)                                     # waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).