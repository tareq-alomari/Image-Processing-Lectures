import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. قراءة الصورة كصورة رمادية (grayscale)
# image = cv2.imread('images/sunflower.jpg',0)
image = cv2.imread(r"E:\INFORMATION TECHNOLOGY\learn programing\DIP\lab5\images\sunflower.jpg",0)


# 2. تطبيق مرشح سوبل على المحور X
sobelx = cv2.Sobel(image, ddepth=-1, dx=1, dy=0, ksize=5)

# 3. تطبيق مرشح سوبل على المحور Y
sobely = cv2.Sobel(image, ddepth=-1, dx=0, dy=1, ksize=5) # تم تصحيح الخطأ المطبعي

# 4. تطبيق مرشح سوبل على المحورين X و Y معاً
sobelxy = cv2.Sobel(image, ddepth=-1, dx=1, dy=1, ksize=5) # تم تصحيح الخطأ المطبعي

# 5. عرض الصور باستخدام نوافذ OpenCV
cv2.imshow('orginal image',image)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('sobelxy', sobelxy)

# 6. انتظار الضغط على أي مفتاح
cv2.waitKey(0)

# 7. إغلاق جميع النوافذ المفتوحة
cv2.destroyAllWindows()