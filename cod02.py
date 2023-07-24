import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture("correr.mp4")

bodyPoints1 = [19, 15, 13, 11, 23, 25, 27, 29, 31]
bodyPoints2 = [20, 16, 14, 12, 24, 26, 28, 30, 32]
bodyPoints1.extend(bodyPoints2)


def graficar(height, width, xii, yii):
    blank = np.zeros((height, width, 3), np.uint8)
    for i in range(len(xii) - 1):
        if i != 8 and i <= 16:
            cv2.line(
                blank,
                (xii[i], yii[i]),
                (xii[i + 1], yii[i + 1]),
                (255, 255, 255),
                3,
            )
        else:
            cv2.line(blank, (xii[3], yii[3]), (xii[12], yii[12]), (255, 255, 255), 3)
            cv2.line(blank, (xii[4], yii[4]), (xii[13], yii[13]), (255, 255, 255), 3)

    for i in range(len(xii)):
        if i < len(xii) - 2:
            if bodyPoints1[i] % 2 == 0:
                cv2.circle(blank, (xii[i], yii[i]), 6, (255, 255, 255), -1)
            else:
                cv2.circle(blank, (xii[i], yii[i]), 6, (255, 5, 55), -1)
        else:
            cv2.circle(blank, (xii[i], yii[i]), 6, (0, 255, 0), -1)
    cv2.imshow("Frame2", blank)


def drawPoints():
    with mp_pose.Pose(static_image_mode=False, model_complexity=0) as pose:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            xi = []
            yi = []
            if results.pose_landmarks is not None:
                for bodyPart in bodyPoints1:
                    xi.append(int(results.pose_landmarks.landmark[bodyPart].x * width))
                    yi.append(int(results.pose_landmarks.landmark[bodyPart].y * height))
                xm1 = int((xi[3] + xi[12]) / 2)
                ym1 = int((yi[3] + yi[12]) / 2)
                xm2 = int((xi[4] + xi[13]) / 2)
                ym2 = int((yi[4] + yi[13]) / 2)
                xi.extend([xm1, xm2])
                yi.extend([ym1, ym2])
            graficar(height, width, xi, yi)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break


drawPoints()
