# Hough Circle Transform
"Hough Transform" is a method to detect any shape with a mathematical shape equation, here describe how hough transform work with circle detection.

## Outline
- Hough Circle Transform

## Hough Circle Transform
```
File name: hough_circle_transform.py
Image name: pool.jpg
Command Line: python hough_circle_transform.py -i pool.jpg
```
* Main Function: circles = cv2.HoughCircles(src_img, cv2.HOUGH_GRADIENT, dp, minDist, 
..................................................................................... param1, param2, minRadius, maxRadius)
```
* src_img: 8-bit, single-channel, grayscale input image.
* method: Only CV_HOUGH_GRADIENT
* dp – Inverse ratio of the accumulator resolution to the image resolution.
* minDist – Minimum distance between the centers of the detected circles.
* param1 – The higher threshold of the two passed to the Canny() edge detector.
* param2 – The accumulator threshold for the circle centers at the detection stage.
* minRadius – Minimum circle radius.
* maxRadius – Maximum circle radius.
```

## Description
```
Equation: 
  - assume (xcenter, ycenter) is the center of the circle, and r is the radius of the circle. 
  - Circle: (x - xcenter)^2 + (y - ycenter)^2 = r^2
```
From equation, we can see we have 3 parameters, so we need a 3D accumulator for hough transform, which would be highly ineffective. So OpenCV uses more trickier method, Hough Gradient Method which uses the gradient information of edges.    (-- From OpenCV-Python Documentation)

![](README_IMG/line.png)

## Improvements
- [Hough Circle Transform - Improve ball detection]()


## Code
- [Hough Line Transform](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/11_Hough_Line_Transform)
- [Implement Hough Line Transform from Scratch](https://github.com/Hank-Tsou/Hough-Transform-Line-Detection)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Reference & Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
