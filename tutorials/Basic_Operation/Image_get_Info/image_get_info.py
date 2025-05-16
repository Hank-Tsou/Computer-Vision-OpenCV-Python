
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/4/2020                   #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""---------------------------------
1. Get image information
---------------------------------"""

# Import OpenCV Library
import cv2

# Load a color image
img = cv2.imread("test.jpg")

print("\n-------- image information --------")

# ----------- Image property information ----------- #
image_shape = img.shape  # image shape
image_size = img.size    # image size
image_dtype = img.dtype  # image data type

print("\nimage property")
print(" -image_shape:\t", image_shape)
print(" -image_size:\t", image_size)
print(" -image_dtype:\t", image_dtype)
print("\n-----------------------------------")

# ---------------- Image pixel value ---------------- #
# pixel location ( x, y )
x = 200
y = 100

pixel_value = img[ x, y ]
pixel_value_B = img[ x, y, 0 ] # BLUE channel value
pixel_value_G = img[ x, y, 1 ] # Green channel value
pixel_value_R = img[ x, y, 2 ] # Red channel value

print("\nimage pixel information")
print(" -pixel value at (300, 150): ", pixel_value)
print(" -Blue  value at (300, 150): ", pixel_value_B)
print(" -Green value at (300, 150): ", pixel_value_G)
print(" -Red   value at (300, 150): ", pixel_value_R)

img[ x, y ] = [0, 0, 0]
pixel_value_B = img[ x, y, 0 ]
pixel_value_G = img[ x, y, 1 ]
pixel_value_R = img[ x, y, 2 ]

print("\nchange image pixel information")
print(" -pixel value at (300, 150): ", pixel_value)
print(" -Blue  value at (300, 150): ", pixel_value_B)
print(" -Green value at (300, 150): ", pixel_value_G)
print(" -Red   value at (300, 150): ", pixel_value_R)
print("\n-----------------------------------\n")



# Reference:
# Website: Opencv-Python Tutorials
# Link: https://opencv-python-tutroals.readthedocs.io/
# en/latest/py_tutorials/py_tutorials.html
