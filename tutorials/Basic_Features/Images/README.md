# What is Image

In computer vision perspective, image(digital image) is a numeric representation, contains a fixed number of pixels. Pixels are the smallest individual element in an image and each pixel has it's location (x, y) and channel value. The image shape should be " weidth x height x channels".
- Color image has three channel, RGB (Red, Green, Blue), different method has different RGB order.
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

The main library you need to install before starting ( [Full code in notebook](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Features/Images/Images.ipynb))

```
pip install opencv-contrib-python
pip install jupyter notebook
pip install matplotlib
```

### 1. Read Image

#### - Use function cv2.imread("Argument_1", Argument_2) to read an image. 

- Argument_1: an image name in the working directory or full image path (String)        

- Argument_2:
  - cv2.IMREAD_COLOR:      Loads a color image.
  - cv2.IMREAD_GRAYSCALE:  Loads image in grayscale mode. 
  - cv2.IMREAD_UNCHANGED:  Loads image as such including alpha channel.
```
Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
```

### 2. Display image using openCV library

#### - Use function cv2.imshow("Argument_1", Argument_2) to display an image.

- Argument_1: image window name (String)

- Argument_2: pass your image into the function
```
Function You Should Know: 

  - cv2.waitKey(): a keyboard binding function. Its argument is the time in milliseconds. 
                   If 0 is passed, it waits indefinitely for a key stroke.
  - cv2.destroyAllWindows() simply destroys all the windows we created.
```

### 3. Display image using matplotlib

#### - Use function pyplot.imshow(Argument_1) to display an image.
- Argument_1: pass your image into the function

```
Note: import pyplot from matplotlib and add " %matplotlib inline " to show image on jyputer notebook
```

### 4. Save or Write image

#### - Use function cv2.imwrite("Argument_1", Argument_2) to save an image.

- Argument_1: image name, ex: my_image_name.jpg

- Argument_2: pass your image into the function
```
Note: The image will save under your work directory
```

## Code
- [Full code in jupyter notebook](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Features/Images/Images.ipynb)
- [Full code in python file] (empty)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* Matplotlib: https://matplotlib.org/api/pyplot_api.html
* Wiki: https://en.wikipedia.org/wiki/Digital_image

