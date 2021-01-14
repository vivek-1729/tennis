import cv2, os
import numpy as np
from matplotlib import pyplot as plt
from statistics import mean


def pixelsPerMeter():
    def horizontalLines(i):
        img = cv2.imread('analysis/frame' + str(i) + '.jpg')
        kernel = np.ones((5,5),np.float32)/30
        img = cv2.filter2D(img,-1,kernel)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150,apertureSize = 3)
        minLineLength=400
        lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/360, threshold=200,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
        a,_,_ = lines.shape
        y1_arr = []
        y2_arr = []
        for i in range(a):
            x1, y1, x2, y2 = lines[i][0][0], lines[i][0][1], lines[i][0][2], lines[i][0][3]
            angle = np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
            if angle != 0 and angle<2 and angle > -10:
                y1_arr.append(y1)
                y2_arr.append(y2)
                cv2.line(gray, (x1,y1), (x2, y2), (0, 0, 255), 3, cv2.LINE_AA)
        y1_arr.sort()
        y2_arr.sort()
        farRight = y2_arr[0]
        farLeft = y1_arr[0]
        closeRight = y2_arr[-1]
        closeLeft = y1_arr[-1]
        distance = abs(mean([farRight, farLeft] - mean([closeRight, closeLeft])))
        pixelsPerMeter = distance / 23.77
        return pixelsPerMeter

    averageRange = range(5)
    pixelsPerMeterList = []
    for i in averageRange:
        pixelsPerMeter = horizontalLines(i)
        pixelsPerMeterList.append(pixelsPerMeter)
    return mean(pixelsPerMeterList)
