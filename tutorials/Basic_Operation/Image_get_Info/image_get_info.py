
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 5/4/2019                   #
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
pixel_value_B = img[ x, y, 0 ] # BLUE channel
pixel_value_G = img[ x, y, 1 ] # Green channel
pixel_value_R = img[ x, y, 2 ] # Red channel

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
print("\n-----------------------------------")

# ----- Pixel accessing and editing using Numpy ----- #

pixel_value_B = img.item(x, y, 0)
pixel_value_G = img.item(x, y, 1)
pixel_value_R = img.item(x, y, 2)

print("\nimage pixel information (Numpy: array.item())")
print(" -Blue  value at (300, 150): ", pixel_value_B)
print(" -Green value at (300, 150): ", pixel_value_G)
print(" -Red   value at (300, 150): ", pixel_value_R)

img.itemset((x,y,0),122) # change blue channel value
img.itemset((x,y,1),245) # change green channel value
img.itemset((x,y,2),140) # change red channel value

print("\nchange image pixel information (Numpy: array.itemset())")
print(" -pixel value at (300, 150): ", img[x, y])
print("\n-----------------------------------\n")



# Reference:
# Website: Opencv-Python Tutorials
# Link: https://opencv-python-tutroals.readthedocs.io/
# en/latest/py_tutorials/py_tutorials.html
