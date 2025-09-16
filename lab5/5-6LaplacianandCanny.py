import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. قراءة الصورة باللون الرمادي
image = cv2.imread('images/number.png',0)

# 2. تطبيق تمويه (Blur) لتقليل الضوضاء
img_blur = cv2.GaussianBlur(image, (3,3), 0)

# 3. تطبيق مرشح لابلاسيان
Laplacian = cv2.Laplacian(img_blur,-1)

# 4. تطبيق كاشف الحواف كاني
Canny = cv2.Canny(img_blur, threshold1=100, threshold2=200)

# 5. عرض النتائج باستخدام نوافذ OpenCV
cv2.imshow('orginal image', image)
cv2.imshow('Laplacian', Laplacian)
cv2.imshow('Canny', Canny)

# 6. انتظار الضغط على مفتاح ثم إغلاق النوافذ
cv2.waitKey(0)
cv2.destroyAllWindows()