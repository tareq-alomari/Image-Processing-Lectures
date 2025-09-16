# استيراد المكتبات
import cv2
import numpy as np

# قراءة الصورة المشوشة بتدرج الرمادي
img_noisy = cv2.imread('images/noisysalterpepper.png', 0)

# الحصول على أبعاد الصورة
m, n = img_noisy.shape

# إنشاء مصفوفة جديدة فارغة بنفس الأبعاد
img_new = np.zeros([m, n])

# المرور على كل بكسل في الصورة (باستثناء الحواف)
for i in range(1, m - 1):
    for j in range(1, n - 1):
        # تجميع قيم البكسلات في نافذة 3x3 المحيطة بالبكسل الحالي
        temp = [img_noisy[i-1, j-1], img_noisy[i-1, j], img_noisy[i-1, j+1],
                img_noisy[i, j-1],   img_noisy[i, j],   img_noisy[i, j+1],
                img_noisy[i+1, j-1], img_noisy[i+1, j], img_noisy[i+1, j+1]]
        
        # ترتيب القيم تصاعدياً
        temp = sorted(temp)
        
        # استبدال البكسل المركزي بالقيمة الوسيطة (العنصر الخامس في القائمة المرتبة)
        img_new[i, j] = temp[4]

# تحويل نوع البيانات إلى uint8
img_new = img_new.astype(np.uint8)

# عرض وحفظ الصورة الناتجة
cv2.imshow('Manual Median Filtered', img_new)
cv2.imwrite('new_median_filtered.png', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()