import numpy as np
import cv2
import pytesseract
import os

percentage = 25

# C:\Program Files\Tesseract-OC
pytesseract.pytesseract.Tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#### 1. Working Directory Path 
cwd = os.getcwd()
Imgs = cwd + "/Images"
Query_Image = Imgs + "/Query_Image.png"

#### 2. Reading in Query Image
ImgQ = cv2.imread(Query_Image)
h,w,c = ImgQ.shape
# ImgQ = cv2.resize(ImgQ, (w//3,h//3))               # Rescaling Image (Takes up less space)

#### 2. Preparing Detector
orb = cv2.ORB_create()                             # Number of Key Points (May need to iterate and display to find a good number)
kp1, des1 = orb.detectAndCompute(ImgQ,None)        # Identifies key points and descriptions from ORB
#impKp1 = cv2.drawKeypoints(ImgQ,kp1,None) 
#key_points and the unique points to the image, descriptors are t mnbvhewesdrftghjnmk,l.; / representation of these points making it easier to for the computer to understand

#### 3. Reading in User Forms
UserForms_Path = Imgs + "/UserForms"
MyPicList = os.listdir(UserForms_Path)

#### 4. Match to User Forms
for i,y in enumerate(MyPicList):                                          # Assigns index for each image
    img = cv2.imread(UserForms_Path + "/"+y)
    img = cv2.resize(img, (w//3,h//3))
    # cv2.imshow(y,img)
    kp2, des2 = orb.detectAndCompute(img,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)                                  # Initiates matcher
    matches = bf.match(des2,des1)                                         # Matches to query image
    matches.sort(key = lambda x: x.distance)                              # READ INTO
    good = matches[:int(len(matches)*(percentage/100))]                   # Ordered, so give top X% of matches
    imgMatch = cv2.drawMatches(img,kp2,ImgQ,kp1,good[:20],None,flags=2)        # Visualises the matches
    imgMatch = cv2.resize(imgMatch, (w//3,h//3))             # Resize to visualize clearly
    print("Showing Image" +str(y))
    cv2.imshow(y,imgMatch)

#### 3. Reading in Query Image
#cv2.imshow("KeyPointsQuery",impKp1)
cv2.imshow("Output",ImgQ)                          # Output image
cv2.waitKey(0)                                       # waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
