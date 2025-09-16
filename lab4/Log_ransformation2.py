# استيراد المكتبات
import cv2
import numpy as np
from matplotlib import pyplot as plt

# قراءة الصورة الملونة
img = cv2.imread('images/varese.jpg')

# تحويل نوع بيانات الصورة إلى float32
img_float = np.float32(img)

# حساب الثابت 'c'
c = 255 / np.log(1 + np.max(img_float))

# تطبيق التحويل اللوغاريتمي
image_log = c * np.log(1 + img_float)

# تحويل نوع البيانات إلى uint8
image_log = np.uint8(image_log)

# تحويل نظام الألوان من BGR إلى RGB للعرض الصحيح باستخدام Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image_log_rgb = cv2.cvtColor(image_log, cv2.COLOR_BGR2RGB)

# إعداد العرض باستخدام Matplotlib
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# عرض الصورة الأصلية
axs[0].imshow(img_rgb)
axs[0].set_title('Original Image')

# عرض الصورة بعد التحويل
axs[1].imshow(image_log_rgb)
axs[1].set_title('Log Transformation')

# إخفاء محاور الإحداثيات
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# عرض المخطط
plt.tight_layout()
plt.show()