# You may run into issues installing pytesseract, this is because python wants you to install things into virtual environments
# For our usecase, venv aren't super useful as we are only making one project at a time, so use the flags below:
# sudo pip3 install pytesseract --break-system-packages
# https://nanonets.com/blog/ocr-with-tesseract/
from PIL import Image
#import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#Find the execution path and join it with the direct reference
def execution_path(filename):
  return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), filename)			

image = cv2.imread(execution_path("3_python-ocr.jpg"))

# Resize
#image = cv2.resize(image, (320, 120))

# Greyscale
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold         120 is threshold, 255 is what we assign if it is below this
_, image = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)

# Canny
image = cv2.Canny(image, 30,200)

# Countours (needs canny)
contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of Contours Found = " + str(len(contours)))
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(image, contours, -1, (255,0,0),2) #


cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
