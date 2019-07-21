
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/20/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""------------------
- Image Histogram
------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# ------------------- Function to find histogram ------------------- #
def Histogram(img):
    # convert to gray scale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # calculate histogram
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    # show result
    plt.plot(hist)
    plt.show()

    # Histogram for each channel blue, green, red
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

# ------- Function to find partial image histogram with a mask ------- #
def Partial_Histogram(img):
    # generate a mask
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[0:100, 0:200] = 255

    # partial image by cover the mask
    masked_img = cv2.bitwise_and(img, img, mask = mask)

    # calculate histogram
    hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
    hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

    # show the result
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.plot(hist_full)
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_mask)
    plt.xlim([0,256])

    plt.show()

# ---------------- Function to do Histogram Equalization ---------------- #
def Histogram_Equalization():
    # read image
    img = cv2.imread("input_image.jpg")
    # convert to gray scale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Histogram Equalization
    equ = cv2.equalizeHist(gray_img)

    # calculate histogram
    ori_hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
    equ_hist = cv2.calcHist([equ],[0],None,[256],[0,256])

    # show the result
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.plot(ori_hist)
    plt.subplot(223), plt.imshow(equ, 'gray')
    plt.subplot(224), plt.plot(equ_hist)
    plt.xlim([0,256])

    plt.show()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_Histogram.py -i input_image.jpg

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    ## Functions
    Histogram(image)
    Partial_Histogram(image)
    Histogram_Equalization()



# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
