import cv2
import matplotlib.pyplot as plt

# قراءة الصورة
img = cv2.imread('balloons.jpg')
# تحويل الصورة من BGR إلى RGB لعرضها بشكل صحيح مع Matplotlib
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# تحديد مركز الصورة للتدوير
center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)

# إنشاء مصفوفة التدوير: تدوير بزاوية 30 درجة مع تصغير الحجم إلى 0.7
rotation_matrix = cv2.getRotationMatrix2D(center, 30, 0.7)
# إنشاء مصفوفة تدوير أخرى: تدوير بزاوية 30 درجة بدون تغيير الحجم
rotation_matrix2 = cv2.getRotationMatrix2D(center, 30, 1)

# تطبيق مصفوفة التدوير الأولى على الصورة
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))
# تطبيق مصفوفة التدوير الثانية
rotated_image2 = cv2.warpAffine(image_rgb, rotation_matrix2, (img.shape[1], img.shape[0]))

# إنشاء نافذة لعرض الصور
fig, axs = plt.subplots(1, 3, figsize=(14, 4))

# عرض الصورة الأصلية
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')

# عرض الصورة بعد التدوير والتصغير
axs[1].imshow(rotated_image)
axs[1].set_title('Image Rotation with Scaling')

# عرض الصورة بعد التدوير فقط
axs[2].imshow(rotated_image2)
axs[2].set_title('Image Rotation without Scaling')

# عرض المخطط
plt.show()