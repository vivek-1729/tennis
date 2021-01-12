import cv2, os
from statistics import median
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

def graph(i):
    path = 'images/' + 'frame' + str(i) + '.jpg'
    img = cv2.imread(path) #('images/frame1770.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength=400
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/90, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
    try:
        a,b,c = lines.shape
    except:
        return 0
    print(len(lines))
    for i in range(a):
        x1, y1, x2, y2 = lines[i][0][0], lines[i][0][1], lines[i][0][2], lines[i][0][3]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180. / np.pi
        if angle > 50 or angle < -50:
            cv2.line(gray, (x1,y1), (x2, y2), (0, 0, 255), 3, cv2.LINE_AA)
    plt.imshow(gray)
    plt.show()

def getLines(path):
    img = cv2.imread(path) #('images/frame1770.jpg')
    try:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except:
        print(path)
        return -31415
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength=400
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/90, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
    try:
        a,b,c = lines.shape
        return a #return number of lines
    except:
        return 0



tennis = True
switch = False
switchFrame = -31415
allSwitchFrames = []
window = []
notTennisFrames = []
tennisFrames = []
numRange = list(range(0,3900,12))
for i,j in tqdm(zip(numRange, range(len(numRange))), total=len(numRange)):
    # print(i)
    path = 'images/' + 'frame' + str(i) + '.jpg'
    numLines = getLines(path)
    if numLines == -31415:
        print('over')
        break
    if switch:
        window.append(numLines) #add 5 numbers to the window
        if len(window) == 5:
            # medianWindow = median(window) #median not a great measure
            numTennisFrames = sum([1 if x >= 70 and x <= 120 else 0 for x in window])
            if numTennisFrames >= 3:
                tennis = True
                [tennisFrames.append(i) for i in numRange[j-5:j]]
                allSwitchFrames.append(switchFrame)
            else:
                tennis = False
            switch = False
            window = []

    if numLines >= 70 and numLines <= 120: #if this frame is a frame of the court
        if not tennis and not switch: #if the algorithm doesn't think we're on a tennis frame but we are (and switch isn't in action) then call the switch
            switch = True
            switchFrame = i
        elif not switch: #if algorithm is correct that we're at tennis and switch isn't in action
            tennisFrames.append(i)
    else:
        if tennis and not switch: #if we're not on a tennis frame but the algorithm thinks we are (and switch isn't in action) then call the switch
            switch = True

allSwitchFrames = list(set(allSwitchFrames))
switchIndices = [tennisFrames.index(x) for x in allSwitchFrames]
if 0 not in switchIndices:
    switchIndices.insert(0,0)
allShots = [tennisFrames[switchIndices[i-1]:switchIndices[i]] for i in range(1,len(switchIndices))] 
allShots.append(tennisFrames[switchIndices[-1]:])
print(allShots)