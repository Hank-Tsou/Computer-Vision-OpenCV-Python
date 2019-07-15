# Image Gradient
Use image gradient to find edges in an image, in an edge the pixel intensity changes or a sharp change in color. So we use derivative to express these kind of changes.

## Outline:
- Sobel Derivatives 
- Scharr Derivatives
- Laplacian Derivatives

### 1. Image Gradient
```
- Input image: chess_board.png
- Command Line: python Image_Gradient.py -i chess_board.png
```
To be more graphical. An edge is shown by the “jump” in intensity in the plot below:
(It shows more clearly if we take the first derivative on f(t))

![](README_IMG/conv_filter.gif)

```
NOTE: we can find an edge by calculate pixel locations where the gradient is higher than its 
neighbors (or to generalize, higher than a threshold).
```
#### a. Sobel Derivatives 
```python
Function: sobel = cv2.Sobel(src_img, ddepth, dx, dy, ksize)
  - ddepth: The depth of the output image. We set it to cv2.CV_64F to avoid overflow.
```

Sobel Operator combines Gaussian smoothing and differentiation. It computes an approximation of the gradient by placing the gradient matrix over each pixel of an image. 

```
Below is how convolution filter work on an image:

* Assume 'I' is an image matrix

                              [-1 0 +1]                                    [-1 -2 -1]
Horizontal changes: result =  [-2 0 +2] * I    Vertical changes: result =  [ 0  0  0] * I  
                              [-1 0 +1]                                    [+1 +2 +1]
```

NOTE: Use function cv2.addWeighted() to combine two result. [(Image Blending)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation) [(Code)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_blending.py)

![](README_IMG/conv_filter.gif)

#### b. Scharr Derivatives
```
Function: Scharr = cv2.Scharr(src_img, ddepth, dx, dy)
  - ddepth: The depth of the output image. Here we set to -1.
```
```
This is as fast but "more accurate" than the standard Sobel function. It implements the following kernels:

* Assume 'I' is an image matrix

                              [-3  0 +3 ]                                    [-3 -10 -3]
Horizontal changes: result =  [-10 0 +10] * I    Vertical changes: result =  [ 0   0  0] * I  
                              [-3  0 +3 ]                                    [+3 +10 +3]
```

NOTE: Use function cv2.addWeighted() to combine two result. [(Image Blending)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation) [(Code)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_blending.py)

![](README_IMG/conv_filter.gif)

#### c. Laplacian Derivatives
```
Function: laplacian = cv2.Laplacian(src_img, ddepth)
  - ddepth: The depth of the output image. We set it to cv2.CV_64F to avoid overflow.
```
We can observe the figure below, the second derivative on an edge is zero. So, we can also use this criterion to attempt to detect edges in an image. 

![](README_IMG/Gaussian_filter.png)


## Code
- [Image Gradient](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/5_Image_Gradient/Image_Gradient.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (sobel & laplacian) https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html?highlight=scharr%20derivatives
