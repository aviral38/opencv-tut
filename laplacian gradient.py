import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    cv2.imshow('frame',frame)
    cv2.imshow('laplacian',laplacian)
    k=cv2.waitKey(1)&0xFF
    if k==ord('q'):
        break
cv2.destroyAllWindow()
cap.release()
