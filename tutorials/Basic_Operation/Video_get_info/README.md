## Getting Started with Video using OpenCV Python

### Outline:
1. Get video information

### Prerequisites

The main library you need to install before starting ( [Full code in python file](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Operation/Video_get_info/video_get_info.py))

```
pip install opencv-contrib-python
```

### 1. Get video information

### - Use cv2.VideoCapture() to get video source. ( [More detail on video I/O](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Basic_Operation/Video_IO))


#### - Use function cv2.VideoCapture(__).get(Argument_1) to get video information.

- Argument_1: property identifier, some commonly use property show as below 

  - [3] cv2.CAP_PROP_FRAME_WIDTH:   Width of the frames in the video stream.
  - [4] cv2.CAP_PROP_FRAME_HEIGHT:  Height of the frames in the video stream.
  - [5] cv2.CAP_PROP_FPS:           Frame rate.
  - [7] cv2.CAP_PROP_FRAME_COUNT:   Number of frames in the video file.
```python
print("FPS: ", cap.get(cv2.CAP_PROP_FPS))
print("FPS: ", cap.get(5))
```
```
Note: There are 46 identifiers in get() method, see more detail on OpenCV Documentation
      Instead of these property, you can simply pass integers respectively (from 0 to 45).
```
[OpenCV Documentation Flags for video I/O](https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html)

## Code
- [Full code in python file](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Features/Video/Video.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* OpenCV Document: https://docs.opencv.org/3.4/

