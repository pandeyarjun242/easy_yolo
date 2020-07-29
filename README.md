## Easy_Yolo - One liner Yolov3 object detection

# Running on YOLO model on an image. Place .cfg, .weights and .names in same directory

Sample:
from easy_yolo.yolo_img import YoloImg


x = YoloImg('example.jpg', 'example.weights', 'example.cfg',example.names)
x.run_model()

# Running on YOLO model on a video. Place .cfg, .weights and .names in same directory

Sample:
from easy_yolo.yolo_vid import Yolov3Video
x = Yolov3Video('example.mp4', 'example.weights', 'example.cfg',example.names)
x.run_model()

# Running on YOLO model on a webcam. Place .cfg, .weights and .names in same directory

Sample:
from easy_yolo.yolo_cam import Yolov3Camera
For webcam:
x = Yolov3Camera(0, 'example.weights', 'example.cfg',example.names)
x.run_model()

For Youtube Livestream:
x = Yolov3Camera('youtube_url', 'example.weights', 'example.cfg',example.names)
x.run_model()
