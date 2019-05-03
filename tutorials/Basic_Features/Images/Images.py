
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/2/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-----------------------------------------------------
1. Read Image
2. Display Image using OpenCV library
3. Display image using matplotlib in jupyter notebook
4. Save Image
-----------------------------------------------------"""

# Import OpenCV Library
import cv2

# --------------------- Read image --------------------- #

## Load a color image, grayscale image and image with all information

# img_color = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR)
img_color = cv2.imread('OpenCV_Logo.png', 1)

# img_gray = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.imread('OpenCV_Logo.png', 0)

# img_unchange = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_UNCHANGED)
img_unchange = cv2.imread('OpenCV_Logo.png', -1)

#---------- Display image using openCV library ----------#

# If you uncomment Line 35 and run, you will find that no image shows
# that is because image shows and destroy in a very short of time
# cv2.imshow('image', img_color)

# display image
cv2.imshow('image', img_gray)

# wait, press any key to continue
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()

#---------------------------------#
# Display image using matplotlib
#---------------------------------#

# This part is used for display an image on jupyter notebook

#----------------------#
# Save or write image
#----------------------#

# The image will save under your work directory
cv2.imwrite('test_save.png',img_gray)



# Reference:
# Website: Opencv-Python Tutorials
# Link: https://opencv-python-tutroals.readthedocs.io/
# en/latest/py_tutorials/py_tutorials.html
