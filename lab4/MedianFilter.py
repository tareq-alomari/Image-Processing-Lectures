# استيراد المكتبات
import cv2
from matplotlib import pyplot as plt

# قراءة الصورة التي تحتوي على تشويش
img = cv2.imread('images/noisysalterpepper.png')

# تطبيق فلتر الوسيط بنواة بحجم 5
img_medianfilter = cv2.medianBlur(img, 5)

# تحويل الألوان للعرض
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_median_rgb = cv2.cvtColor(img_medianfilter, cv2.COLOR_BGR2RGB)

# إعداد العرض
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# عرض الصور
axs[0].imshow(img_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(img_median_rgb)
axs[1].set_title('Median Filter')

# إخفاء المحاور
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()