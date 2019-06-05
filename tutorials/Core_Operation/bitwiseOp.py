
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 6/4/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""---------------------------------------------
-- Combine two images using bitwise mmethod
---------------------------------------------"""

import cv2
import argparse

# -------------------------- bitwise top left -------------------------- #
# Function of using bitwise operation to combine two images
# put on the top left
def image_blending_bitwise_topLeft(image, ontop):
    # resize the ontop image and crop the top left background image
    ontop = cv2.resize(ontop, (200, 200), interpolation=cv2.INTER_CUBIC)
    roi = image[0:200, 0:200]

    # convert ontop image to grayscale inorder to generate the mask
    ontop_gray = cv2.cvtColor(ontop, cv2.COLOR_BGR2GRAY)

    # mask generate by using binary threshold
    _, mask = cv2.threshold(ontop_gray, 150, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # background image: image without ontop region(black)
    backGround = cv2.bitwise_and(roi, roi, mask = mask)
    # foreground image: ontop image without background region(black)
    foreGround = cv2.bitwise_and(ontop, ontop, mask = mask_inv)

    # combine two images
    dst = cv2.add(backGround, foreGround)
    # put the result region back to background image
    image[0:200, 0:200] = dst

    cv2.imshow("result", image)
    cv2.imwrite("topleft.jpg", image)

    cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()

# -------------------------- bitwise middle -------------------------- #
# Function of using bitwise operation to combine two images
# put in the middle
def image_blending_bitwise_middle(image, ontop):

    # resize ontop image to be same as background image
    ontop = cv2.resize(ontop, (481, 359), interpolation=cv2.INTER_CUBIC)

    # convert ontop image to grayscale inorder to generate the mask
    ontop_gray = cv2.cvtColor(ontop,cv2.COLOR_BGR2GRAY)

    # mask generate by using binary threshold
    _, mask = cv2.threshold(ontop_gray, 150, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)


    # background image: image without ontop region(black)
    backGround = cv2.bitwise_and(image, image, mask = mask)
    # foreground image: ontop image without background region(black)
    foreGround = cv2.bitwise_and(ontop, ontop, mask = mask_inv)
    # combine two images
    dst = cv2.add(backGround,foreGround)

    cv2.imshow("result", dst)
    cv2.imwrite("middle.jpg", dst)


    cv2.waitKey(0)
    # if k == 27:
    #     cv2.destroyAllWindows()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read input from terminal
    # command line >> python bitwiseOp.py --image dog.jpg --ontop opencv.png
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-o", "--ontop", required=True, help="Path to the ontop image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])
    ontop = cv2.imread(args["ontop"])

    # bitwise image blending
    # image_blending_bitwise_middle(image, ontop)
    image_blending_bitwise_topLeft(image, ontop)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/3.1.0/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36
# ( Ctr Find fucntion "bitwise" )
