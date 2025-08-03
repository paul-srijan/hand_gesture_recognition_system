
# 🖐️ Real-Time Hand Gesture Recognition using MediaPipe & OpenCV

This Python project uses **MediaPipe** and **OpenCV** to recognize hand gestures in real time from a webcam feed. It detects specific gestures like ✊ **Fist**, ✋ **Open Palm**, 👍 **Thumbs Up**, ✌️ **Victory**, 🤟 **Love Sign**, 🖖 **Spock**, 🤘 **Rock Sign**, 👉 **Pointing**, and 👌 **OK Sign**, based on the position of hand landmarks.

---

## 🧠 Features

* Detects and tracks a single hand using **MediaPipe Hands**.
* Recognizes common hand gestures based on finger positions.
* Real-time gesture classification and display on webcam.
* Can be extended to more gestures or actions (like volume control, mouse control, etc.).

---

## 🔧 Requirements

Install dependencies via pip:

```bash
pip install opencv-python mediapipe numpy
```

---

## 🖼️ Recognized Gestures

| Gesture Name     | Finger Status / Condition                    |
| ---------------- | -------------------------------------------- |
| ✊ Fist           | All fingers down `[0, 0, 0, 0, 0]`           |
| ✋ Open Palm      | All fingers up `[1, 1, 1, 1, 1]`             |
| ✌️ Victory       | Index and middle up `[0, 1, 1, 0, 0]`        |
| 👍 Thumbs Up     | Only thumb up `[1, 0, 0, 0, 0]`              |
| 👉 Pointing      | Only index up `[0, 1, 0, 0, 0]`              |
| 🤟 Love Sign     | Thumb, index, pinky up `[1, 1, 0, 0, 1]`     |
| 🤘 Rock Sign     | Index and pinky up `[0, 1, 0, 0, 1]`         |
| 🖖 Spock         | Gap between middle and ring finger > 0.05    |
| 👌 OK Sign       | Thumb tip close to index tip (`dist < 0.05`) |
| 🖐️ Four Fingers | `[0, 1, 1, 1, 1]`                            |
| Three Fingers    | `[0, 1, 1, 1, 0]`                            |

---

## 📁 Project Structure

```
📂 your_project_folder/
├── 📄 gesture_recognition.py    # Main Python script
```

---

## ▶️ How It Works

1. Uses **MediaPipe Hands** to detect 21 3D landmarks per hand.
2. Compares:

   * **Y-coordinate** (for vertical fingers)
   * **X-coordinate** (for thumb, horizontal)
   * Distance between thumb and index tips for OK sign
   * Gap between fingers for Spock sign
3. Matches finger status to predefined gesture patterns.

---

## 💻 How to Run

1. Make sure your webcam is working.
2. Run the script:

```bash
python gesture_recognition.py
```

3. Wave your hand in front of the camera.
4. Press **`q`** to quit.


## 🚀 Potential Extensions

* Control mouse cursor or volume using gestures.
* Add multi-hand detection (`max_num_hands=2`).
* Train custom gestures using machine learning.
* Save detected gestures to file or trigger actions (e.g., system commands, IoT).

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgments

* [MediaPipe](https://mediapipe.dev/)
* [OpenCV](https://opencv.org/)

---
