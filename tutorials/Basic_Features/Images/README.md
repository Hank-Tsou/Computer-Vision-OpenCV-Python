# What is Image

In computer vision perspective, image is a combination of pixels, the image shape should be "weidth x height x channels".
- Color image has three channel, RGB.
- Grayscale image only has one channel.

Note: it is possible for an image to have more than three channels.

## Getting Started with Image using OpenCV Python

### Outline:
1. Read Image
2. Display Image using OpenCV library
3. Display image using matplotlib in jupyter notebook
4. Save Image

### Prerequisites

The main library you need to install before starting

```
pip install opencv-contrib-python
pip install jupyter notebook
pip install matplotlib
```

### Read Image

#### Function: Use function cv2.imread(Argument_1, Argument_2) to read an image. 

- Argument_1: an image name in the working directory or full image path           

- Argument_2:
  - cv2.IMREAD_COLOR:      Loads a color image.
  - cv2.IMREAD_GRAYSCALE:  Loads image in grayscale mode. 
  - cv2.IMREAD_UNCHANGED:  Loads image as such including alpha channel.

```
Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
```

### DISPLAY IMAGE using openCV library

#### Function: Use function cv2.imshow(Argument_1, Argument_2) to display an image.

- Argument_1: image window name

- Argument_2: pass your image into the function

```
Other Function You Should Know: 
  - cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
    If 0 is passed, it waits indefinitely for a key stroke.

  - cv2.destroyAllWindows() simply destroys all the windows we created.
```




## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

