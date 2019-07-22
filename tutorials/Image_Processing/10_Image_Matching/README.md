# Image Matching (Template Matching)

## Outline
- Template Matching
- Template Matching for Multi-objects

## Template Matching
```
- File name: Image_Matching.py 
- Input image: brain.jpg 
- Input target: target.jpg
- Command Line: python Image_Matching.py -i brain.jpg -t target.jpg
```
```python
Main Function: hist = cv2.calcHist(src_img, channels, mask, hist_size, range)

  * mask: Input mask or None
  * hist_size: Array of histogram sizes in each dimension.
  * range: Boundaries in each dimension
```
![](README_IMG/temp_match.png)

## Template Matching for Multi-objects
```
- File name: Image_Matching.py 
- Input image: cell.jpg
- Input target: cell_target.jpg
- Command Line: python Image_Matching.py -i cell.jpg -t cell_target.jpg
```
```python
Main Function: hist = cv2.calcHist(src_img, channels, mask, hist_size, range)

  * mask: Input mask or None
  * hist_size: Array of histogram sizes in each dimension.
  * range: Boundaries in each dimension
```
![](README_IMG/multi_match.png)

### Useful link:

- [Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/1_Changing_colorspace)

- [Bitwise Operation](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation)

## Code
- [Image Histogram](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/9_Image_Histogram)
- [Histogram Equalization Implementation](https://github.com/Hank-Tsou/Histogram)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Histogram) https://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html

