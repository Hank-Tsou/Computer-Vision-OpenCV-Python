## Getting Started with Image using OpenCV Python

### Outline:
1. Get image information

### Prerequisites

The main library you need to install before starting ( [Full code in python file](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Operation/Image_get_Info/image_get_info.py) )

```
pip install opencv-contrib-python
```

### 1. Get image information

#### - Use function cv2.imread() to read an image. ( [More detail on image I/O](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Basic_Operation/Image_IO))

#### - Get image property information (color image)
  - image.shape:  It returns a tuple of number of [rows, columns, channels]. 
  - image.size: Data size which calculate by rows x colums x channels
  - image.dtype: Image datatype
```
Note: 
    - In grayscale image, image.shape returned only contains number of rows and columns.
    - Total number of pixels = image.size divided by number of channels.
```

#### - Get image pixel information (color image)
  - pixel value at image ( x , y ) = image [ x , y ]
    - Color image return [ B,G,R ]
    - Grayscale image only return a value between ( 0-255 )

```
Note: Different method has different RGB order, the order with OpenCV imread() is BGR.
```
```python
# Get image pixel value
pixel_value = img[ x, y ]
pixel_value_B = img[ x, y, 0 ] # BLUE channel value
pixel_value_G = img[ x, y, 1 ] # Green channel value
pixel_value_R = img[ x, y, 2 ] # Red channel value
```

## Code
- [Full code in python file](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Operation/Image_get_Info/image_get_info.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
