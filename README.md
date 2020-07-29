## Easy_Yolo - One liner Yolov3 object detection

# Running on YOLO model on an image. Record location of necessary files

Sample:
from easy_yolo.yolo_img import YoloImg

<br>
x = YoloImg('example.jpg', 'example.weights', 'example.cfg',example.names)
x.run_model()

# Running on YOLO model on a video.

Sample:
from easy_yolo.yolo_vid import Yolov3Video
<br>
x = Yolov3Video('example.mp4', 'example.weights', 'example.cfg',example.names)
<br>
x.run_model()

# Running on YOLO model on a webcam.
<br>
Sample:
<br>
from easy_yolo.yolo_cam import Yolov3Camera
<br>
For webcam:
<br>
x = Yolov3Camera(0, 'example.weights', 'example.cfg',example.names)
<br>
x.run_model()

For Youtube Livestream:
<br>
x = Yolov3Camera('youtube_url', 'example.weights', 'example.cfg',example.names)
<br>
x.run_model()
