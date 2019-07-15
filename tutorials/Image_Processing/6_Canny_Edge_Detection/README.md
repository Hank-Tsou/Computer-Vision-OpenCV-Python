# Canny Edge Detection

## Step:
- Noise Reduction

### Step 1. Noise Reduction
Noise will effect the accuracy of the result, so the first step of canny edge detection is to reduce noise by using 5x5 Gaussian filter. [(see Image Filtering)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/4_Image_Filtering)

### Step 2. Find Intensity Gradient (magnitude) and Orientation of the Image
(a) Use Sobel kernel in both horizontal and vertical direction to get first derivative of both direction. 
(b) Then we can find edge gradient and direction for each pixel with the two result image.
The equation is as follow:


### Step 1. Noise Reduction
### Step 1. Noise Reduction
### Step 1. Noise Reduction

```
- Input image: chess_board.png
- Command Line: python Image_Gradient.py -i chess_board.png
```
To be more graphical. An edge is shown by the “jump” in intensity in the plot below:
(It shows more clearly if we take the first derivative on f(t))

![](README_IMG/thresh.png)

```
NOTE: we can find an edge by calculate pixel locations where the gradient is higher than its 
neighbors (or to generalize, higher than a threshold).
```

![](README_IMG/canny_edge.png)

## Code
- [Canny Edge Detection](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/6_Canny_Edge_Detection)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

