import cv2
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Volume setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))

minVol, maxVol = volume.GetVolumeRange()[0], volume.GetVolumeRange()[1]

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if len(lmList) != 0:
                # Thumb tip = 4, Index tip = 8
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]

                # Draw line
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.circle(img, (x1, y1), 10, (0, 255, 0), -1)
                cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)

                # Distance
                length = math.hypot(x2 - x1, y2 - y1)

                # Convert distance → volume
                vol = minVol + (length / 200) * (maxVol - minVol)
                vol = max(minVol, min(maxVol, vol))
                smoothVol = 0
                smoothness = 5

                smoothVol = smoothVol + (vol - smoothVol) / smoothness
                volume.SetMasterVolumeLevel(smoothVol, None)

                # Display
                cv2.putText(img, f'Volume: {int(length)}', (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Volume Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()