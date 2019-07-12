
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/12/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-------------------------------------------------
- Image filtering (Image Blurring, Image Smoothing)
    - 2D convolution Filtering
    - Averaging Filtering
    - Gaussian Filtering
    - Median Filtering
    - Bilateral Filtering
--------------------------------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# ------------------- Function to do 2D convolution Filtering ------------------- #
def Image_filtering(img):
    # 2D convolution Filtering
    kernel = np.ones((3,3), np.float32)/25
    # 3 * 3 kernel as below:
    # [1, 1, 1]
    # [1, 1, 1]  *  1/25
    # [1, 1, 1]
    conv_filtering = cv2.filter2D(img, -1, kernel)

    # average filtering
    average = cv2.blur(img,(5,5))

    # gaussian filtering
    gaussian = cv2.GaussianBlur(img,(5,5),0)

    # median filtering
    median = cv2.medianBlur(img,5)

    # bilateral filtering
    bilateral = cv2.bilateralFilter(img,9,75,75)

    # show result images
    plt.subplot(231),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232),plt.imshow(conv_filtering),plt.title('conv_filtering')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233),plt.imshow(average),plt.title('average')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234),plt.imshow(gaussian),plt.title('gaussian')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235),plt.imshow(median),plt.title('median')
    plt.xticks([]), plt.yticks([])
    plt.subplot(236),plt.imshow(bilateral),plt.title('bilateral')
    plt.xticks([]), plt.yticks([])
    plt.show()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_filtering.py -i noise.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    ## Functions
    Image_filtering(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
