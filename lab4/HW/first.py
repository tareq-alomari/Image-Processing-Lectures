import cv2
import os

video_path = "HW_4/1.mp4"


if not os.path.exists(video_path):
    print(f"File not found: {video_path}")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Failed to open the video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or failed to read frame.")
        break

    mean_filtered = cv2.blur(frame, (5, 5))

    cv2.imshow("Original", frame)
    cv2.imshow("Mean Filter (OpenCV)", mean_filtered)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stopped by user.")
        break

cap.release()
cv2.destroyAllWindows()
