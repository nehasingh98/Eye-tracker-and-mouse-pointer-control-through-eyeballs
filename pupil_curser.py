import numpy as np
import cv2
import pyautogui

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

#number signifies camera
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray)
   
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        
        roi_color2 = img[ey:ey+eh, ex:ex+ew]
        roi_2=img[ey:ey+eh+100 ,ex:ex+ew+800]
        x= (ex+ew)/2
        y= (ey+eh)/2
        
       
        
        circles = cv2.HoughCircles(roi_gray2,cv2.cv.CV_HOUGH_GRADIENT,1,200,param1=200,param2=1,minRadius=0,maxRadius=0)
        try:
            for i in circles[0,:]:
               
                cv2.circle(roi_color2,(i[0],i[1]),i[2],(0,0,255),2)
                
                cv2.circle(roi_color2,(i[0],i[1]),2,(0,0,255),3)
                if(i[1] > y-100):
                    print('upward')
                    pyautogui.moveRel(None,-100,3)
                if(i[1]<y-35):
                    print('down')
                    pyautogui.moveRel(None,100,3)
                if(i[0]> x-150):
                    print('right')
                    pyautogui.moveRel(70,None,3)
                if(i[0]<x+150):
                    print('left')
                    pyautogui.moveRe1(-100,None,3)
        
            
                    
                
                
                
        except Exception as e:
            print e
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

