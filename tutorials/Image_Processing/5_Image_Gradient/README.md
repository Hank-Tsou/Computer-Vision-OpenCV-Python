# Image Gradient
Use image gradient to get edge in an image, on edges the pixel intensity changes. So we use derivative to express these kind of changes.

## Outline:
- Sobel Derivatives 
- Scharr Derivatives
- Laplacian Derivatives

### 1. Image Gradient
```
- Input image: chess_board.png
- Command Line: python Image_Gradient.py -i chess_board.png
```

#### a. Sobel Derivatives 
```
Function: 
```
```python
NOTE: 
  - Use numpy to generate kernel (Filter)
    kernel = np.ones(kernel_size, np.float32)
```
```
Below is how convolution filter work on an image:
```
![](README_IMG/conv_filter.gif)

#### b. Scharr Derivatives
```
Function: 
```
```
The function using kernel:

K = 1/(kernel_width * kernel_height) * np.ones(kernel_size, np.float32) [opecv-python documentation]
```
#### c. Laplacian Derivatives
```
Function: 
```
![](README_IMG/Gaussian_filter.png)






## Code
- [Image Gradient](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/5_Image_Gradient/Image_Gradient.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (sobel & laplacian) https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html?highlight=scharr%20derivatives
