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
Main Function: res = cv2.matchTemplate(img,target,method)
```
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
cv2.rectangle(img,top_left, bottom_right, 255, 2)

![](README_IMG/temp_match.png)

## Template Matching for Multi-objects
```
- File name: Image_Matching.py 
- Input image: cell.jpg
- Input target: cell_target.jpg
- Command Line: python Image_Matching.py -i cell.jpg -t cell_target.jpg
```
```python
Main Function: res = cv2.matchTemplate(img_gray,target,cv2.TM_CCOEFF_NORMED)
```

loc = np.where( res >= threshold)
cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

![](README_IMG/multi_match.png)

### Useful link:

- [Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/1_Changing_colorspace)

- [Image Thresholding](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/2_Image_Thresholding)

## Code
- [Image Matching (Template Matching)](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/10_Image_Matching)
- [Image Matching Implementation]

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (Histogram) https://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html

