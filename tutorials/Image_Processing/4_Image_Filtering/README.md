# Image Filtering
Images can be filtered with various filters. "Low Pass Filter" helps in removing noise, or blurring the image. 
"High Pass Filter" helps in finding edges in an image.

## Outline:
- Image filtering (Image Blurring, Image Smoothing) ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/4_Image_Filtering/Image_filtering.py))
    - 2D convolution Filtering
    - Averaging Filtering
    - Gaussian Filtering
    - Median Filtering
    - Bilateral Filtering

### 1. Image Filtering 
```
- Input image: noise.png
- Command Line: python Image_filtering.py -i noise.png
```

#### a. 2D convolution Filtering
```
Function: conv_filtering = cv2.filter2D(src_img, ddepth, kernel)
    - ddepth: Desired depth of the destination image, here we set negative to be the same as source.
```
```python
NOTE: 
  - Use numpy to generate kernel
    kernel = np.ones(kernel_size, np.float32)
```
#### b. Averaging Filtering
```
Function: average = cv2.blur(src_img,(5,5))
```
#### c. Gaussian Filtering
```
Function: gaussian = cv2.GaussianBlur(src_img,(5,5),0)
```
#### d. Median Filtering
```
Function: median = cv2.medianBlur(src_img,5)
```
#### e. Bilateral Filtering
```
Function: bilateral = cv2.bilateralFilter(src_img,9,75,75)
```

## Code
- [Image Filtering](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/4_Image_Filtering/Image_filtering.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Filtering) Link: https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html
