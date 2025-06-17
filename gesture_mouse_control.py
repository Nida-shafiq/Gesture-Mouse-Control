# gesture_mouse_control.py

import cv2
import mediapipe as mp
import pyautogui
import time



cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils


screen_w, screen_h = pyautogui.size()


prev_time = 0
last_click_time = 0
click_delay = 0.5  

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

           
            ix, iy = lm_list[8]
            scr_x = int(ix / w * screen_w)
            scr_y = int(iy / h * screen_h)
            pyautogui.moveTo(scr_x, scr_y, duration=0)

           
            tx, ty = lm_list[4]
            distance = ((tx - ix)**2 + (ty - iy)**2)**0.5

            if distance < 40:
         
                
                current_time = time.time()
                if current_time - last_click_time > click_delay:
                    pyautogui.click()
                    last_click_time = current_time
                    cv2.circle(frame, (ix, iy), 15, (0, 255, 0), cv2.FILLED)

 
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    
    cv2.imshow("Hand Gesture Mouse", frame)
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()