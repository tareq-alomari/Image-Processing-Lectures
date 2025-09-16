import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. قراءة الصورة وتحويل مساحة الألوان

# قراءة الصورة من الملف (تأكد من أن المسار صحيح)
img = cv2.imread('balloons.jpg')

# تحويل الصورة من صيغة BGR (المستخدمة في OpenCV) إلى RGB (المستخدمة في Matplotlib)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# --- 2. تحديد أبعاد الإزاحة والمصفوفة ---

# الحصول على أبعاد الصورة
height = image_rgb.shape[0]
width = image_rgb.shape[1]

# تحديد مقدار الإزاحة: 100 بكسل أفقيًا (لليمين) و 70 بكسل رأسيًا (للأسفل)
tx = 100
ty = 70

# إنشاء مصفوفة التحويل للإزاحة
# [[1, 0, tx], [0, 1, ty]]
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

# --- 3. تطبيق الإزاحة على الصورة ---

# استخدام دالة warpAffine لتطبيق مصفوفة الإزاحة على الصورة
translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))

# --- 4. عرض الصور ---

# إنشاء نافذة عرض مكونة من جزأين (1 صف، 2 أعمدة)
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# عرض الصورة الأصلية في الجزء الأول
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[0].axis('off') # لإخفاء المحاور

# عرض الصورة بعد الإزاحة في الجزء الثاني
axs[1].imshow(translated_image)
axs[1].set_title('Image Translation')
axs[1].axis('off') # لإخفاء المحاور

# إظهار نافذة العرض
plt.show()