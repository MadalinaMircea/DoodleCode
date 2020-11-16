"""
Detectron MaskRCNN pe object detection
"""
# import some common detectron2 utilities
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2

class Detectron():
    def detect_masks(self, file, output_file, size_percentage):
        # get image
        im = cv2.imread(file)

        height, width, channels = im.shape

        height //= size_percentage
        width //= size_percentage

        # Create config
        cfg = get_cfg()
        cfg.merge_from_file("./Models/Detectron2/detectron2/configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        cfg.MODEL.WEIGHTS = "detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl"

        # Create predictor
        predictor = DefaultPredictor(cfg)

        # Make prediction
        outputs = predictor(im)

        v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
        v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        imS = cv2.resize(v.get_image()[:, :, ::-1], (width, height))
        cv2.imshow("", imS)
        cv2.waitKey(0)
