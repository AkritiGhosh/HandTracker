import cv2
import mediapipe as mp
import time
import imutils
from imutil import FPS
from imutil import WebCamVideoStream

stream = WebCamVideoStream(src=0).start()  # Built-in primary webcam
# stream = WebCamVideoStream(src='http://abc.abc.xyz.xyz:port/mjpegfeed?640x480').start() # Droidcam

fps = FPS().start() #starting fps

# Hand tracking module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:

    img = stream.read()
    results = hands.process(img)

    if results.multi_hand_landmarks: # If hand detected
        for hndLmk in results.multi_hand_landmarks: 
            for id, lm in enumerate(hndLmk.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                
                # Customize the tracking pattern
                if id == 0: #Base of palm
                    cv2.circle(img, (cx, cy), 25, (255, 255, 0), cv2.FILLED)

            # mpDraw.draw_landmarks(img, hndLmk) ### landmark points only
            mpDraw.draw_landmarks(img, hndLmk, mpHands.HAND_CONNECTIONS)  ### Lines connecting landmarks

    ### Calculate and print FPS 
    fps.update()
    fps.stop()
    cv2.putText(img, str(fps.fps()), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 20, 240), 3)

    cv2.imshow("Camera", img)
    key = cv2.waitKey(1) & 0xFF ### get the last 8 bit of binary value
    print(key)
    # Check and change the key value below to change the exit key
    # Exit loop if q is pressed
    if key == ord('q'):
        break

# Exit code !!!important
cv2.destroyAllWindows() ### Close imshow windows
stream.stop() ### Stop the thread 
exit() ### Stop the main thread
