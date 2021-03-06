# Core_Operation

## Descrption:
- know how to select a ROI (region of interest) in an image.
- know how to do "image padding" to fill the edge of an image.
- know how to use "image blending" and "birwise operation" to combine two images.

### Outline:
1. Image ROI
2. Image padding
3. Image blending
4. Bitwise operation

### 1. Image ROI ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_ROI.py))
```
- Input image: opencv.png
- Command Line: python image_ROI.py --image opencv.png
```
![](README_IMG/ROI_result.png)

#### - Method 1: Use pixel range to select the region
```python
ROI_image = Input_Image[22:265, 60:311]
```
```
NOTE: 
  - notice that the image pixel x, y position in OpenCV is Input_Image[y, x].
  - ROI region x axis: from pixel 60 to 311, y axis: from pixel 22 to 265.
```
#### - Method 2: Use cv2.selectROI("input_image") to select the region
```python
r = cv2.selectROI(Input_Image)
ROI_img = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
```
```
NOTE: r = (x, y, width, height), we can use these return region values to crop the image.
```

### 2. Image padding ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_padding.py))
```
- Input image: padding_source.png
- Command Line: python image_ROI.py --padding_source.png
```
![](README_IMG/image_padding.png)

#### - Method: Use cv2.copyMakeBorder(Source, top, bottom, left, right, borderType)
```
void cv::copyMakeBorder	( InputArray src,
                          OutputArray dst,
                          int 	top,
                          int 	bottom,
                          int 	left,
                          int 	right,
                          int 	borderType,
                          const Scalar & value = Scalar() 
)	
```
```python
* replicate = cv2.copyMakeBorder(..,cv2.BORDER_REPLICATE)
* reflect = cv2.copyMakeBorder(..,cv2.BORDER_REFLECT)
* wrap = cv2.copyMakeBorder(..,,cv2.BORDER_WRAP)
* constant= cv2.copyMakeBorder(..,cv2.BORDER_CONSTANT,value=BLUE)
```

### 2. Image blending ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_blending.py))
```
- Input image: 
  * Background image: dog.jpg
  * foreground image: moon.jpg
- Command Line: python image_blending.py --image dog.jpg --ontop moon.jpg
```
![](README_IMG/image_blending.png)

#### - Method: Use cv2.addWeighted(src_1,alpha,src_2,beta,gamma)
```
This function calculates the weighted sum of two images.
dst(I) = Saturate(src(I)*alpha + src(I)*beta + gamma)
```

### 2. Bitwise operation ([Full code in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/bitwiseOp.py))
```
- Input image: 
  * Background image: dog.jpg
  * foreground image: opencv.png
- Command Line: bitwiseOp.py --image dog.jpg --ontop opencv.png
```
```
NOTE: two images need to be same shape.
```
#### - Function 1: Overlap two images
**STEP 1.** If two images not in the same shape, use function "cv2.resize()" to resize the image.
```
cv2.resize(src, (height, width), interpolation)
  - interpolation:
    * INTER_NEAREST - a nearest-neighbor interpolation
    * INTER_LINEAR - a bilinear interpolation (used by default)
    * INTER_AREA - resampling using pixel area relation. 
    * INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
    * INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood
```
**STEP 2.** Create mask by using grayscale image and threshold. 
```
Convert color(BGR) image to grayscale image. 

Function: cv2.cvtColor(input_image, flag)
  - Flag:
    * cv2.COLOR_BGR2GRAY: BGR to Gray conversion. 
    * cv2.COLOR_BGR2HSV: BGR to HSV conversion.
```
[More detail on Changing Colorspace](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/1_Changing_colorspace)
```
Thresholding: If pixel value is greater than a threshold value, it is assigned one value, 
              else it is assigned another value 

Function: ret,thresh1 = cv.threshold(src, threshold, maxval, type)
  - type:
    * cv.THRESH_BINARY
    * cv.THRESH_BINARY_INV
    * cv.THRESH_TRUNC
    * cv.THRESH_TOZERO
    * cv.THRESH_TOZERO_INV
```
[More detail on Image Thresholding](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/2_Image_Thresholding)

![](README_IMG/threshold.png)

**STEP 3.** Use function "cv2.bitwise_and()" to get background and foreground area on two images. Then add together.
```
NOTE: Use function "cv2.bitwise_not(mask)" which inverts every bit to get opposite mask.
```
```
* cv2.bitwise_and
* cv2.bitwise_or
* cv2.bitwise_xor

Usage: https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html
Code in bitwiseOp.py
```
![](README_IMG/middle.jpg)

#### - Function 2: Add foreground image on the top left (or any desire position): Method similar to Funtion 1.
![](README_IMG/topleft.jpg)

## Code
- [Image ROI in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_ROI.py)
- [Image Padding in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_padding.py)
- [Image blending in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/image_blending.py)
- [Bitwise Operation in python](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Core_Operation/bitwiseOp.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Reference & Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* (resize) Link: https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html?highlight=resize
* (threshold) Link: https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
