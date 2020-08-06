<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EASY_YOLO</h3>

  <p align="center">
    Run YoLOv3 object detectors in one line
    <br />
    <a href="https://github.com/pandeyarjun242/easy_yolo"><strong>Explore the code »</strong></a>
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project


We realised that implementing and running YOLOv3 object detectors require lines of unnecessary code. This library helps users automate the process by running any YOLOv3 models on images, videos, cameras and live streams

About Yolo-Auto
* It takes 2 lines to run
* Wide variaety of platforms
* Easy to use and best to test models in the development phase


### Built With/On

* [Python](https://www.python.org/)
* [Darknet](https://pjreddie.com/darknet/)
* [OpenCV](https://opencv.org/)



<!-- GETTING STARTED -->
## Getting Started

To get started to test some awesome object detectors.

### Installation
 
1. Pip install the package
```sh
pip install easy-yolo
```
2. Gather Cfg, weights and names file in a repository
```sh
data/yolov3.cfg
data/yolov3.weights
data/data.names
```




<!-- USAGE EXAMPLES -->
## Usage

This is the only amount of code you need to write:

_For more examples, please refer to the [Documentation](https://example.com)_

For Images:

```sh
from easy_yolo.yolo_img import YoloImg

x = YoloImg('example.jpg', 'example.weights', 'example.cfg','example.names')

x.run_model()

```
For Videos:


```sh
from easy_yolo.yolo_vid import Yolov3Video

x = Yolov3Video('example.mp4', 'example.weights', 'example.cfg','example.names')

x.run_model()
```

For Live Camera:


```sh
from easy_yolo.yolo_cam import Yolov3Camera

x = Yolov3Camera(0, 'example.weights', 'example.cfg','example.names')

x.run_model()
```
For Youtube Live Stream: # Reuires pafy
```sh
pip install pafy 
```
Then:

```sh
from easy_yolo.yolo_cam import Yolov3Camera

x = Yolov3Camera('youtube_url', 'example.weights', 'example.cfg','example.names')

x.run_model()
```



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@instagram_handle](https://instagram.com/_.pandeymonium) - pandeyarjun.242@gmail.com

Project Link: [https://github.com/pandeyarjun242/easy_yolo](https://github.com/pandeyarjun242/easy_yolo)

