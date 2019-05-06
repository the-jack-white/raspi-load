#Jack White
#white123jack@gmail.com
#15 June 2018

import cv2
import os
#from time import gmtime, strftime
import time
import datetime

#add the Haar Cascades for testing data
face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_al1.xml')
face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier ('haarcascade_eye.xml')

#Use video camera, 0 ----> first assigned camera
cap = cv2.VideoCapture(0)
cap.set(3, 640) # set video width
cap.set(4, 480) # set video height
count = 0

d = datetime.date.today()

while (True):
    #read what is displayed on the camera
    ret, img = cap.read()

    #convert to grey scale, for better processing
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #body = body_cascade.detectMultiScale(gray, 1.1, 3)      #set the scale

    #create the detection boarders around features
    for (x,y,w,h) in faces:
        cv2.imwrite("dataset/" + "S001_C01_" + str(d) + "_" + time.strftime("%H_%M_%S") + ".jpg", img)
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        count += 1
    
    #cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    #elif count >= 5:
    #    break
    elif count >= 1: # After the first image is taken, the whole process will be delayed with 15 seconds
        time.sleep(15)

cap.release()
cv2.destroyAllWindows()