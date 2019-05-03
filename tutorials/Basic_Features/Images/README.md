# What is Image

In computer vision perspective, image is a combination of pixels, each pixel has it's location ( x, y ) and pixel value. So the image shape should be " weidth x height x channels".
- Color image has three channel, RGB (Red, Green and Blue), different method has different RGB order.
- Gray scale image only has one channel.
```
Note: it is possible for an image to have more than three channels.
```
## Getting Started with Image using OpenCV Python

### Outline:
1. Read Image
2. Display Image using OpenCV library
3. Display image using matplotlib in jupyter notebook
4. Save Image

### Prerequisites

The main library you need to install before starting

```
pip install opencv-contrib-python
pip install jupyter notebook
pip install matplotlib
```

### Read Image

#### Function: Use function cv2.imread(Argument_1, Argument_2) to read an image. 

- Argument_1: an image name in the working directory or full image path           

- Argument_2:
  - cv2.IMREAD_COLOR:      Loads a color image.
  - cv2.IMREAD_GRAYSCALE:  Loads image in grayscale mode. 
  - cv2.IMREAD_UNCHANGED:  Loads image as such including alpha channel.
```
Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
```

### Display image using openCV library

#### Function: Use function cv2.imshow(Argument_1, Argument_2) to display an image.

- Argument_1: image window name

- Argument_2: pass your image into the function
```
Function You Should Know: 
  - cv2.waitKey(): a keyboard binding function. Its argument is the time in milliseconds. 
                   If 0 is passed, it waits indefinitely for a key stroke.
  - cv2.destroyAllWindows() simply destroys all the windows we created.
```

### Display image using matplotlib

#### Function: Use function imshow(Argument_1) to display an image.
- Argument_1: pass your image into the function

```
# import pyplot from matplotlib and add second line in order to show image on jyputer notebook

from matplotlib import pyplot as plt
%matplotlib inline 
```

### Save or Write image

#### Function: Use function imwrite(Argument_1, Argument_2) to display an image.

- Argument_1: image name, ex: my_image.jpg

- Argument_2: pass your image into the function
```
Note: The image will save under your work directory
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* Matplotlib: https://matplotlib.org/api/pyplot_api.html

