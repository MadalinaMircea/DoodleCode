import keras.backend as Backend
from keras.models import Sequential, model_from_json
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint
from Utils.ImageUtils import bytesToImage
import cv2
import numpy as np


class DoodleModel:
    def __init__(self, create):
        if create:
            self.model = self.create_model()
        else:
            self.read_from_file()
        self.write_to_file()

        self.classes = ["Apple", "Banana", "Butterfly",
                        "Car", "Cat", "Flower", "Guitar", "House", "Skull", "Smiley Face"]

    def write_to_file(self):
        json = self.model.to_json()
        file = open("model.json", "w+")
        file.write(json)
        file.close()

    def read_from_file(self, model_path = "model.json", weights_path = "best_weights.h5"):
        text = open(model_path, "r").read()
        self.model = model_from_json(text)
        self.model.load_weights(weights_path)

        self.model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    def predict(self, image):
        bytesToImage(image, "img.jpg")
        img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (28, 28))
        img = np.reshape(img, [1, 28, 28, 1])

        classes = np.argmax(self.model.predict(img), axis=-1)
        return self.classes[classes[0]]
        # img = ImageUtil.LoadImg(path, target_size: new
        # Shape(75, 75));
        # NDarray
        # arr = ImageUtil.ImageToArray(img);
        #
        # arr = Numpy.np.expand_dims(arr, 0);
        #
        # NDarray
        # response = model.Predict(arr);
        #
        # char
        # pred = GetPrediction(response[0]);
        #
        # return pred;
        # }

    def create_model(self):
        imgHeight = 28

        if Backend.image_data_format() == "channels_first":
            inputShape = (1, imgHeight, imgHeight)
        else:
            inputShape = (imgHeight, imgHeight, 1)

        newModel = Sequential()
        newModel.add(Conv2D(32, (3,3), padding="same", input_shape=inputShape, activation="relu"))
        newModel.add(MaxPooling2D(padding="same"))
        newModel.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape, activation="relu"))
        newModel.add(MaxPooling2D(padding="same"))
        newModel.add(Flatten())
        newModel.add(Dropout(0.3))
        newModel.add(Dense(1024, activation="relu"))
        newModel.add(Dropout(0.5))
        newModel.add(Dense(10, activation="softmax"))

        newModel.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

        return newModel

    def fit_and_evaluate(self):
        imgHeight = 28
        trainSamples = 15500
        testSamples = 2500
        epochs = 1000
        batchSize = 750

        trainDirectory = "Data/New_Train"
        testDirectory = "Data/New_Test"
        validationDirectory = "Data/New_Validation"

        generator = ImageDataGenerator(rescale=(1.00 / 255.00))

        trainIterator = generator.flow_from_directory(trainDirectory, class_mode="categorical",
                                                      target_size=(imgHeight, imgHeight),
                                                      batch_size=batchSize, color_mode="grayscale")

        testIterator = generator.flow_from_directory(testDirectory, class_mode="categorical",
                                                     target_size=(imgHeight, imgHeight),
                                                     batch_size=batchSize, color_mode="grayscale")

        validationIterator = generator.flow_from_directory(validationDirectory, class_mode="categorical",
                                                           target_size=(imgHeight, imgHeight), batch_size=batchSize,
                                                           color_mode="grayscale")

        checkpoint = ModelCheckpoint(filepath="best_weights.h5", monitor="val_accuracy", verbose=1, save_best_only=True)

        self.model.fit_generator(trainIterator, steps_per_epoch=trainSamples // batchSize, epochs=epochs, verbose=1,
                                 validation_data=validationIterator, callbacks=[checkpoint])

        loss = self.model.evaluate_generator(testIterator, steps=testSamples // batchSize)

        for d in loss:
            print(str(d) + " ")
