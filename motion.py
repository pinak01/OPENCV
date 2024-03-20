import cv2,time

video = cv2.VideoCapture(0);
first=None
while True:
    check,frame=video.read();
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0);
    if first is None:
        first=gray
        continue
    delta_frame=cv2.absdiff(first,gray)
    threshol_frm=cv2.threshold(delta_frame,50,255,cv2.THRESH_BINARY)[1]
    threshol_frm=cv2.dilate(threshol_frm,None,iterations=2)

    (cntr,_)=cv2.findContours(threshol_frm.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
       if cv2.contourArea(contour)<500:
        continue
       (x,y,w,h)=cv2.boundingRect(contour)
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Motion",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('a'):
       cv2.setWindowProperty("Motion", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


video.release()
cv2.destroyAllWindows()
