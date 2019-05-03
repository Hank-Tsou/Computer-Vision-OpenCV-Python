
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/3/2019                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#


"""------------------
1. Read Video from file
2. Read video from webcam
3. Display video
4. Save Video
------------------"""

# Import OpenCV Library
import numpy as np
import cv2

# --------------------- Read video --------------------- #

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
