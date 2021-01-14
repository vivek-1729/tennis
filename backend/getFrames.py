import cv2

class GetFrames:
    def __init__(self, videoPath):
        self.vidcap = cv2.VideoCapture(videoPath)
        self.count = 0
        self.success = True
        self.placeholder = 0
    def preliminaryFrames(self):
        while self.success:
            self.vidcap.set(1,self.count)
            self.success,image = self.vidcap.read()
            if self.success == False:
                break
            cv2.imwrite("images/frame%d.jpg" % self.count, image)     # save frame as JPEG file      
            if self.count % 240 == 0:
                print('Read', int(self.count/24), 'seconds')
            self.count += 12

    def interpolateFrames(self, start, end):
        self.count = 0
        self.success = True
        while start+self.count < end:
            self.vidcap.set(1,start+self.count)
            success,image = self.vidcap.read()
            if success == False:
                break
            cv2.imwrite("analysis/frame%d.jpg" % (self.placeholder + self.count), image)     # save frame as JPEG file      
            if self.count % 24 == 0:
                print('Read', int(self.count/24), 'seconds')
            self.count += 1
        self.placeholder += self.count