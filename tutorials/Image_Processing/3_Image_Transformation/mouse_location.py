
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/10/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""-----------------------------------------------------------
Get mouse location on an image
    - Can use this program to help do image transformation
-----------------------------------------------------------"""

# Import OpenCV Library, command line interface
import cv2
import argparse

# ------------------- Function to get mouse location on an image ------------------- #
def get_location(event, x, y, flags, param):
    global loc_x, loc_y # location parameter
    # mouse left click --> draw dot and get location
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        loc_x = x
        loc_y = y

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # Step: (1) left click on the image location (2) press 'a' to show location on Terminal
    # command line >> python mouse_location.py -i perspect_img.png

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    args = vars(ap.parse_args())

    # Read image
    img = cv2.imread(args["image"])
    cv2.namedWindow('image')

    # function to get the location
    cv2.setMouseCallback('image',get_location)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(20)

        # Esc key to end program
        if k == 27:
            break

        # press 'a' to print the location
        elif k == ord('a'):
            print (loc_x,loc_y)

# Reference:
# Website: OpenCV-Python Document
# Link: https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv
