
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/23/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""---------------------------------------------------
- Improve Hough Circle Transform for Ball Detection
---------------------------------------------------"""

from matplotlib import pyplot as plt
import numpy as np # use numpy library as np for array object
import cv2 # opencv-python

# segment the pool table used color information
def table_selection(image):
    boundaries = [ ([20, 15, 0], [200, 150, 35])] # color boundary for the pool table

    # create NumPy arrays from the boundary
    for (lower, upper) in boundaries:
    	lower = np.array(lower, dtype = "uint8")
    	upper = np.array(upper, dtype = "uint8")

    	mask = cv2.inRange(image, lower, upper)  # create the mask for the selected region
    	result = cv2.bitwise_and(image, image, mask = mask) # remain only the pool table

    return result # return table selection

# Canny Edge Detection
def edge_detection(image):
    gray = cv2.cvtColor(table_img, cv2.COLOR_BGR2GRAY) # convert image in to grayscale
    gray = cv2.GaussianBlur(gray,(3, 3),0) # use gaussian blur
    edged = cv2.Canny(gray,50,150,apertureSize = 3) # Canny Edge Detection
    return edged # return edge image

# find pool balls contous
def ball_contours(lc_edge, table_mask):
    # find contours
    im,contours,hierarchy = cv2.findContours(lc_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0: # if has contours
        img_contour = np.zeros(image.shape, dtype='uint8') # create a empty image for image contours
        cv2.drawContours(img_contour, contours, -1, (0,225,0), 3) # draw contours

    fat_mask = cv2.dilate(table_mask, None, iterations=15) # dilate the mask in order to select the largest table
    gray_mask = cv2.cvtColor(fat_mask, cv2.COLOR_BGR2GRAY) # convert the mask into grayscale

    target_img = cv2.bitwise_and(img_contour, img_contour, mask=gray_mask) # create the largest table image
    imgray = cv2.cvtColor(target_img,cv2.COLOR_BGR2GRAY) # convert the largest table image into grayscale

    return imgray # return grayscale target image

# Hough Circle Detection (with "cv2.HoughCircles")
def hough_circle(im, seg_obj):
    # Call function "cv2.HoughCircles" and adjust the parameter for the function
    c = cv2.HoughCircles(seg_obj,cv2.HOUGH_GRADIENT,1,20, param1=100,param2=10,minRadius=14,maxRadius=21)

    # draw circles and centers
    for i in c[0,:]:
        cv2.circle(im,(i[0],i[1]),i[2],(0,255,0),2) # draw the outer circle
        cv2.circle(im,(i[0],i[1]),2,(0,0,255),3) # draw the center of the circle

    return im # return result image

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # command >> python table_color.py
    image = cv2.imread('pool.jpg')                # read image
    table_mask = cv2.imread('obj_mask.jpg')        # read table mask create from problem 1, part a

    table_img = table_selection(image)             # segment the pool table used color information
    edge_img = edge_detection(table_img)           # Canny Edge Detection
    ball_con = ball_contours(edge_img, table_mask) # find balls contours
    circle_img = hough_circle(image, ball_con)     # hough circle find pool balls

    # show result
    plt.subplot(111), plt.imshow(cv2.cvtColor(circle_img, cv2.COLOR_BGR2RGB))
    plt.show()
