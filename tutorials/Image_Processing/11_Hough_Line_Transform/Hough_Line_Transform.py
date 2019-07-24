
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/23/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""----------------------
- Hough Line Transform
----------------------"""

from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# ---------------- Function to do Hough Line Transform ---------------- #
def Hough_Line(image, edges):
    img = image.copy()

    # Hough Line Transform
    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    # Draw all the line on the image
    for i in range(0, len(lines)):
        for rho,theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    # show result
    plt.subplot(111), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# ---------------- Function to do Probabilistic Hough Line Transform ---------------- #
def P_Hough_Line(image, edges):
    img = image.copy()

    # Probabilistic Hough Transform
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

    # Draw all the line on the image
    for i in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    # show result
    plt.subplot(111), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Hough_Line_Transform.py -i pool.jpg

    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required = True, help = "input image source path")
    args = vars(ap.parse_args())

    # read image
    image = cv2.imread(args["image"])
    # convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # get edges by using "Canny edge detection"
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    # Functions
    # Hough_Line(image, edges)
    # P_Hough_Line(image, edges)
    # show result
    cv2.imshow("edge", gray)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html#hough-lines
