print('Importing modules... ')
from tqdm import tqdm
import cv2, os
from statistics import mean
import matplotlib.pyplot as plt
import cvlib as cv
from backend.getFrames import GetFrames
from backend.pixelsPerMeter import pixelsPerMeter
from backend.getTennisFrames import getTennisFrames

rallyNumber = int(input('Rally number: '))
def getForce(rallyNumber):
    getFrame = GetFrames('tennis.mp4')

    if len(os.listdir('images')) <= 5:
        print('Getting tennis frames')
        getFrame.preliminaryFrames()

    print(f'Getting frames for rally {rallyNumber}')
    tennisFrames = getTennisFrames()    

    shot = tennisFrames[rallyNumber]
    start, end = (min(shot), max(shot))
    notFound = 0
    print(f'Interpolating frames for rally {rallyNumber}')
    getFrame.interpolateFrames(start, end)
    allBallX = []
    allBallY = []
    print('Starting object detection for ball in every frame where the object detection system can detect the ball... ')
    for i in range(0, end-start):
        if notFound == 3:
            break
        path = 'analysis/frame' + str(i) + '.jpg'
        im = cv2.imread(path)
        bbox, label, _ = cv.detect_common_objects(im)
        try:
            index = label.index('sports ball')
        except ValueError:
            notFound += 1
            continue
        label = [label[index]]
        bbox = [bbox[index]]
        ballX = int(mean([bbox[0][0], bbox[0][2]]))
        ballY = int(mean([bbox[0][1], bbox[0][3]]))
        allBallX.append(ballX)
        allBallY.append(ballY)
    serveX = -31415
    print('Finding frame for serve... ')
    for i in range(1, len(allBallX)):
        if allBallX[i] - allBallX[i-1] > 30:
            serveX = i
    print('Getting pixel per meter ratio')
    pixelPerMeter = pixelsPerMeter()
    if serveX != -31415:
        print('Computing force... ')
        changeInY = abs(allBallY[serveX-1] - allBallY[serveX])
        distance = changeInY / pixelPerMeter
        speed = distance / (1/24)
        acceleration = speed / (1/24)
        force = 0.058 * acceleration 
        return force
    else:
        print('Was not able to find serve in this rally')
        return None


force = getForce(rallyNumber)

if force is not None:
    print(f'The force with which the ball was hit in rally {rallyNumber} was {force} newtons')
