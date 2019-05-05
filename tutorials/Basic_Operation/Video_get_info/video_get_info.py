
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/4/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""---------------------------------
1. Get video information
---------------------------------"""

# Import OpenCV Library
import cv2

# -------------------- Get Video source --------------------- #
# NOTE: "cat.mp4" is in video_IO or input your video source

# get video source from video file
cap = cv2.VideoCapture("cat.mp4")

# get video source from webcam
# cap = cv2.VideoCapture(0)

# ----------------------------------------------------------- #

print("\ncheck video capture: ", cap.isOpened())

# ------------------ Get Video information ------------------ #

if(cap.isOpened()):
    print("\n-------- video information --------")
    print("frame width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("frame width: ", cap.get(3))

    print("frame height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("frame height: ", cap.get(4))

    print("Total number of frames: ", cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total number of frames: ", cap.get(7))

    print("FPS: ", cap.get(cv2.CAP_PROP_FPS))
    print("FPS: ", cap.get(5))
    print("-----------------------------------")

# ---------------------------------------------------------- #



# Reference:
# Website: Opencv-Python Tutorials
# Link: https://opencv-python-tutroals.readthedocs.io/
# en/latest/py_tutorials/py_tutorials.html
