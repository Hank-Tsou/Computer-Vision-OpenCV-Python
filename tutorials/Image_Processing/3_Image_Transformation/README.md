# Image Transformation

## Outline:
- Geometric Transformations ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/3_Image_Transformation/Geometric_Transformations.py))
  - Image scaling
  - Image translation
  - Image rotation
  - Image transformation

- Morphological Transformations ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/3_Image_Transformation/Morphological_Transformations.py))
  - Image erosion
  - Image dilation
  - Function MorphologyEx()

### 1. Geometric Transformations
```
Input image: opencv.png (for scaling, translation, rotation), perspect_img.png (for transformation)

(1) command line >> python Geometric_Transformations.py -i opencv.png
(2) command line >> python Geometric_Transformations.py -i perspect_img.png
```
```
NOTE: see instruction in main part
```
#### a. Image scaling
```python
Function: scale_img = cv2.resize(src_img, output_size, method)
```
```python
Interpolation method:
   - INTER_NEAREST: a nearest-neighbor interpolation
   - INTER_LINEAR: a bilinear interpolation (used by default)
   - INTER_AREA: resampling using pixel area relation. It's a preferred method for image decimation, 
                 But when the image is zoomed, it is similar to the INTER_NEAREST method.
   - INTER_CUBIC: a bicubic interpolation over 4x4 pixel neighborhood
```
![](README_IMG/simple_thresh.png)

#### b. Image translation
```python
Function: trans_img = cv2.warpAffine(src_img, Translation_Matrix, output_size)
```
```
Translation_Matrix:
  - (x, y) = original location, (x', y') = result location

x' = x + a.     in matirx                  [ 1 0 ]  
y' = y + b.    ----------->    [x, y, 1] * [ 0 1 ]  = [x + a, y + b] = [x', y']
                                           [ a b ]
```
```python
Translation_Matrix: trans_Matrix = np.float32([[1, 0, x_moving_scale],[0, 1, y_moving_scale]])
```

![](README_IMG/simple_thresh.png)

#### c. Image rotation
```python
Function: rotate_img = cv2.warpAffine(src_img, rotation_Matrix, output_size)
```
```
Translation_Matrix:
  - (x, y): original location = (r*cos(a), y*sin(a))  
  - (x', y'): result location (rotate 'b' degree) = (r*cos(a+b), y*sin(a+b))

x' = r * cos(a+b) = r*cos(a)cos(b) - r*sin(a)sin(b) = xcos(a) - ysin(a)  
y' = r * sin(a+b) = r*sin(a)cos(b) + r*cos(a)sin(b) = xsin(a) + ycos(a)  

 in matrix                [ cos(a) -sin(a) ]
----------->   [x', y'] = [ sin(a)  cos(a) ] * [x, y]
```
```python
Rotattion_Matrix = cv2.getRotationMatrix2D(center, angle, scale)
```

#### d. Image transformation


### 2. Morphological Transformations
```
- Input image: thresh.jpg
- Command Line: python Image_threshold.py -i thresh.jpg
```
```python
Function: th = cv2.adaptiveThreshold(src_img, maxValue, adaptiveMethod, thresholdType, blockSize, C)
```
```python
Adaptive method and math description:

- cv2.ADAPTIVE_THRESH_MEAN_C:
  The threshold value T(x,y) is a mean of the blockSize x blockSize neighborhood of (x, y) minus C.

- cv2.ADAPTIVE_THRESH_GAUSSIAN_C:
  The threshold value T(x, y) is a weighted sum (cross-correlation with a Gaussian window) of the 
  blockSize x blockSize neighborhood of (x, y) minus C
```
![](README_IMG/adaptive_thresh_opencv_example.png)

#### 3. Otsu’s Binarization thresholding
```
- Input image: noise.jpg
- Command Line: python Image_threshold.py -i noise.jpg
```
```python
Function: ret,th = cv2.threshold(src_img, threshValue, maxValue, thresholdType)
ThresholdType: cv2.THRESH_BINARY+cv2.THRESH_OTSU
```
```python
Otsu’s Binarization thresholding and math description:

- This method is better to use with "bimodal image" which is an image whose histogram has two peaks.
- cv2.THRESH_OTSU
  This method automatically calculates a threshold value from image histogram for a bimodal image. 
  (For images which are not bimodal, binarization won’t be accurate.)
```
![](README_IMG/Otsus_thresh.png)

```
NOTE: Can apply "Gaussian filter" on the image to improve the result.
      - Function: cv2.GaussianBlur(src_img,(kernel size),sigma)
```
[(see "Smoothing Images" for more detail on Gaussian Filtering)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/edit/master/tutorials/Image_Processing/2_Image_Thresholding/README.md) (Unavailable)

[How Otsu's Binarization Works?](https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html)

[Youtube](https://www.youtube.com/watch?v=mnmjZOLjoBA)

## Code
- [Image Thresholding](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/2_Image_Thresholding/Image_Threshold.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (threshold) Link: https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
