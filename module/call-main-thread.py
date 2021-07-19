import cv2
import handTrackingModule as htm
from imutil import FPS
from imutil import WebCamVideoStream

def main():
    stream = WebCamVideoStream(src=0).start()  # Built-in primary webcam
    # stream = WebCamVideoStream(src='http://192.168.29.204:4747/mjpegfeed?640x480').start() # Droidcam
    det = htm.handDetector()
    fps = FPS().start() #starting fps

    while True:
        img = stream.read()
        img2 = det.findHands(img)
        lmk = det.findPosition(img2)
        # lmk is an array of length 21, where each element is a list of landmark coordinate
        # if len(lmk) != 0:
        #     print(len(lmk))
        #     print(lmk)
        
        ### Calculate and print FPS 
        fps.update()
        fps.stop()
        cv2.putText(img, str(fps.fps()), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 20, 240), 3)

        cv2.imshow("Camera", img)
        key = cv2.waitKey(1) & 0xFF ### get the last 8 bit of binary value
        # Check and change the key value below to change the exit key
        # Exit loop if q is pressed
        if key == ord('q'):
            break

    # Exit code !!!important
    cv2.destroyAllWindows() ### Close imshow windows
    stream.stop() ### Stop the thread 
    exit() ### Stop the main thread

if __name__ == "__main__":
    main()


