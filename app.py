import cv2
import os
from utils.recognition import recognize_faces
from utils.database import mark_attendance

def main():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        name = recognize_faces(frame)
        if name:
            mark_attendance(name)
        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
