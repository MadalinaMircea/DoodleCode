# from Models.Detectron2.DetectronUtils import Detectron
# detectron = Detectron()
# detectron.detect_masks("Data/1.jpg", "doodle_out.jpg", 3)

from CodeGenerator import CodeGenerator

cg = CodeGenerator("Python")

response_bool, response_text = cg.generate_code("", "Output")

print(response_text)

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