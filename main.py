import tkinter as tk
import cv2
import threading
import mediapipe as mp
from playsound import playsound
import concurrent.futures
from random import choice
import os

class MiddleFingerDetector:
    def __init__(self):
        self.running = True
        self.middle_finger = False
        self.voice_lines = [os.path.join('audio', f) for f in os.listdir('audio') if f.endswith('.mp3')]

        self.window = tk.Tk()
        self.window.title("The Gesture")
        frame = tk.Frame(self.window, padx=10, pady=10)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="The Gesture", font=("Arial", 20)).grid(row=0, column=0)
        tk.Label(frame, text="Middle finger detector.").grid(row=1, column=0)
        tk.Button(frame, text="Quit", command=self.close).grid()

        self.hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.camera_thread = threading.Thread(target=self.watch_camera)
        self.camera_thread.start()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()

    def watch_camera(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened() and self.running:
            ret, frame = cap.read()
            if not ret:
                self.close()
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame)

            if results.multi_hand_landmarks and not self.middle_finger:
                for hand_landmarks in results.multi_hand_landmarks:
                    middle_tip = hand_landmarks.landmark[12]
                    middle_pip = hand_landmarks.landmark[10]
                    index_tip = hand_landmarks.landmark[8]
                    index_pip = hand_landmarks.landmark[6]
                    ring_tip = hand_landmarks.landmark[16]
                    ring_pip = hand_landmarks.landmark[14]
                    pinky_tip = hand_landmarks.landmark[20]
                    pinky_pip = hand_landmarks.landmark[18]

                    if middle_tip.y < middle_pip.y and index_tip.y > index_pip.y and ring_tip.y > ring_pip.y and pinky_tip.y > pinky_pip.y:
                        self.middle_finger = True
                        self.pool.submit(self.play_voice)

        cap.release()
        cv2.destroyAllWindows()

    def play_voice(self):
        if self.middle_finger:
            playsound(choice(self.voice_lines))
            self.middle_finger = False

    def close(self):
        self.running = False
        self.pool.shutdown(wait=False)
        self.window.quit()

if __name__ == "__main__":
    app = MiddleFingerDetector()