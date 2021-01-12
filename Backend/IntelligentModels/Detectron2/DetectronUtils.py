"""
Detectron MaskRCNN pe object detection
"""
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2


class Detectron:
    def __init__(self):
        # Create config
        self.cfg = get_cfg()

        self.cfg.merge_from_file(
            "IntelligentModels/Detectron2/detectron2/configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        self.cfg.MODEL.WEIGHTS = "detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl"

        # Create predictor
        self.predictor = DefaultPredictor(self.cfg)

        self.meta = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0])

    def detect_masks(self, file, output_file, size_percentage, show=False, save=False):
        im = cv2.imread(file)

        height, width, channels = im.shape

        height //= size_percentage
        width //= size_percentage

        # Make prediction
        outputs = self.predictor(im)
        instances = outputs["instances"].to("cpu")

        if show:
            v = Visualizer(im[:, :, ::-1], self.meta, scale=1.2)
            v = v.draw_instance_predictions(instances)
            ims = cv2.resize(v.get_image()[:, :, ::-1], (int(width), int(height)))
            cv2.imshow("", ims)
            cv2.waitKey(0)

        if instances.has("pred_classes"):
            return [self.meta.thing_classes[x] for x in instances.pred_classes]

        return []
