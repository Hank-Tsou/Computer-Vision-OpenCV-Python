
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/23/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""------------------------
- Hough Circle Transform
-------------------------"""

import numpy as np
import argparse
import cv2

# ---------------- Function to do Hough Circle Transform ---------------- #
def Hough_Circle_Transform(image, gray):
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,
                                param1=100,param2=10,minRadius=10,maxRadius=15)

    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python hough_circle_transform.py -i pool.jpg

    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required = True, help = "Path to source image")
    args = vars(ap.parse_args())

    # read image and convert to grayscale image
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Function
    Hough_Circle_Transform(image, gray)
