# Changing Colorspace

## Outline:
- Changing Color Space for an image
- Extract specific color object ([Can apply on object tracking](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/edit/master/tutorials/Image_Processing/1_Changing_colorspace/README.md))(unavailable 7/4/2019)

### 1. Changing Colorspace  ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/1_Changing_colorspace/Changing_Colorspace.py))
```
- Input image: opencv.png
- Command Line: python Changing_Colorspace.py -i opencv.png
```

#### - Method 1: Color image to Grayscale image
```python
Grayscale_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
```
```
NOTE: 
  - RGB color image: each pixel (x,y) has three channals [Red, Green, Blue].
  - Grayscale image: each pixel (x,y) only has one channel from 0-255. (0 = Black, 255 = white)
```
![](README_IMG/RGBtoGray.png)

#### - Method 2: Color image to HSV image
```python
HSV_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)
```
```
NOTE: HSV image has three parameter [Hue, Saturation, Value].
    - Hue: Color portion of the model, expressed as a number from 0 to 360 degrees 
    - Saturation: Describes the amount of gray in a particular color, from 0 to 100 percent. 
    - Value: Describes the brightness or intensity of the color, from 0-100 percent.
```
([Wiki: HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV))

![](README_IMG/RGBtoHSV.png)

### 2. Extract Object 
```
Method:
    Step 1. Using HSV color space, convert color image to HSV image.
    Step 2. Define the range of color for the target object.
    Step 3. Using "cv2.inRange" to generate mask for the target bject
    Step 4. Using "cv2.bitwise_and" to extract the object
```
```
For Step 3: Generate object mask by using function "cv2.inRange()"

cv2.inRange(src_image, lowerbound, upperbound)
    - lowerbound and upperbound are the color range of the target.
```

[More detail for Step 4. Bitwise Operation](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Core_Operation)

![](README_IMG/Extract_Obj.png)

## Code
- [Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Image_Processing/1_Changing_colorspace/Changing_Colorspace.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (inRange()) Link: https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html
