# Canny Edge Detection

## Outline:
- Canny Edge Detection

### 1. Canny Edge Detection
```
- Input image: chess_board.png
- Command Line: python Image_Gradient.py -i chess_board.png
```
To be more graphical. An edge is shown by the “jump” in intensity in the plot below:
(It shows more clearly if we take the first derivative on f(t))

![](README_IMG/thresh.png)

```
NOTE: we can find an edge by calculate pixel locations where the gradient is higher than its 
neighbors (or to generalize, higher than a threshold).
```

![](README_IMG/canny_edge.png)

## Code
- [Canny Edge Detection](https://github.com/Hank-Tsou/Computer-Vision-OpenCV-Python/tree/master/tutorials/Image_Processing/6_Canny_Edge_Detection)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* OpenCV-Python Tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

