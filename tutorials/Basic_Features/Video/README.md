# What is Video

In computer vision perspective, video(Digital video) is an electronic representation of moving visual images in the form of encoded digital data. Basically, video is created by a series of image frames. Each image frame has shape width x height x channel.

```
FPS: frame per second is measure the rate at which frames are displayed is known as the frame rate.
```
## Getting Started with Video using OpenCV Python

### Outline:
1. Read video from file and webcam
2. Get video information
3. Display video
4. Save video

### Prerequisites

The main library you need to install before starting ( [Full code in notebook] (empty))

```
pip install opencv-contrib-python
pip install numpy
```

### 1. Read Video from file and webcam

#### - Use function cv2.VideoCapture(Argument_1) to get a video. 

- Argument_1: 
  - Read from file: give an video name in the working directory or full video path (String).
  - Read from webcam: give 0, it will open the default camera (Integer).
              
#### - Use function cv2.VideoCapture(_).read() to read a video frame by frame. 

- no argument
```
Note: Use function "cv2.VideoCapture(_).isOpened()" to check get video success or not. (Boolean)
```

### 2. Get video information

#### - Use function cv2.VideoCapture(_).get(Argument_1, Argument_2) to get video information.

- Argument_1: passing video capture.

- Argument_2: property identifier, some id show as below 
  - [3] CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
  - [4] CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
  - [5] CV_CAP_PROP_FPS Frame rate.
  - [7] CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.

```
Note: There are 22 identifiers in get() method, see more detail on OpenCV Documentation
```
[OpenCV Documentation Media I/O](https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?
)

### 3. Display video

#### - Use function imshow(Argument_1) with while loop to display a video.
- Argument_1: pass your video frame into the function

```
Note: Make sure proper versions of ffmpeg or gstreamer is installed. Sometimes, it is a headache to work with Video Capture mostly due to wrong installation of ffmpeg/gstreamer. (from OpenCV-Python Tutorial)
```

### 4. Save or Write image

#### - Use function cv2.imwrite("Argument_1", Argument_2) to save an image.

- Argument_1: image name, ex: my_image_name.jpg

- Argument_2: pass your image into the function
```
Note: The image will save under your work directory
```

## Code
- [Full code in jupyter notebook](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Features/Images/Images.ipynb)
- [Full code in python file](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/blob/master/tutorials/Basic_Features/Images/Images.py)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* Matplotlib: https://matplotlib.org/api/pyplot_api.html
* Wiki: https://en.wikipedia.org/wiki/Digital_image

