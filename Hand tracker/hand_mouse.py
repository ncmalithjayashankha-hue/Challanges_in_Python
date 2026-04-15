import cv2
import mediapipe as mp
import pyautogui
import numpy as np

#Camera
cap = cv2.VideoCapture(0)

#screen size
screen_w, screen_h = pyautogui.size()

#MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) # Mirror View

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            lm_list = []

            for id,lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x *w),int(lm.y *h)
                lm_list.append([id, cx, cy])

            #index finger tip = 8
            x1,y1 = lm_list[8][1],lm_list[8][2]

            #convert camera coords -> screen coords
            screen_x = np.interp(x1, [0,w], [0, screen_w])
            screen_y = np.interp(y1, [0,h], [0, screen_h])

            pyautogui.moveTo(screen_x, screen_y)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Mouse",img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
