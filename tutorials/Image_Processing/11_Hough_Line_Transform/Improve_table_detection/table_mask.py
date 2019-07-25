
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/25/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-----------------------------------------
Improve hough line transform on pool tabke
------------------------------------------"""
"""
Improvement: Use target mask to select the target, function table_selection(), largest_contours()
"""

import numpy as np # use numpy library as np for array object
import cv2 # opencv-python

# segment the pool table used color information
def table_selection(ts_image):
    boundaries = [ ([60, 60, 0], [190, 150, 35])] # color boundary for the pool table

    # create NumPy arrays from the boundary
    for (lower, upper) in boundaries:
    	lower = np.array(lower, dtype = "uint8")
    	upper = np.array(upper, dtype = "uint8")

    	ts_mask = cv2.inRange(ts_image, lower, upper) # create the mask for the selected region
    	result = cv2.bitwise_and(ts_image, ts_image, mask = ts_mask) # remain only the pool table

    return result, ts_mask # return table selection and mask

# Canny Edge Detection
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert image in to grayscale
    gray = cv2.GaussianBlur(gray,(3, 3),0) # use gaussian blur
    edged = cv2.Canny(gray,50,150,apertureSize = 3) # Canny Edge Detection
    return edged # return edge image

# Hough Lines Detection (with "cv2.HoughLines")
def hough_line(image, edge_img):
    # Call function "cv2.HoughLines" and adjust the parameter for the function
    line = cv2.HoughLines(edge_img,rho=2,theta=np.pi/180, threshold=150)
    p, q, r = line.shape
    # calsulate the line point use "theta" and "rho" value

    # Parameters ---------------------------------------------#
    # rho – Distance resolution of the accumulator in pixels. #
    # theta – Angle resolution of the accumulator in radians. #
    #---------------------------------------------------------#

    for i in range(p): # calculate points for each line and draw the four lines
        for rho,theta in line[i]:
            a, b = np.cos(theta), np.sin(theta)              # calculate slop scale
            x, y = a*rho, b*rho                            # calculate one point (x0, y0) on the line
            x1, y1 = int(x + 600*(-b)), int(y + 600*(a))   # calculate two end points of the line
            x2, y2 = int(x - 1500*(-b)), int(y - 1500*(a)) # calculate two end points of the line

            cv2.line(image,(x1,y1),(x2,y2),(0,255,255),1) # draw line on the image

    return image # return image with four lines for the pool table

# select the largest pool table
def largest_contours(ori_image, lc_image, lc_mask):
    ret,thresh = cv2.threshold(lc_mask, 40, 255, 0) # convert the mask image into black and white

    # find contours
    im,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0: # if has contour
        c = max(contours, key = cv2.contourArea) # find the largest contour area

    mask = np.zeros(ori_image.shape, dtype='uint8') # create a empty mask
    mask = cv2.drawContours(mask, [c], -1, (225,225,225), -1) # create a mask for the largest pool table

    gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) # convert the mask into grayscale
    output = cv2.bitwise_and(ori_image, ori_image, mask=gray) #create the image only the largest pool table

    return output, mask # return the largest pool table image and it's mask

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # command >> python table_mask.py

    ori_image = cv2.imread('pool.jpg') # read image
    table_img, table_img_mask = table_selection(ori_image) # segment the pool table used color information
    seg_obj, obj_mask = largest_contours(ori_image, table_img, table_img_mask) # slect the largest pool table
    edge_img = edge_detection(seg_obj) # Canny Edge Detection
    line_img = hough_line(ori_image, edge_img) # Hough Lines Detection

    # show result image
    cv2.imshow("images", line_img)
    cv2.waitKey(0) # system pause, press esc to exit
