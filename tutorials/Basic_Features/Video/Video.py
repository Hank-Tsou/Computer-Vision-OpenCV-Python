
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/3/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""---------------------------------
1. Get video source and information
2. Read source video
3. Display video
4. Save Video
---------------------------------"""

# Import OpenCV Library
import cv2

# --------------- Get Video source and basic informarion ---------------#

# get video source from video file
cap = cv2.VideoCapture("cat.mp4")

# get video source from webcam
# cap = cv2.VideoCapture(0)

# ---------------------------------------------------------------------#

print("\ncheck video capture: ", cap.isOpened())

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

#------------------- object for write a video -------------------#

# Define the codec and create VideoWriter object for save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# ------------------------- Read Video ------------------------- #

while(True):

    # Read video frame-by-frame
    ret, frame = cap.read()

    # read a video frame or not
    if(not ret):
        break

    # Write a frame image into video
    out.write(frame)

    # Display the video frame
    cv2.imshow('frame',frame)

    cv2.waitKey(10) # control the output speed

    # PRESS 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When finished, release everything
cap.release()
out.release()
cv2.destroyAllWindows()



# Reference:
# Website: Opencv-Python Tutorials
# Link: https://opencv-python-tutroals.readthedocs.io/
# en/latest/py_tutorials/py_tutorials.html
