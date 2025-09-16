# استيراد المكتبات
import cv2
import numpy as np
from matplotlib import pyplot as plt

# قراءة الصورة
img = cv2.imread('images/sunflower.jpg')

# تطبيق فلتر المتوسط باستخدام نواة بحجم 5x5
img_meanfilter = cv2.blur(img, (5, 5))

# تطبيق فلتر جاوس باستخدام نواة بحجم 5x5 والانحراف المعياري 0
img_gaussianfilter = cv2.GaussianBlur(img, (5, 5), 0)

# تحويل الألوان من BGR إلى RGB للعرض
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_mean_rgb = cv2.cvtColor(img_meanfilter, cv2.COLOR_BGR2RGB)
img_gaussian_rgb = cv2.cvtColor(img_gaussianfilter, cv2.COLOR_BGR2RGB)

# إعداد العرض
fig, axs = plt.subplots(1, 3, figsize=(10, 4))

# عرض الصور
axs[0].imshow(img_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(img_mean_rgb)
axs[1].set_title('Mean Filter')
axs[2].imshow(img_gaussian_rgb)
axs[2].set_title('Gaussian Filter')

# إخفاء المحاور
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# عرض المخطط
plt.tight_layout()
plt.show()