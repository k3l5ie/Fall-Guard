import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw
import mediapipe as mp
import collections
import winsound

duration = 1000  # milliseconds
freq = 440  # Hz




#skeleton keypoints
def plot_skeleton_kpts(img, kpts, thickness):
    for i in range(len(kpts) - 1):
        cv.circle(img, kpts[i], 3, (0, 255, 0), thickness)


# Function to draw a rounded rectangle
def draw_border(img, p1, p2, color, thickness, r, d):
    x1, y1 = p1
    x2, y2 = p2


    # Draw the main rectangle
    cv.rectangle(img, p1, p2, color, thickness)


    # Draw the rounded corners
    cv.circle(img, (x1 + r, y1 + r), r, color, thickness)
    cv.circle(img, (x2 - r, y1 + r), r, color, thickness)
    cv.circle(img, (x1 + r, y2 - r), r, color, thickness)
    cv.circle(img, (x2 - r, y2 - r), r, color, thickness)


    # Draw the connecting lines
    cv.line(img, (x1 + r, y1), (x2 - r, y1), color, thickness)
    cv.line(img, (x1 + r, y2), (x2 - r, y2), color, thickness)
    cv.line(img, (x1, y1 + r), (x1, y2 - r), color, thickness)
    cv.line(img, (x2, y1 + r), (x2, y2 - r), color, thickness)


# Function to get coordinates
def get_coord(kpts, index):
    return kpts[index]


# Function to get keypoints from the frame using MediaPipe
def get_pose_keypoints(frame, pose):
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = pose.process(frame_rgb)
    keypoints = []


    if result.pose_landmarks:
        for lm in result.pose_landmarks.landmark:
            keypoints.append((int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])))
    return keypoints


# detect fall based on keypoint angles
class FallAction:
    def __init__(self):
        self.detected_angles = collections.deque(5*[0], 5)


    # def check(self, angle):
    #     self.detected_angles.appendleft(angle)
    #     if all(70 <= i <= 100 for i in self.detected_angles):
    #         print("Fall Detected :)")


# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


# Initialize webcam
play = cv.VideoCapture(1)


# Threshold value
frame_height = int(play.get(cv.CAP_PROP_FRAME_HEIGHT))
thre = (frame_height // 2) * 100


# Initialize fall detection
fall_action = FallAction()


while True:
    ret, frame = play.read()
    if not ret:
        break


    keypoints = get_pose_keypoints(frame, pose)


    if keypoints:
        plot_skeleton_kpts(frame, keypoints, 3)


        # Example bounding box calculation based on keypoints
        xmin, ymin = min([kp[0] for kp in keypoints]), min([kp[1] for kp in keypoints])
        xmax, ymax = max([kp[0] for kp in keypoints]), max([kp[1] for kp in keypoints])
        p1 = (int(xmin), int(ymin))
        p2 = (int(xmax), int(ymax))


        dx = int(xmax) - int(xmin)
        dy = int(ymax) - int(ymin)
        cy = (int(ymin) + int(ymax)) // 2  # To get center
        difference = dy - dx  # Difference between dy and dx
        ph = get_coord(keypoints, 2)[1]  # Example of getting the y-coordinate of the 3rd keypoint


        if ((difference < 0) and (int(ph) > thre)) or (difference < 0):
            draw_border(frame, p1, p2, (34, 61, 247), 10, 25, 24)  # Returns rounded rectangle
            im = Image.fromarray(frame)
            draw = ImageDraw.Draw(im)
            cx, cy = p1[0], p1[1]  # Assuming cx and cy are the coordinates for the icon
            draw.rounded_rectangle((cx - 10, cy - 10, cx + 60, cy + 60), fill=(84, 61, 247), radius=15)
            frame = np.array(im)
            print("Fall Detected :)")
            winsound.Beep(freq, duration)


        # Calculate angle for fall detection
        # if len(keypoints) > 10:
        #     shoulder = keypoints[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        #     hip = keypoints[mp_pose.PoseLandmark.LEFT_HIP.value]
        #     dx = shoulder[0] - hip[0]
        #     dy = shoulder[1] - hip[1]
        #     angle = np.degrees(np.arctan2(dy, dx))
        #     fall_action.check(angle)


    # Display each frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break


play.release()
cv.destroyAllWindows()
print(ret)
