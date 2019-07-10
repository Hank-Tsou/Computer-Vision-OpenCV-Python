
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/10/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""--------------------------------
- Image scaling
- Image translation
- Image rotation
- Image transformation
    * Affine Transformation
    * Perspective Transformation
---------------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse

# ------------------- Function to do image scaling ------------------- #
def Image_scaling(img):
    # get image height(row) and width(col)
    height, width = img.shape[:2]

    # - cv2.INTER_LINEAR: bilinear interpolation
    scal_img = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_LINEAR)

    # - cv2.INTER_CUBIC: bicubic interpolation
    # scal_img = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

    # - cv2.INTER_AREA: resampling using pixel area relation.
    # scal_img = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_AREA)

    # - cv2.INTER_NEAREST: nearest neighbor interpolation
    # scal_img = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_NEAREST)

    # show result image
    cv2.imshow("scal_img", scal_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# ------------------- Function to do image translation ------------------- #
def Image_translation(img):
    # get image height(rows) and width(cols)
    rows,cols = img.shape[:2]

    # get translation matrix
    trans_Matrix = np.float32([[1,0,100],[0,1,50]]) # Right 100 pixels, Down 50 pixels

    # do image translation with matrix
    trans_img = cv2.warpAffine(img, trans_Matrix, (cols,rows))

    # show result image
    cv2.imshow('img',trans_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# -------------- Function to do image rotation -------------- #
def Image_rotation(img):
    # get image height(rows) and width(cols)
    rows,cols = img.shape[:2]

    # get rotation matrix
    rotate_Matrix = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)

    # do image rotation with matrix
    rotate_img = cv2.warpAffine(img, rotate_Matrix, (cols,rows))

    # show result image
    cv2.imshow('img',rotate_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# -------------- Function to do Affine transformation -------------- #
def Affine_transformation(img):
    # get image height(rows) and width(cols)
    rows,cols = img.shape[:2]

    # points 1 on original imgage transform to points 2 location
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])

    # get the transformation matrix from point 1 to points 2
    Matrix = cv2.getAffineTransform(pts1,pts2)

    # do image Affine transformation with matrix
    trans_img = cv2.warpAffine(img, Matrix, (cols,rows))

    # show result image
    cv2.imshow('img',trans_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# -------------- Function to do Perspective transformation -------------- #
def Perspective_transformation(img):
    # get image height(rows) and width(cols)
    rows,cols = img.shape[:2]

    # match points 1 to points 2
    pts1 = np.float32([[211,213],[575,214],[102,537],[676,538]])
    pts2 = np.float32([[0,0],[500,0],[0,500],[500,500]])

    # match points matrix
    Matrix = cv2.getPerspectiveTransform(pts1,pts2)

    # do prespective transformation with matrix
    prespec_img = cv2.warpPerspective(img, Matrix, (500,500))

    # show result image
    cv2.imshow('img',prespec_img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python Image_Transformation.py -i opencv.png
    # (2) command line >> python Image_Transformation.py -i perspect_img.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])

    ## Functions
    ## -- Input image opencv.png (first command line input) --
    Image_scaling(image)
    # Image_translation(image)
    # Image_rotation(image)

    ## -- Input image change to aff_img.jpg (second command line input) --
    # Affine_transformation(image)
    # Perspective_transformation(image)


# Reference:
# Website: OpenCV-Python Document
# Link: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
