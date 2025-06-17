**Gesture-Based Virtual Mouse Using Hand Tracking with OpenCV and MediaPipe**

**Project Description:**
This project demonstrates a real-time virtual mouse system controlled entirely using hand gestures through a webcam. The main goal is to provide a touchless interface that replaces traditional mouse operations (like moving the cursor and clicking) using only your hand movements.

Using a combination of computer vision and machine learning models from Google’s MediaPipe, this project identifies hand landmarks and tracks the movement of the index finger to move the cursor. A simple gesture—bringing the thumb and index finger together—is recognized as a click.

**Objectives:**
Build a virtual mouse that moves based on finger movement

Detect gestures using hand landmark positions

Simulate mouse click events using hand gestures

Use only a webcam and Python libraries (OpenCV, MediaPipe, PyAutoGUI)

**Tools and Libraries Used:**
OpenCV	(To capture video frames and display real-time video)
MediaPipe	(To detect and track 21 hand landmarks with high accuracy)
PyAutoGUI	(To control the mouse cursor and simulate click actions)
time	(To manage delays (used to prevent repeated fast clicking)

**How it Works (Step-by-Step):**
**Capture Video:**

Use cv2.VideoCapture(0) to access your webcam.

Set frame resolution using cap.set(3, 640) and cap.set(4, 480) for consistent accuracy.

**Detect Hand Landmarks:**

Use MediaPipe’s hand detection module to identify 21 landmarks on your hand.

These landmarks include fingertips, joints, and the wrist.

**Move Cursor Using Index Finger:**

The index fingertip corresponds to landmark ID 8.

The x, y position of this point is converted from camera resolution to screen resolution using pyautogui.moveTo().

**Click Using Gesture:**

Thumb tip = ID 4

If the distance between ID 8 (index tip) and ID 4 (thumb tip) becomes small (e.g., < 40 pixels), it is interpreted as a click gesture.

pyautogui.click() is triggered, and a green circle is drawn as visual feedback.

**Delay Mechanism:**

A short delay (click_delay = 0.5s) is used to avoid multiple clicks from a single gesture.

**Display Video Feed:**

OpenCV displays the annotated frame with hand landmarks and FPS counter.

Pressing the ESC key (27) stops the program.

**Features:**
Real-time hand tracking with low latency

Cursor movement via index finger

Click operation with pinch gesture

High accuracy using MediaPipe’s hand landmark model

No external hardware required — only a webcam!

** Use Cases:**
Accessibility tool for people with disabilities

Touchless control in hygienic environments

Use in interactive presentations

Could be adapted for games or smart TV control

**Future Improvements:**
Add drag and drop support

Use multiple hand gestures for right-click, scroll, etc.

Improve click detection using gesture classification

Add voice feedback or GUI interface

