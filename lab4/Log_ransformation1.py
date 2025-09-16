# استيراد المكتبات اللازمة
import cv2
import numpy as np

# قراءة الصورة الأصلية بتدرج الرمادي
img = cv2.imread('images/Arithmetic.jpg', 0)

# تحويل نوع بيانات الصورة إلى float32 لتحسين دقة العمليات الحسابية
img_float = np.float32(img)

# حساب الثابت 'c' لضمان بقاء قيم البكسلات ضمن النطاق (0-255)
c = 255 / np.log(1 + np.max(img_float))

# تطبيق معادلة التحويل اللوغاريتمي
image_log = c * np.log(1 + img_float)

# تحويل الصورة الناتجة مرة أخرى إلى نوع uint8 لعرضها
image_log = np.uint8(image_log)

# عرض الصور
cv2.imshow('Original Image', img)
cv2.imshow('Log Transformation', image_log)
cv2.waitKey(0)
cv2.destroyAllWindows()