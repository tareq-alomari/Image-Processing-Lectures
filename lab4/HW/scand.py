import cv2
import numpy as np
import os

def mean_filter(img, ksize=5):
    if img is None:
        raise ValueError("Input image is None")

    if ksize < 1 or ksize % 2 == 0:
        raise ValueError("Kernel size must be a positive odd number")

    pad = ksize // 2
    padded_img = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0)
    output = np.zeros_like(img)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                region = padded_img[y:y+ksize, x:x+ksize, c]
                output[y, x, c] = np.mean(region)

    return output.astype(np.uint8)

video_path = "HW_4/1.mp4"

if not os.path.exists(video_path):
    print(f"⚠️ File not found: {video_path}")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("⚠️ Failed to open the video. Check the codec or format.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print(" End of video or failed to read frame.")
        break

    try:
        mean_filtered_manual = mean_filter(frame, ksize=5)
    except Exception as e:
        print(f" Error during filtering: {e}")
        break

    cv2.imshow("Original", frame)
    cv2.imshow("Mean Filter (Manual)", mean_filtered_manual)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(" Stopped by user.")
        break

cap.release()
cv2.destroyAllWindows()
