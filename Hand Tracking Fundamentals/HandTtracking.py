import cv2 #image processing
import mediapipe as mp #to train and build ML applications
import time #check frame rate

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands= mpHands.Hands(False)
mpDraw = mp.solutions.drawing_utils  #draws dots over the hands

pTime=0 #prev time
cTime=0 #current time
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                print(id,lm) #EACH IMAGE HAS AN UNIQUE LANDMARK
                h,w,c=img.shape
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS) #drawing the lines on BGR image not RGB

    cTime = time.time()
    fps= 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

