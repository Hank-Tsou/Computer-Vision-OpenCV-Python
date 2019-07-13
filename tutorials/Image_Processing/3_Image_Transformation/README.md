# Image Transformation

## Outline:
- Geometric Transformations ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/3_Image_Transformation/Geometric_Transformations.py))
  - Image scaling
  - Image translation
  - Image rotation
  - Image transformation

- Morphological Transformations ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/3_Image_Transformation/Morphological_Transformations.py))
  - Image erosion & Image dilation
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
                 but when the image is zoomed, it is similar to the INTER_NEAREST method.
   - INTER_CUBIC: a bicubic interpolation over 4x4 pixel neighborhood
```

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
![](README_IMG/translation.png)

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

 in matrix     [x'] = [ cos(a) -sin(a) ] * [x]
----------->   [y']   [ sin(a)  cos(a) ]   [y]
```
```python
Rotattion_Matrix = cv2.getRotationMatrix2D(center, angle, scale)
  - scale: Isotropic scale factor.
```
![](README_IMG/rotation.png)

#### d. Image transformation (Affine_transformation)
```python
Function: prespec_img = cv2.warpAffine(src_img, Matrix, output_size)
```
```python
Matrix = cv2.getAffineTransform(points_1[3 points], points_2[3 points]), see code.
```
```
NOTE: Matrix need 3 points from input image and their corresponding locations in output image. 
```
![](README_IMG/affin.png)

#### e. Image transformation (Perspective_transformation)
```python
Function: prespec_img = cv2.warpPerspective(src_img, Matrix, output_size)
```
```python
Matrix = cv2.getPerspectiveTransform(points_1[4 points], points_2[4 points]), see code.
```
```
NOTE: Matrix need 4 points on the input image and corresponding points on the output image. 
```
![](README_IMG/perspective.png)

### 2. Morphological Transformations

#### a. Image erosion & Image dilation
```python
Function: 
  - erosion = cv2.erode(src_img, kernel, iterations)
  - dilation = cv2.dilate(src_img, kernel, iterations)
```
```python
NOTE: 
  - Use numpy to generate kernel
    kernel = np.ones(kernel_size, np.uint8)
  
  - iterations: Number of times erosion and dilation are applied.
```
![](README_IMG/eorsion_dilation.png)
```
Tips: [erosion] increase black, [dilation] increase white.
```

 #### b. Function MorphologyEx()
 ```python
Function: cv2.morphologyEx(src_img, operation, kernel)
```
```
Morphological operation:

  - cv2.MORPH_OPEN: an opening operation, erosion followed by dilation. 
    * dilate(erode(src, element))
    
  - cv2.MORPH_CLOSE: a closing operation, Dilation followed by Erosion.
    * erode(dilate(src, element))
    
  - cv2.MORPH_GRADIENT: Difference between dilation and erosion of an image.
    * dilate(src, element) - erode(src, element)
    
  - cv2.MORPH_TOPHAT: Difference between input image and Opening of the image.
    * src - open(src, element)
    
  - cv2.MORPH_BLACKHAT: Difference between the closing of the input image and input image.
    * close(src, element) - src
```
```python
NOTE: 
  - Use numpy to generate kernel
    kernel = np.ones(kernel_size, np.uint8)
```
![](README_IMG/morphology.png)

## Code
- [Geometric Transformations](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/3_Image_Transformation/Geometric_Transformations.py)
- [Morphological Transformations](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/3_Image_Transformation/Morphological_Transformations.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Geometric) https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html
* (Morphological) https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html?highlight=morphologyex
