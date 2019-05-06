
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/6/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""------------------------------------
- ROI selection and save roi_image
------------------------------------"""

# Import OpenCV Library and command line interface
import cv2
import argparse

# --------------- Function for ROI Selection --------------- #

def ROI_selection(image):

    # Select ROI
    r = cv2.selectROI(image)
    print("(x, y, width, height) = ", r) # print the return information

    # Get roi region
    ROI_img = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    cv2.imshow("Image", ROI_img) # show image
    # cv2.imwrite('ROI_'+args["image"], ROI_img) # save image

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read input from terminal
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    # function for ROI selection
    ROI_selection(image)



# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/3.1.0/d1/d18/structcv_1_1ROISelector_1_1handlerT.html
