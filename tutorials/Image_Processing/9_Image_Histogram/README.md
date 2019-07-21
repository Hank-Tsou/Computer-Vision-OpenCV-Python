# Image Histogram

## Outline
- Image Histogram
- Histogram Equalization

## Image Histogram
Image histogram is a graph showing distribution of the pixel intensity values in an image.
```
- File name: Image_Histogram.py
- Input image: input_image.jpg
- Command Line: python Image_Histogram.py -i input_image.jpg
```

(a) Image Histogram
```python
Main Function: hist = cv2.calcHist(src_img, channels, mask, hist_size, range)
  * mask: Input mask or None
  * hist_size: Array of histogram sizes in each dimension.
  * range: Boundaries in each dimension
```
```
NOTE: An singel channel image has 256 different possible intensities (0-255).
```

(b) Partial Image Histogram
  * Step 1: Generate a binary mask.
  * Step 2: Use mask to select the region for calculate the histogram.
```python
Main Function: hist = cv2.calcHist(src_img, channels, mask, hist_size, range)
  * mask: Input mask = mask
```
  
Useful link:
[Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/1_Changing_colorspace)
[Bitwise Operation](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation)


## Histogram Equalization
```python
Main Function: equ_img = cv2.equalizeHist(src_img)
  * src_img: Source 8-bit single channel image(grayscale image).
```







![](README_IMG/extre_point.png)

## Code
- [Image Contours](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/8_Image_Contours/Image_Contours.py)
- [Contour Features](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/8_Image_Contours/Contour_Feature.py)
- [Convex Hull Implementation](https://github.com/Hank-Tsou/Convex-Hull)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Histogram) https://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html

