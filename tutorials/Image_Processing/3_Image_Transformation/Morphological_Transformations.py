
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/10/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""--------------------------------
- Morphological Transformations
    - Image erosion
    - Image dilation
- Function morphologyEx
    - six different method
---------------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

def Morphological_Transformations(img):
    # 6 by 6 kernel
    kernel = np.ones((6,6),np.uint8)
    erosion = cv2.erode(img, kernel, iterations = 2)
    dilation = cv2.dilate(img, kernel, iterations = 2)

    # show result images
    plt.subplot(131),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(erosion),plt.title('erosion')
    plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(dilation),plt.title('dilation')
    plt.xticks([]), plt.yticks([])

    plt.show()

def morphologyEx(img):
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

    # show result images
    plt.subplot(231),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232),plt.imshow(opening),plt.title('opening')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233),plt.imshow(closing),plt.title('closing')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234),plt.imshow(gradient),plt.title('gradient')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235),plt.imshow(tophat),plt.title('tophat')
    plt.xticks([]), plt.yticks([])
    plt.subplot(236),plt.imshow(blackhat),plt.title('blackhat')
    plt.xticks([]), plt.yticks([])
    plt.show()
# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Morphological_Transformations.py -i morpho_img.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    # Functions
    Morphological_Transformations(image)
    morphologyEx(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#void%20filter2D(InputArray%20src,%20OutputArray%20dst,%20int%20ddepth,%20InputArray%20kernel,%20Point%20anchor,%20double%20delta,%20int%20borderType)
