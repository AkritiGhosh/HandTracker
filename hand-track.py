import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) # Built-in webcam
# cap = cv2.VideoCapture('http://10.126.160.55:4747/mjpegfeed?640x480') # Droidcam

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:


    suc, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks: # If hand detected
        for hndLmk in results.multi_hand_landmarks: 
            for id, lm in enumerate(hndLmk.landmark):
                print(id, lm) 
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                
                # Customize the tracking pattern
                if id == 0: #Base of palm
                    cv2.circle(img, (cx, cy), 25, (255, 255, 0), cv2.FILLED)

            # mpDraw.draw_landmarks(img, hndLmk) ### landmark points only
            mpDraw.draw_landmarks(img, hndLmk, mpHands.HAND_CONNECTIONS) ### Lines connecting points in 

# Calculate and print FPS 
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 20, 240), 3)

    cv2.imshow("Camera", img)
    cv2.waitKey(1)