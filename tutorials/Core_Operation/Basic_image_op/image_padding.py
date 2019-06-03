
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 6/3/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""------------------
- image padding
------------------"""

# Import OpenCV Library and command line interface
import cv2
import argparse
from matplotlib import pyplot as plt

# --------------- Function for image padding --------------- #
def image_padding(img1):

    BLUE = [255,0,0]

    # Replicate: repeat the last pixel value
    replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
     # |             +|+++|
     # |            +*|***|
     # |           +--|---|
     # |______________|___|
     #     original    padding

    # Reflect: reflect the boarder
    reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
    # |             +|+  |
    # |            +*|*+ |
    # |           +--|--+|
    # |______________|___|
    #     original    padding

    # Wrap: connect origial image then crop the boarder
    wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
     #    |  +|--             +|--|
     #    | +*|+             +*|+ |
     #    |+--|==           +--|==|
     #    |___|________________|__|
     # padding     original     padding

    # Constant: A constant colored border
    constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
    # |             +|BLUE|
    # |            +*|BLUE|
    # |           +--|BLUE|
    # |______________|BLUE|
    #     original    padding

    # show padding result by using plt
    plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.subplot(234),plt.imshow(wrap,'gray'),plt.title('WRAP')
    plt.subplot(235),plt.imshow(constant,'gray'),plt.title('CONSTANT')

    plt.show()

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read input from terminal
    # command line >> python image_ROI.py --image padding_source.png.png
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    # image padding
    image_padding(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/3.1.0/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36
# ( Ctr Find fucntion "copyMakeBorder" )
