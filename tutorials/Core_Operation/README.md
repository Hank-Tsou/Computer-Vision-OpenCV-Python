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

#### - Method 1: Use pixel range to select the region
```python
ROI_image = Input_Image[22:265, 60:311]
```
```
NOTE: 
  - notice that the image pixel x, y position in OpenCV is Input_Image[y ,x].
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

### 2. Image padding
