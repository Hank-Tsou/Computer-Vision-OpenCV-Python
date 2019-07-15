
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/15/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-----------------------
- Canny Edge Detection
-----------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# ------------------- Function to do Canny Edge Detection ------------------- #
def Canny_Edge_Detection(img):
    # Canny edge detector
    edges = cv2.Canny(img,100,200)

    # show result
    plt.subplot(121),plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Canny_Edge_Detection.py  -i Lenna.jpg

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    ## Functions
    Canny_Edge_Detection(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
