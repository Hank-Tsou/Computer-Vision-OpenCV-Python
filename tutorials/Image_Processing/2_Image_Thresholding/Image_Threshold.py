
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/2/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""----------------------------------------
- Simple thresholding   (sim_thresh())
- Adaptive thresholding (ada_thresh())
- Otsu’s thresholding   (otsu_thresh())
----------------------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt # use to show the result

# ------------------- Function to do simple thresholding ------------------- #
def sim_thresh(img):
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    # if src(x,y) > thresh
    #   dst(x,y) = maxValue
    # else
    #   dst(x,y) = 0

    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    # if src(x,y) > thresh
    #   dst(x,y) = 0
    # else
    #   dst(x,y) = maxValue

    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    # if src(x,y) > thresh
    #   dst(x,y) = thresh
    # else
    #   dst(x,y) = src(x,y)

    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    # if src(x,y) > thresh
    #   dst(x,y) = src(x,y)
    # else
    #   dst(x,y) = 0

    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    # if src(x,y) > thresh
    #   dst(x,y) = 0
    # else
    #   dst(x,y) = src(x,y)

    ## Show the images using matplotlib
    titles = ['Origin','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()

# ------------------- Function to do adaptive thresholding ------------------- #
def ada_thresh(img):
    # simple threshold for compare
    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # thresh value using the mean of neighbourhood area
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    # thresh value using the weighted sum of neighbourhood values by gaussian filter
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    ## Show the images using matplotlib
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

# -------------- Function to do Otsu’s Binarization thresholding -------------- #
def otsu_thresh(img):
    # simple thresholding for compare
    ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # Otsu's thresholding
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    ## show all the images and their histograms
    images = [img, 0, th1,img, 0, th2]
    titles = ['Original Noisy Image','Histogram','Global Thresholding',
              'Original Noisy Image','Histogram',"Otsu's Thresholding"]
    for i in range(2):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line for sim and ada >> python Image_threshold.py -i thresh.jpg
    # (2) command line for otsu >> python Image_threshold.py -i noise.png
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # should input grayscale imge for thresholding

    # Functions, the input image should be grayscale image
    # sim_thresh(image)
    # ada_thresh(image)
    otsu_thresh(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
