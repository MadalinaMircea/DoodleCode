from keras.models import load_model
import tensorflow as tf
from PIL import Image
import io
import numpy as np
import base64


class DoodleRecognitionHelper:
    def __init__(self):
        self.model = load_model("Models/doodle_trial_model.h5")

    def predict(self, path):
        image = Image.open(path)
        image.resize((80, 80), Image.ANTIALIAS)
        image = np.array(image)
        image = image[:, :, 0]
        image = image.flatten()
        image_np = np.array([image])
        prediction = self.model.predict(image_np).tolist()
        response = {
            'prediction': {
                'apple': prediction[0][0],
                'banana': prediction[0][1],
                'circle': prediction[0][2],
                'pineapple': prediction[0][3]
            }
        }
        return response
