import cv2
cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(True):
    ret,frame=cap.read()
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    out.write(frame)# IT WILL OUTPUT THE VIDEO IN NORMAL COLOR MODE
    if cv2.waitKey(1)== ord('b'):
        break
cap.release()
cv2.destroyAllWindows()