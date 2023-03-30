import cv2
from matplotlib import pyplot as plt

  
capture = cv2.VideoCapture(0)
  
while(True):
      
    ret, frame = capture.read()
 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('video gray', grayFrame)
    cv2.imshow('video original', frame)
    plt.hist(grayFrame.ravel(), 256, [0, 256])
    plt.draw()
    plt.pause(0.1)
    plt.clf()   #clear the current figure
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
capture.release()
cv2.destroyAllWindows()