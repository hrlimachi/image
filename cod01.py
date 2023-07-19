import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# cap = cv2.VideoCapture("correr.mp4")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_pose.Pose(static_image_mode=False) as pose:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        width, height = 500, 500
        blank_image = np.zeros((height, width, 3), np.uint8)
        if results.pose_landmarks is not None:
            # mp_pose.PoseLandmark.RIGHT_SHOULDER
            bodyNumbers = [11, 13, 15, 23, 25, 27, 12, 14, 16, 24, 26, 28]
            bodyWires = [15, 13, 11, 23, 25, 27, 16, 14, 12, 24, 26, 28]
            xi = []
            yi = []
            for bodyPart in bodyWires:
                xi.append(int(results.pose_landmarks.landmark[bodyPart].x * width))
                yi.append(int(results.pose_landmarks.landmark[bodyPart].y * height))
            # print(xi, yi)
            # cv2.circle(frame, (x1, y1), 6, (255, 255, 255), -1)
            for i in range(len(bodyNumbers)):
                cv2.circle(blank_image, (xi[i], yi[i]), 6, (255, 255, 255), -1)
            for i in range(len(bodyWires) - 1):
                cv2.line(
                    blank_image,
                    (xi[i], yi[i]),
                    (xi[i + 1], yi[i + 1]),
                    (255, 255, 255),
                    3,
                )

        cv2.imshow("Frame", blank_image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
