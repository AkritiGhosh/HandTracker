import cv2
import time
import handTrackingModule as htm

def main():
    cap = cv2.VideoCapture(0) # Built-in webcam
    # cap = cv2.VideoCapture('http://10.126.160.55:4747/mjpegfeed?640x480') # Droidcam
    det = htm.handDetector()
    pTime = 0
    cTime = 0

    while True:
        suc, img = cap.read()
        # print(results.multi_hand_landmarks)
        img2 = det.findHands(img)
        lmk = det.findPosition(img2)
        if len(lmk) != 0:
            print(lmk[4])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 20, 240), 3)

        cv2.imshow("Camera", img)
        key = cv2.waitKey(1) & 0xFF ### get the last 8 bit of binary value
        # Check and change the key value below to change the exit key
        # Exit loop if q is pressed
        if key == ord('q'):
            break

    # Exit code !!!important
    cv2.destroyAllWindows()
    exit()

if __name__ == "__main__":
    main()


