# استيراد المكتبات
import cv2
import numpy as np

# قراءة الصورة
img = cv2.imread('images/sunflower.jpg')

# إنشاء نواة (kernel) لفلتر المتوسط
# جميع العناصر متساوية ومجموعها يساوي 1
mask = np.ones((5, 5), np.float32) / 25

# تطبيق الفلتر باستخدام دالة filter2D
# ddepth = -1 يعني أن الصورة الناتجة سيكون لها نفس عمق الصورة الأصلية
img_filter = cv2.filter2D(src=img, ddepth=-1, kernel=mask)

# عرض الصور
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image (filter2D)', img_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()