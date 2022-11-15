from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2 import model_zoo

import cv2
import numpy as np

class Detector:
    def __init__(self, model_type):
        self.cfg = get_cfg()

        #Load model and pretrained model
        if model_type == "KP":
            self.cfg.merge_from_file(model_zoo.get_config_file("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml"))
            self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml")

        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
        self.cfg.MODEL.DEVICE = "cpu"

        self.predictor = DefaultPredictor(self.cfg)

    def onVideo(self, videoPath):
        cap = cv2.VideoCapture(videoPath)

        if(cap.isOpened()==False):
            print("Error")
            return
        (sucess, image) = cap.read()

        while sucess:
            predictions = self.predictor(image)

            viz = Visualizer(image[:,:,::-1], metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
            instance_mode = ColorMode.IMAGE)

            output = viz.draw_instance_predictions(predictions["instances"].to("cpu"))

            cv2.imshow("Result", output.get_image()[:,:,::-1])

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            (sucess, image) = cap.read()