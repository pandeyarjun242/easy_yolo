import numpy as np
import cv2,pafy
import time
import streamlit as st

class Yolov3Camera:
    def __init__(self,link,weights,cfg,names):
        self.link = link
        self.weights = weights
        self.cfg = cfg
        self.names = names
    def run_model(self):
        if self.link == 0:
            camera = cv2.VideoCapture(0)
        else:
            url = self.link
            vPafy = pafy.new(url)
            play = vPafy.getbest(preftype="mp4")
            camera = cv2.VideoCapture()
            camera.open(play.url)
        h, w = None, None
        with open(self.names) as f:
            labels = [line.strip() for line in f]
        network = cv2.dnn.readNetFromDarknet(self.cfg,self.weights)
        layers_names_all = network.getLayerNames()
        layers_names_output = \
            [layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]

        probability_minimum = 0.5
        threshold = 0.3

        colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

        while True:
            _, frame = camera.read()
            if w is None or h is None:
                h, w = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                         swapRB=True, crop=False)

            network.setInput(blob)  # setting blob as input to the network
            start = time.time()
            output_from_network = network.forward(layers_names_output)
            end = time.time()

            print('Current frame took {:.5f} seconds'.format(end - start))
            bounding_boxes = []
            confidences = []
            class_numbers = []
            for result in output_from_network:
                for detected_objects in result:
                    scores = detected_objects[5:]
                    class_current = np.argmax(scores)
                    confidence_current = scores[class_current]
                    if confidence_current > probability_minimum:
                        box_current = detected_objects[0:4] * np.array([w, h, w, h])
                        x_center, y_center, box_width, box_height = box_current
                        x_min = int(x_center - (box_width / 2))
                        y_min = int(y_center - (box_height / 2))

                        # Adding results into prepared lists
                        bounding_boxes.append([x_min, y_min,
                                               int(box_width), int(box_height)])
                        confidences.append(float(confidence_current))
                        class_numbers.append(class_current)
            results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                                       probability_minimum, threshold)
            if len(results) > 0:
                # Going through indexes of results
                for i in results.flatten():
                    x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
                    box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]
                    cv2.rectangle(frame, (x_min, y_min),
                                  (x_min + box_width, y_min + box_height),
                                  (255,0,0), 2)
                    text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])], confidences[i])
                    cv2.putText(frame, text_box_current, (x_min, y_min - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            cv2.namedWindow('YOLO v3 Real Time Detections', cv2.WINDOW_NORMAL)
            cv2.imshow('YOLO v3 Real Time Detections', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()