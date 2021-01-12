import cv2
vidcap = cv2.VideoCapture('tennis.mp4')
count = 0
success = True
while success:
    vidcap.set(1,count)
    success,image = vidcap.read()
    if success == False:
        break
    cv2.imwrite("images/frame%d.jpg" % count, image)     # save frame as JPEG file      
    if count % 240 == 0:
        print('Read', int(count/24), 'seconds')
    count += 12