# Hough Line Transform
"Hough Transform" is a method to detect any shape with a mathematical shape equation, here describe how hough transform work with line detection.

* Provide Hough Line Transform implement from scatch. [(Code)]

## Outline
- Hough Line Transform
- Probabilistic Hough Line Transform

## Hough Transform (Line)
```
- File name: Hough_Line_Transform.py
- Input image: pool.jpg
- Command Line: python Hough_Line_Transform.py -i pool.jpg
```

## Hough Line Transform

* Main Function: lines = cv2.HoughLines(src_img, rho, theta, threshold)
```python
* rho: Distance resolution of the accumulator in pixels.
* theta: Angle resolution of the accumulator in radians. (np.pi/180)
* threshold: Accumulator threshold, line selection.
```
### Process for hough line transformation:
```
Step 1. Get an edge image from original input image
```
* Read image and convert to grayscale image using cv2.cvtColor().
* Get edge image by using Canny Edge Detection cv2.Canny().

![](README_IMG/step1.png)

```
Step 2. Generate a matrix for theta and rho
```
* General line equation: y = ax+b
* Hough Line Transform use another line representation: x * cos(theta)+y * sin(theta) = rho

![](README_IMG/step2.png)

```
Step 3. Calculate (theta, rho) for each edge pixel (x, y) then add 1 to the matrix(theta, rho)
```
![](README_IMG/step3.png)
```
Step 4. Get the several high value in matrix then use theta and rho value to draw the line.
```

### Useful link:

- [Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/1_Changing_colorspace)
- [Canny Edge Detection](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/6_Canny_Edge_Detection)
- [Youtube: How Hough Transform works](https://www.youtube.com/watch?v=4zHbI-fFIlI)

![](README_IMG/lin5e.png)
    
    
![](README_IMG/temp_match.png)

## Template Matching for Multi-objects
```
- File name: Image_Matching.py 
- Input image: cell.jpg
- Input target: cell_target.jpg
- Command Line: python Image_Matching.py -i cell.jpg -t cell_target.jpg
```
```
Set a threshold for the return value by using numpy.where() for cv2.matchTemplate(), then 
draw all the region using cv2.rectangle():

* location = np.where( res >= threshold )
```

![](README_IMG/multi_match.png)

### Useful link:

- [Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/1_Changing_colorspace)

- [Image Thresholding](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/2_Image_Thresholding)

## Code
- [Image Matching (Template Matching)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/10_Image_Matching)
- [Template Matching Implementation by Using "Normalized Cross Correlation"](https://github.com/Hank-Tsou/Template-Matching)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Hough Line) https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html?highlight=houghlines
