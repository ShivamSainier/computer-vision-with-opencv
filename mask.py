import cv2
import numpy as np

def nothing(x):
    print(x)

cv2.namedWindow("josh")

img=cv2.imread("a.jpg",1)
img=cv2.resize(img,(400,550))
cv2.createTrackbar("LBlue","josh",0,255,nothing)
cv2.createTrackbar("LGreen","josh",0,255,nothing)
cv2.createTrackbar("LRed","josh",0,255,nothing)
cv2.createTrackbar("UBlue","josh",0,255,nothing)
cv2.createTrackbar("UGreen","josh",0,255,nothing)
cv2.createTrackbar("URed","josh",0,255,nothing)
while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lb=cv2.getTrackbarPos("LBlue","josh")
    lg=cv2.getTrackbarPos("LGreen","josh")
    lr=cv2.getTrackbarPos("LRed","josh")
    ub=cv2.getTrackbarPos("UBlue","josh")
    ug=cv2.getTrackbarPos("UGreen","josh")
    ur=cv2.getTrackbarPos("URed","josh")
    l_b=np.array([lb,lg,lr])
    u_b=np.array([ub,ug,ur])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("framm",img)
    cv2.imshow("g",hsv)
    cv2.imshow("frame",res)
    cv2.imshow("fram",mask)
    k=cv2.waitKey(1)
    if k==13:
        break
cv2.destroyAllWindows()
