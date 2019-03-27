import cv2

camera=cv2.VideoCapture(0)#0-default camera(video akak nm 0 wenuwata path aka denawa)

face_clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    
    ret,frame=camera.read()#ret-this time camera is on or off frame-get one image for frame

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_clsfr.detectMultiScale(gray)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("LIVE",frame)

    #cv2.imshow("LIVE",gray)

    cv2.waitKey(1)
