import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    # Convert to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process image
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []

            # Get landmark positions
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            # Draw hand
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Finger tip IDs
            tips = [4, 8, 12, 16, 20]

            fingers = []

            # Thumb (special case)
            if lmList[tips[0]][1] > lmList[tips[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other 4 fingers
            for i in range(1, 5):
                if lmList[tips[i]][2] < lmList[tips[i] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            # Show number on screen
            cv2.putText(img, f'Fingers: {totalFingers}', (20, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Detector", img)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()