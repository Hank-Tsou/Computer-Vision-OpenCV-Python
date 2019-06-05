# Basic_Operation

## Descrption:
- know how to select a ROI (region of interest) in an image.
- know how to do "image padding" to fill the edge of an image.
- know how to use "image blending" and "birwise operation" to combine two images.

### Outline:
1. Image ROI
2. Image padding
3. Image blending
4. Bitwise operation

### 1. Image ROI 
```
- Input image: opencv.png
- Command Line: python image_ROI.py --image opencv.png
```
![](README_IMG/ROI_result.png)

#### - method 1: use pixel range to select the region
```python
ROI_image = Input_Image[22:265, 60:311]
```
```
ROI region x: from pixel 22 to 265, y: from pixel 60 to 311
```
#### - method 2: use cv2.selectROI("input_image") to select the region
```python
r = cv2.selectROI(Input_Image)
ROI_img = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
```
```
NOTE: r = (x, y, width, height), we can use these return region values to crop the image
```



### 2. Display image using openCV library

#### - Use function cv2.imshow("Argument_1", Argument_2) to display an image.

- Argument_1: image window name (String)

- Argument_2: pass your image into the function
```
Function You Should Know: 

  - cv2.waitKey(): a keyboard binding function. Its argument is the time in milliseconds. 
                   If 0 is passed, it waits indefinitely for a key stroke.
  - cv2.destroyAllWindows(): simply destroys all the windows we created.
```
```python
cv2.imshow('image', img_gray) # display image
cv2.waitKey(0)                # wait, press any key to continue
cv2.destroyAllWindows()       # destroy all windows
```
