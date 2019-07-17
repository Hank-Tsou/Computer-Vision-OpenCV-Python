
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/17/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-----------------
- Image Contours
-----------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# ------------------- Function to find image moment ------------------- #
def moment(cnt):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print ("* Center of the contour: (" + str(cx) + ", " + str(cy) + ")")

# ------------------- Function to find contour's area and perimeter------------------- #
def Area_Perimeter(cnt):
    # Contour Area
    area = cv2.contourArea(cnt)
    print ("* Area of the contour: " + str(area) + " pixels")

    # Contour Perimeter
    perimeter = cv2.arcLength(cnt,True)
    print ("* Perimeter of the contour: " + str(perimeter) + " pixels")

# ------------------- Function to find image approximation contour ------------------- #
def approximation(image, cnt):
    # image contours
    temp_Image = image.copy()
    contour_img = cv2.drawContours(temp_Image, cnt, -1, (0, 255, 0), 3)

    # approximation contours
    temp_Image = image.copy()
    epsilon = 0.02*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    approx_img = cv2.drawContours(temp_Image, [approx], -1, (255, 0, 0), 3)

    # show result image
    plt.subplot(121),plt.imshow(contour_img)
    plt.title('contour_img'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(approx_img)
    plt.title('approx_img'), plt.xticks([]), plt.yticks([])

    plt.show()

# ------------------- Function to find image convex hull ------------------- #
def convex_Hull(image, cnt):
    temp_Image = image.copy()

    # Convex Hull
    hull = cv2.convexHull(cnt)
    hull_img = cv2.drawContours(temp_Image, [hull], -1, (255, 0, 0), 3)

    # show result image
    plt.subplot(111),plt.imshow(hull_img)
    plt.title('hull_img'), plt.xticks([]), plt.yticks([])

    plt.show()

# ------------------- Function to find target bonding box ------------------- #
def bonding_box(image, cnt):
    # Straight bonding box
    temp_Image = image.copy()
    x,y,w,h = cv2.boundingRect(cnt)
    bonding_box = cv2.rectangle(temp_Image,(x,y),(x+w,y+h),(0,255,0),3)

    # Rotated bonding box
    temp_Image = image.copy()
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    bonding_box_2 = cv2.drawContours(temp_Image,[box],0,(0,255,0),3)

    # show result image
    plt.subplot(121),plt.imshow(bonding_box)
    plt.title('bonding_box'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(bonding_box_2)
    plt.title('bonding_box_2'), plt.xticks([]), plt.yticks([])

    plt.show()

# ------------------- Function to find enclosing circle for the object ------------------- #
def enclosing_circle(image, cnt):
    # Enclosing Circle
    temp_Image = image.copy()
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    circle_img = cv2.circle(temp_Image,(int(x),int(y)),int(radius),(0,255,0),3)

    # Fitting an Ellipse
    temp_Image = image.copy()
    ellipse = cv2.fitEllipse(cnt)
    ellipse_img = cv2.ellipse(temp_Image,ellipse,(0,255,0),3)

    # show result image
    plt.subplot(121),plt.imshow(circle_img)
    plt.title('circle_img'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(ellipse_img)
    plt.title('ellipse_img'), plt.xticks([]), plt.yticks([])

    plt.show()

# ------------------- Function to find 4 extreme points ------------------- #
def extreme_points(image, cnt):
    temp_Image = image.copy()

    # get extreme points
    leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
    rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
    bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

    # draw points
    cv2.circle(temp_Image, leftmost, 6, (0, 0, 255), -1)
    cv2.circle(temp_Image, rightmost, 6, (0, 255, 0), -1)
    cv2.circle(temp_Image, topmost, 6, (255, 0, 0), -1)
    cv2.circle(temp_Image, bottommost, 6, (255, 255, 0), -1)

    # show result image
    plt.subplot(111),plt.imshow(temp_Image)
    plt.title('extreme_points'), plt.xticks([]), plt.yticks([])

    plt.show()


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Contour_Feature.py -i feature.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])
    # convert to grayscale image
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # apply image threshold to define the target area
    ret,thresh = cv2.threshold(gray_img,250,255,cv2.THRESH_BINARY)
    # find contours
    _,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = contours[0]

    ## Functions:
    moment(cnt)
    Area_Perimeter(cnt)
    approximation(image, cnt)
    convex_Hull(image, cnt)
    bonding_box(image, cnt)
    enclosing_circle(image, cnt)
    extreme_points(image, cnt)



# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
