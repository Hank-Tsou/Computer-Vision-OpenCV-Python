# Image Contours

## Outline
- Image Contours
- Contour Features
  - Moments
  - Contour Area and Perimeter
  - Contour Approximation
  - Convex Hull
  - Bounding Rectangle
  - Minimum Enclosing Circle
  - Extreme Points

### Image Contours
In OpenCV, finding contours is like finding white object from black background. So object to be found should be white and background should be black.   - (from openCV-python tutorial)
```
- File: Image_Contours.py
- Input image: shapes.png
- Command Line: python Image_Contours.py -i shapes.png
```
```python
Main Function: image, contours, hierarchy = cv2.findContours(src_img, mode, method)
```
```python
- mode:
  * CV_RETR_EXTERNAL: retrieves only the extreme outer contours.
  * CV_RETR_LIST: retrieves all of the contours without establishing any hierarchical relationships.
  * CV_RETR_CCOMP: retrieves all of the contours and organizes them into a two-level hierarchy. 
  * CV_RETR_TREE: retrieves all of the contours and reconstructs a full hierarchy of nested contours. 
- method:
  * CV_CHAIN_APPROX_NONE: stores absolutely all the contour points. 
  * CV_CHAIN_APPROX_SIMPLE: stores only several important points.
```
```
NOTE: 
  * FindContours() modifies the source image. So can use image.copy() to store the original image.
  * The different between two Contour approximation method show as blow:
    (1) cv2.CV_CHAIN_APPROX_SIMPLE
    (2) cv2.CV_CHAIN_APPROX_NONE
```
![](README_IMG/contour.png)

### More - drawpoint function
```
FindContours() will return contour pixels, here use cv2.circle() to draw a dot on each pixel.
Function: cv2.circle(src_img, center, radius, color, thickness)
```

### Image Features
```python
- File: Contour_Feature.py
- Input image: feature.png
- Command Line: python Contour_Feature.py -i feature.png
```

#### a. Moments
Image moments help you to calculate some features like center of mass of the object, area of the object etc. Check out the wikipedia page on [Image Moments](https://en.wikipedia.org/wiki/Image_moment)   - (from openCV-python tutorial)
```python
Main Function: M = cv2.moments(contour)
```
```
Here extract useful data from moments(M) to calculate Centroid:
  * cx = int(M['m10']/M['m00'])
  * cy = int(M['m01']/M['m00'])
```

#### b. Contour Area and Perimeter
```python
Main Function:
  (1) area = cv2.contourArea(contour)
  (2) perimeter = cv2.arcLength(contour, isClosed)
      - isClosed: whether the curve is closed or not.
```
```
NOTE: The unit for the Area and Perimeter is "pixel".
```

#### c. Contour Approximation
It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify.

```python
Main Function: approx = cv2.approxPolyDP(contour, epsilon, isClosed)

epsilon = 0.02 * cv2.arcLength(contour,isClosed)
  - epsilon: Parameter specifying the approximation accuracy. This is the maximum distance between 
             the original curve and its approximation.
```
![](README_IMG/approximation.png)

#### c. Convex Hull
 ```
 Main Function: hull = cv2.convexHull(contour)
 ```
 ![](README_IMG/convex_hull.png)
 
 
 
 
 
 
 
 
![](README_IMG/Gaussian.png)
```
NOTE: In figure above, while doing up sampling, image decrease resolution because the process 
lost information during down sampling.
```

#### 2. Laplacian pyramids
Laplacian Pyramids are formed from the Gaussian Pyramids. A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid. The process show as below:

```
  * Generate Laplacian Pyramids:               * Re-construct the image using Laplasian pyramid:

    L0 = G0 - G1(Expand)                         re-construct(3) = L3 + L4(Expand)
    L1 = G1 - G2(Expand)                         re-construct(2) = L2 + re-construct(3)(Expand)
    L2 = G2 - G3(Expand)                         re-construct(1) = L1 + re-construct(2)(Expand)
        .                                        re-construct image = L0 + re-construct(1)(Expend)
        .
        .
```
![](README_IMG/pyramid.png)
```
NOTE: Laplacian pyramid images are like edge images. Can adjust the screen brighter to see the 
contour of the image below or it will be all black.
```
![](README_IMG/Laplacian.png)

## Code
- [Image pyramids](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/7_Image_Pyramids)
- [Implement pyramid image blending](https://github.com/Hank-Tsou/Image-Pyramids)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Gaussian pyramid) https://docs.opencv.org/2.4/doc/tutorials/imgproc/pyramids/pyramids.html
* (Laplacian process) http://www.eng.tau.ac.il/~ipapps/Slides/lecture05.pdf
