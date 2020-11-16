# from Models.Detectron2.DetectronUtils import Detectron
# detectron = Detectron()
# detectron.detect_masks("Data/1.jpg", "doodle_out.jpg", 3)

# from CodeGenerator import CodeGenerator
#
# cg = CodeGenerator("Python")
#
# response_bool, response_text = cg.generate_code("", "Output")
#
# print(response_text)

# from Models.DoodleRecognitionHelper import DoodleRecognitionHelper
#
# drh = DoodleRecognitionHelper()
#
# response = drh.predict("Data/2_b.png")
#
# print(response)

"""
Train doodle model
"""
# from Models.DoodleModel import DoodleModel
#
# dm = DoodleModel()
# dm.fit_and_evaluate()

# from Models.DoodleModel import DoodleModel
# from Utils.ImageUtils import imageToBytes
#
# # f = open("output.txt", "w+")
# # f.write(imageToBytes("570.jpg"))
# # f.close()
#
# bytes = imageToBytes("570.jpg")
# dm = DoodleModel(False)
# print(dm.predict(bytes))


"""
Data Split
"""
# import os
# from shutil import copy
#
# for folder in os.listdir("Data/Doodles"):
#     folder_path = "Data/Doodles/" + folder
#     files = os.listdir(folder_path)
#     i = 0
#     while i < 1400:
#         new_folder = "Data/Train/" + folder
#         if not os.path.exists(new_folder):
#             os.mkdir(new_folder)
#         copy(folder_path + "/" + files[i], new_folder + "/" + files[i])
#         i+=1
#     while i < 1800:
#         new_folder = "Data/Test/" + folder
#         if not os.path.exists(new_folder):
#             os.mkdir(new_folder)
#         copy(folder_path + "/" + files[i], new_folder + "/" + files[i])
#         i+=1
#     while i < 2000:
#         new_folder = "Data/Validation/" + folder
#         if not os.path.exists(new_folder):
#             os.mkdir(new_folder)
#         copy(folder_path + "/" + files[i], new_folder + "/" + files[i])
#         i+=1

# import os
# import cv2
#
# for folder in os.listdir("Data/Train"):
#     train_folder = "Data/Train/" + folder
#     test_folder = "Data/Test/" + folder
#     val_folder = "Data/Validation/" + folder
#
#     new_train_folder = "Data/New_Train/" + folder
#     new_test_folder = "Data/New_Test/" + folder
#     new_val_folder = "Data/New_Validation/" + folder
#
#     if not os.path.exists(new_train_folder):
#         os.mkdir(new_train_folder)
#     if not os.path.exists(new_test_folder):
#         os.mkdir(new_test_folder)
#     if not os.path.exists(new_val_folder):
#         os.mkdir(new_val_folder)
#
#     for fold, new_fold in [(train_folder, new_train_folder), (test_folder, new_test_folder), (val_folder, new_val_folder)]:
#         for file in os.listdir(fold):
#             image = cv2.imread(fold + "/" + file)
#             invert = cv2.bitwise_not(image)
#             cv2.imwrite(new_fold + "/" + file, invert)

from quickdraw import QuickDrawDataGroup
import os

# groups = ["apple", "banana", "bird", "birthday cake",
#           "book", "butterfly", "car", "cat", "crown",
#           "dog", "duck", "elephant", "eye", "fish",
#           "flower", "guitar", "hand", "house", "key",
#           "ladder", "leaf","light bulb", "mushroom",
#           "skull", "smiley face", "snowman", "square",
#           "circle", "tree"]
#
# for g in groups:
#     os.mkdir("Data/Doodles/" + g)
#     qdg = QuickDrawDataGroup(g, max_drawings=2000)
#     i=1
#     try:
#         for drawing in qdg.drawings:
#             drawing.image.save("Data/Doodles/" + g + "/" + str(i) + ".jpg")
#             i+=1
#     except:
#         pass


#
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import patches
#
# train = pd.read_csv("keras_frcnn/test.csv")
# train.head()
#
# data = pd.DataFrame()
# data['format'] = train['image_names']
#
# # as the images are in train_images folder, add train_images before the image name
# for i in range(data.shape[0]):
#     data['format'][i] = 'train_images/' + data['format'][i]
#
# # add xmin, ymin, xmax, ymax and class as per the format required
# for i in range(data.shape[0]):
#     xmin = train['xmin'][i]
#     ymin = train['ymin'][i]
#     width = train['width'][i]
#     height = train['height'][i]
#     xmax = xmin + width
#     ymax = ymin + height
#     data['format'][i] = data['format'][i] + ',' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + ',' + train['type'][i]
#
# data.to_csv('test.txt', header=None, index=None, sep=' ')



"""
Display image with annotations
"""

# fig = plt.figure()
#
# # add axes to the image
# ax = fig.add_axes([0, 0, 1, 1])
#
# # read and plot the image
# image = plt.imread('Data/DoodleData/2.jpg')
# plt.imshow(image)
#
# # iterating over the image for different objects
# for _, row in train[train.image_names == "2.jpg"].iterrows():
#     xmin = row.xmin
#     ymin = row.ymin
#
#     width = row.width
#     height = row.height
#
#     xmax = xmin + width
#     ymax = ymin + height
#
#     # assign different color to different classes of objects
#     if row.type == 'doodle':
#         edgecolor = 'r'
#         ax.annotate('doodle', xy=(xmax - 40, ymin + 20))
#     elif row.type == 'arrows':
#         edgecolor = 'b'
#         ax.annotate('arrows', xy=(xmax - 40, ymin + 20))
#     elif row.type == 'row':
#         edgecolor = 'g'
#         ax.annotate('row', xy=(xmax - 40, ymin + 20))
#
#     # add bounding boxes to the image
#     rect = patches.Rectangle((xmin, ymin), width, height, edgecolor=edgecolor, facecolor='none')
#
#     ax.add_patch(rect)
#
# plt.waitforbuttonpress()