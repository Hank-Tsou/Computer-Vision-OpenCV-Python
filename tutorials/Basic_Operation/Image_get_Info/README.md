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
  - img.shape:  It returns a tuple of number of [rows, columns, channels]. 
  - img.size: Data size which calculate by rows x colums x channels
    - Total number of pixels need to divided by number of channels
  - img.dtype: Image datatype
```
Note: In grayscale image, img.shape returned only contains number of rows and columns.
```





## Code
- [Full code in python file](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Operation/Image_get_Info/image_get_info.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
