
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/2/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-----------------------------------------
- Changing Color Space for an image
  * (function: RGB_to_Gray(), RGB_to_HSV())

- Extract specific color object
  * (function: extract_obj())
-----------------------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse

# ----- Function to convert RGB imge to grayscale image ----- #
def RGB_to_Gray(img):
    Gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("grayscale.png", Gray_img)

    # cv2.imwrite('gray_'+args["image"], Gray_img) # save image
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# ----- Function to convert RGB imge to HSV image ----- #
def RGB_to_HSV(img):
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV.png", HSV_img)

    # cv2.imwrite('gray_'+args["image"], Gray_img) # save image
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# ----- Function to extact object by color ----- #
def extract_obj(img):
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Get only blue region
    mask = cv2.inRange(HSV_img, lower_blue, upper_blue)

    # Bitwise-AND use mask to extract blue region
    obj = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow("obj.png", obj)                    # show result image
    # cv2.imshow("mask.png", mask)                # show mask image
    # cv2.imwrite('gray_'+args["image"], obj_img) # save image

    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # command line >> python Changing_Colorspace.py -i opencv.png
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    # Functions, will automatically show the three result images one by one. 
    RGB_to_Gray(image)
    RGB_to_HSV(image)
    extract_obj(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
