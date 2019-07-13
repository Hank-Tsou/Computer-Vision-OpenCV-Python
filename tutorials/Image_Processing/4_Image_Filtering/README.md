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
```python
NOTE: 
  - Use numpy to generate kernel
    kernel = np.ones(kernel_size, np.float32)
```
#### b. Averaging Filtering

#### c. Gaussian Filtering

#### d. Median Filtering

#### e. Bilateral Filtering

## Code
- [Image Filtering](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/4_Image_Filtering/Image_filtering.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (threshold) Link: https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
