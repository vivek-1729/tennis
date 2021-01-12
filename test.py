import cv2
from statistics import mean
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im = cv2.imread('images/frame144.jpg')
bbox, label, conf = cv.detect_common_objects(im)
index = label.index('sports ball')
label = [label[index]]
bbox = [bbox[index]]
dot = (int(mean([bbox[0][0], bbox[0][2]])), int(mean([bbox[0][1], bbox[0][3]])))
plt.imshow(im)
plt.show()
