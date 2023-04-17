import cv2
import mediapipe as mp 
import time
import HandTrackingModule as HTM


wScreen = 640
hScreen = 480
index = 0

cap = cv2.VideoCapture(0)

cap.set(3,wScreen)
cap.set(4,hScreen)


detec = HTM.handDetector()

cTime = 0
pTime = 0

while True :
    success, img = cap.read()
    
    detec.findHands(img)   
    detec.findPosition(img)
    listDis = detec.findDistanceFromThumb(img)
    
    for lenFinger in listDis:
        if 0 < lenFinger[1] < 20 : 
            print(lenFinger[0] , ' cham ngon tro ')

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime        
    cv2.putText(img,str(int(fps)), (10,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0) , 3)

    cv2.imshow('images' , img)
    
    key = cv2.waitKey(1)
    if key == 27 :
        break