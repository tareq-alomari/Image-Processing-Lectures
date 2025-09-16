import cv2

# قراءة الصورة
image = cv2.imread('planet_glow.jpg')

# تحديد معامل التكبير (ضعف الحجم)
scale_factor_1 = 2.0
# تحديد معامل التصغير (نصف الحجم)
scale_factor_2 = 0.5

# الحصول على أبعاد الصورة الأصلية
height, width = image.shape[:2]

# حساب الأبعاد الجديدة للتكبير
new_height_zoom = int(height * scale_factor_1)
new_width_zoom = int(width * scale_factor_1)
# تكبير الصورة باستخدام استيفاء INTER_CUBIC (جودة عالية)
zoomed_image = cv2.resize(src=image, dsize=(new_width_zoom, new_height_zoom), interpolation=cv2.INTER_CUBIC)

# حساب الأبعاد الجديدة للتصغير
new_height_shrink = int(height * scale_factor_2)
new_width_shrink = int(width * scale_factor_2)
# تصغير الصورة باستخدام استيفاء INTER_AREA (الأفضل للتصغير)
shrink_image = cv2.resize(src=image, dsize=(new_width_shrink, new_height_shrink), interpolation=cv2.INTER_AREA)

# عرض الصور
cv2.imshow('image', image)
cv2.imshow('zoomed image', zoomed_image)
cv2.imshow('Shrink image', shrink_image)

# انتظار الضغط على أي مفتاح
cv2.waitKey()

# إغلاق جميع النوافذ
cv2.destroyAllWindows()