
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/17/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""------------------
- Image Contours
------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

def draw_points(image, contours):
    temp_Image = np.zeros(image.shape,np.uint8)
    temp_Image = image.copy()
    for i in range(len(contours)):
        for p in range(len(contours[i])):
            cv2.circle(temp_Image,(contours[i][p][0][0], contours[i][p][0][1]), 2, (255, 0, 0), -1)

    return temp_Image

# ------------------- Function to find image contours ------------------- #
def Image_Contour(image):
    # convert to grayscale image
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # apply threshold for the image
    ret,thresh = cv2.threshold(gray_img,250,255,cv2.THRESH_BINARY_INV)

    # find contours
    _, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour_img_1 = draw_points(image, contours)
    _, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contour_img_2 = draw_points(image, contours)

    # draw contours
    contour_img = cv2.drawContours(image, contours, -1, (255,0,0), 3)

    # show result (should trun the screen brighter to see the result)
    plt.subplot(131),plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
    plt.title('draw Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(cv2.cvtColor(contour_img_1, cv2.COLOR_BGR2RGB))
    plt.title('simple Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(cv2.cvtColor(contour_img_2, cv2.COLOR_BGR2RGB))
    plt.title('contours Image'), plt.xticks([]), plt.yticks([])

    plt.show()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_Contours.py -i shapes.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    ## Functions
    Image_Contour(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_pyramids/py_pyramids.html
