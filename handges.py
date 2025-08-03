import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

print(mp_hands , hands , mp_draw)

# Define finger tip landmarks
tip_ids = [4, 8, 12, 16, 20]

def get_finger_status(hand_landmarks):
    fingers = []

    # Thumb (tip id 4), compare x
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (tip vs pip), compare y
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def is_ok_sign(landmarks):
    # OK sign: thumb tip close to index tip
    thumb_tip = landmarks.landmark[4]
    index_tip = landmarks.landmark[8]
    dist = np.sqrt((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)
    return dist < 0.05

def is_spock_sign(landmarks):
    # Spock sign: big gap between middle and ring fingers
    fingers_y = [landmarks.landmark[i].y for i in [8, 12, 16, 20]]
    middle_ring_gap = abs(fingers_y[1] - fingers_y[2])
    return middle_ring_gap > 0.05

def classify_gesture(finger_status, landmarks):
    if finger_status == [0, 0, 0, 0, 0]:
        return "Fist "
    elif finger_status == [1, 1, 1, 1, 1]:
        return "Open Palm "
    elif finger_status == [0, 1, 1, 0, 0]:
        return "Victory "
    elif finger_status == [1, 0, 0, 0, 0]:
        return "Thumbs Up "
    elif finger_status == [0, 1, 0, 0, 0]:
        return "Pointing "
    elif finger_status == [1, 1, 0, 0, 1]:
        return "Love/ILY "
    elif finger_status == [0, 1, 0, 0, 1]:
        return "Rock Sign "
    elif finger_status == [0, 1, 1, 1, 1]:
        return "Four Fingers"
    elif finger_status == [0, 1, 1, 1, 0]:
        return "Three Fingers"
    elif is_ok_sign(landmarks):
        return "OK Sign "
    elif is_spock_sign(landmarks):
        return "Spock "
    else:
        return "Unknown"

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip frame for mirror view
    frame = cv2.flip(frame, 1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw landmarks
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # Recognize gesture
            finger_status = get_finger_status(handLms)
            gesture = classify_gesture(finger_status, handLms)

            # Display gesture name
            cv2.putText(frame, gesture, (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (0, 255, 0), 3)

    # Show the video frame
    cv2.imshow("Hand Gesture Recognition", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
