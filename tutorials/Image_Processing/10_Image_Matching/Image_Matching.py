
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/22/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""--------------------
- Template Matching
--------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# ------------------- Function to do template matching ------------------- #
# (1) command line >> python Image_Matching.py -i brain.jpg -t target.jpg

def template_matching(img, target):
    # convert to grayscale image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    # copy image in order to compare with different method
    img2 = img.copy()
    w, h = target.shape[::-1]

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    # do template matching with different method
    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,target,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # get the rectangle information
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # draw the match region
        cv2.rectangle(img,top_left, bottom_right, 255, 2)

        # show the result
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()

# ------- Function to do multi template matching ------- #
# (2) command line >> python Image_Matching.py -i cell.jpg -t cell_target.jpg

def multi_matching(img_rgb, target):
    # convert to grayscale image
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    w, h = target.shape[::-1]

    # Apply template Matching
    res = cv2.matchTemplate(img_gray,target,cv2.TM_CCOEFF_NORMED)
    # Set threshold
    threshold = 0.9
    loc = np.where( res >= threshold)
    # Draw the match region
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # show the result
    plt.subplot(121),plt.imshow(target)
    plt.title('target'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_rgb)
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

    plt.show()


# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_Matching.py -i brain.jpg -t target.jpg
    # (2) command line >> python Image_Matching.py -i cell.jpg -t cell_target.jpg

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-t", "--target", required=True, help="Path to the input target")
    args = vars(ap.parse_args())

    # Read image and target(template)
    image = cv2.imread(args["image"])
    target = cv2.imread(args["target"])

    ## Functions (NOTE: different input image and target, see command line (1)(2))
    template_matching(image, target)
    # multi_matching(image, target)



# Reference:
# Website: OpenCV-Python Document
# Link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
