import cv2
import pyautogui

cscPath="closed_frontal_palm.xml"
cpalm=cv2.CascadeClassifier(cscPath)
val=[0,0]
cap=cv2.VideoCapture(0)
count=0

while (True):
    ret, frame=cap.read()
    cv2.imshow("swipe closed palm for volume control",frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    paw=cpalm.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(30,30))
    
    if (len(paw)!=0):
        for (x, y, w, h) in paw:    
            print (x)
        for i in range (0,5,1):
            ret, frame=cap.read()
        if (count==0):
            val[0]=int(x)
        if (count==1):
            val[1]=int(x)
        
        if (val[0]>val[1]and val[1]!=0):
            for i in range (0,4,1):
                pyautogui.press('volumeup')
        if (val[0]<val[1]and val[1]!=0):
            for j in range (0,4,1):
                pyautogui.press('volumedown')
        count=count+1

        if (count==2):
            count=0    
            val[0]=0
            val[1]=0
            
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
        
