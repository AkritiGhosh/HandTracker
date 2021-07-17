# HandTracker

Use computer vision to detect hand movement and track it in real time. For this, you'll require a laptop with a decent webcam, python and required libraries installed and strong internet connection(for droidcam).

![Hand Tracker using CV](/images/hand-tracker.PNG "Hand Tracker project")

## hand-track.py

The most basic hand tracking function which shows landmarks in your hand.

![Hand Landmarks(CV)](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png "Hand Landmarks")

### Libraries required (Install to run)
- OpenCV
- Mediapipe

There are 2 cameras used for this, one is the primary webcam of your laptop/system. The other is a droidcam. Droidcam is a free software available for Windows to use Android camera as webcam.(Great for video conferences and CV projects).

![webcam](/images/webcam.PNG "Using a Webcam")

![droidcam](/images/droidcam.PNG "Using Droidcam software")


It also displays the fps of your camera. Using droidcam reduces the fps and slows down the function significantly but with better picture quality, it can perform better detection.

The mediapipe.solutions.hands module is used for this project. It reads an RGB image, processes it and then gives the following information about each landmark.
- id : the landmark number(according to the picture given above)
- lm.x - the x-coordinate of a landmark
- lm.y - the y-coordinate of a landmark

You can draw only the landmark or with connections. You can also manipulate the pattern of a particular landmark, as shown for the point at the base of the palm.

![id0-change](/images/id0-pattern.PNG "Changing landmark 0")

### Run 
To use this, simply download the .py file and execute it using cmd or VS code terminal.

```path/to/file> python hand-track.py ```


----

