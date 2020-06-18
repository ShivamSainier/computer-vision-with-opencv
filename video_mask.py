import numpy as np
import cv2


def nothing(x):
    print(x)

cv2.namedWindow("new")
cv2.createTrackbar("LB","new",0,255,nothing)
cv2.createTrackbar("LG","new",0,255,nothing)
cv2.createTrackbar("LR","new",0,255,nothing)


cv2.createTrackbar("UB","new",0,255,nothing)
cv2.createTrackbar("UG","new",0,255,nothing)
cv2.createTrackbar("UR","new",0,255,nothing)


cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lb=cv2.getTrackbarPos("LB","new")
    lg=cv2.getTrackbarPos("LG","new")
    lr=cv2.getTrackbarPos("LR","new")

    ub=cv2.getTrackbarPos("UB","new")
    ug=cv2.getTrackbarPos("UG","new")
    ur=cv2.getTrackbarPos("UR","new")

    
    u_b=np.array([ub,ug,ur])
    l_b=np.array([lb,lg,lr])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",hsv)
    cv2.imshow("fram",res)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
