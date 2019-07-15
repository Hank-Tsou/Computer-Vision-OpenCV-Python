
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

# ------------------- Function to do Image Gradient ------------------- #
def Canny_Edge_Detection(img):

    cv2.imshow("image", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindow()


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_Gradient.py -i chess_board.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image and convert to grayscale image
    image = cv2.imread(args["image"])

    ## Functions
    Canny_Edge_Detection(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
