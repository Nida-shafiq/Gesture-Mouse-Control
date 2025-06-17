# **Gesture-Based Virtual Mouse Using Hand Tracking with OpenCV and MediaPipe**

## **Project Description**
This project demonstrates a real-time virtual mouse system controlled entirely using hand gestures through a webcam. The main goal is to provide a touchless interface that replaces traditional mouse operations (like moving the cursor and clicking) using only your hand movements.

Using a combination of computer vision and machine learning models from Google’s MediaPipe, this project identifies hand landmarks and tracks the movement of the index finger to move the cursor. A simple gesture—bringing the thumb and index finger together—is recognized as a click.

---

## **Objectives**
- Build a virtual mouse that moves based on finger movement  
- Detect gestures using hand landmark positions  
- Simulate mouse click events using hand gestures  
- Use only a webcam and Python libraries (OpenCV, MediaPipe, PyAutoGUI)  

---

## **Tools and Libraries Used**
| Tool/Library | Purpose |
|--------------|---------|
| **OpenCV** | To capture video frames and display real-time video |
| **MediaPipe** | To detect and track 21 hand landmarks with high accuracy |
| **PyAutoGUI** | To control the mouse cursor and simulate click actions |
| **time** | To manage delays (used to prevent repeated fast clicking) |

---

## **How it Works (Step-by-Step)**

### **1. Capture Video**
- Use `cv2.VideoCapture(0)` to access your webcam  
- Set frame resolution using `cap.set(3, 640)` and `cap.set(4, 480)`  

### **2. Detect Hand Landmarks**
- Use MediaPipe’s hand detection module to identify 21 landmarks  
- These landmarks include fingertips, joints, and the wrist  

### **3. Move Cursor Using Index Finger**
- Index fingertip = **Landmark ID 8**  
- Get x, y position and convert to screen resolution using `pyautogui.moveTo()`  

### **4. Click Using Gesture**
- Thumb tip = **Landmark ID 4**  
- If distance between ID 8 and ID 4 is < 40 pixels, trigger `pyautogui.click()`  
- A green circle is drawn for visual feedback  

### **5. Delay Mechanism**
- A short delay (`click_delay = 0.5s`) prevents accidental multiple clicks  

### **6. Display Video Feed**
- OpenCV shows annotated hand with FPS  
- Press **ESC (27)** to exit  

---

## **Features**
- Real-time hand tracking with low latency  
- Cursor movement via index finger  
- Click operation with pinch gesture  
- High accuracy using MediaPipe’s hand model  
- No external hardware required — only a webcam!  

---

## **Use Cases**
- Accessibility tool for people with disabilities  
- Touchless control in hygienic environments  
- Interactive presentations  
- Can be extended to games or smart TV control  

---

## **Future Improvements**
- Add drag-and-drop support  
- Enable more gestures (right-click, scroll, etc.)  
- Improve click detection with gesture classification  
- Add voice feedback or GUI interface  
