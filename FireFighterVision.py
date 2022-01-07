import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('/home/pi/OpenCV-Face-Recognition-master/FaceDetection/Cascades/haarcascade_frontalface_default.xml')
fire_cascade = cv2.CascadeClassifier('/home/pi/FIRE_DETECTION-main/fire_detection_cascade_model.xml') 
# To access xml file which includes positive and negative images of fire. (Trained images)

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX

    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20, 20))

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        cv2.putText(img,'Face', (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_4)

    fire = fire_cascade.detectMultiScale(img, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
        cv2.putText(img, 'Fire', (x-20, y-20), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        

    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()