
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/14/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-------------------------------------------------
- Sobel and Scharr Derivatives
- Laplacian Derivatives
--------------------------------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# ------------------- Function to do Image Gradient ------------------- #
def Image_Gradient(img):
    # Laplacian Derivatives
    laplacian = cv2.Laplacian(img,cv2.CV_64F)

    # Sobel Derivatives
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    # Scharr Derivatives
    Scharrx = cv2.Scharr(img, -1, 1, 0)
    Scharry = cv2.Scharr(img, -1, 0, 1)

    # show result images
    plt.subplot(2,4,2),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,3),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,5),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,6),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,7),plt.imshow(Scharrx,cmap = 'gray')
    plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,4,8),plt.imshow(Scharry,cmap = 'gray')
    plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])

    plt.show()


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_Gradient.py -i chess_board.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image and convert to grayscale image
    image = cv2.imread(args["image"])
    Grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ## Functions
    Image_Gradient(Grayscale_image)




# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
