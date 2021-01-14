import os
from backend.getFrames import GetFrames
from backend.getTennisFrames import getTennisFrames

getFrame = GetFrames('tennis.mp4')

if len(os.listdir('images')) <= 5:
    print('Getting images... ')
    getFrame.preliminaryFrames()

print('Getting tennis frames... ')
tennisFrames = getTennisFrames()

def generateHighlight(tennisFrames, getFrame):
    for i,j in zip(tennisFrames, range(len(tennisFrames))): #get list of frame 
        j += 1
        print(f'Rally {j}')
        start,end = (min(i), max(i))
        getFrame.interpolateFrames(start, end)
    print('Converting to video... ')
    os.system('ffmpeg -r 24 -i analysis/frame%01d.jpg -vcodec mpeg4 -y highlight.mp4')
    os.rename('highlight.mp4', 'output/highlight.mp4')
    
    print('Deleting files in analysis folder... ') #delete because there are thousands of frames in the analysis folder
    filelist = [ f for f in os.listdir('analysis')]
    for f in filelist:
        os.remove(os.path.join('analysis', f))
generateHighlight(tennisFrames, getFrame)
print('The highlights is now in the output folder')