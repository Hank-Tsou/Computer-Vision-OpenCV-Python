
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/6/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-------------------------------------
- Image Blending, combine two images
-------------------------------------"""

# Import OpenCV Library and command line interface
import cv2
import argparse

# ----- Function for image blending using addWeight ----- #
def imageBlending(image_1, image_2):

    # Using add weight to do image blending
    dst = cv2.addWeighted(image_1,0.3,image_2,0.7,0)

    # show result image
    cv2.imshow('dst',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read two input from terminal
    # command line >> python image_blending.py --image dog.jpg --ontop moon.jpg
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-o", "--ontop", required=True, help="Path to the ontop image")
    args = vars(ap.parse_args())

    # Read image
    image_1 = cv2.imread(args["image"])
    image_2 = cv2.imread(args["ontop"])

    # image blending
    imageBlending(image_1, image_2)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/3.1.0/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36
# ( Ctr Find fucntion "addWeighted" )
