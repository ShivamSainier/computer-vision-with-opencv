import cv2

cv2.namedWindow("track")
def nothing(x):
    print(x)

cv2.createTrackbar("two","track",4,15,nothing)
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    two=cv2.getTrackbarPos("two","track")
    th=cv2.adaptiveThreshold(frame, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY ,13,two)
    cv2.imshow("frame",th)
    k=cv2.waitKey(1)
    if k==13:
        break
cap.release()
cv2.destroyAllWindows()
