# 1. استدعاء المكتبات اللازمة
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 2. قراءة الصورة
# image = cv2.imread('images/natural.jpg')
image = cv2.imread(r"E:\INFORMATION TECHNOLOGY\learn programing\DIP\lab5\images\natural.jpg")
# image = cv2.imread(r"E:\INFORMATION TECHNOLOGY\learn programing\DIP\lab5\coins.jpg")

# 3. تعريف المرشحات (الماسكات) كمصفوفات NumPy
mask1=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

mask2=np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
])

mask3=np.array([
    [-2,1,-2],
    [1,5,1],
    [-2,1,-2]
])

# 4. تطبيق المرشحات على الصورة الأصلية
sharpened_image1 = cv2.filter2D(src=image, ddepth=-1, kernel=mask1)
sharpened_image2 = cv2.filter2D(src=image, ddepth=-1, kernel=mask2)
sharpened_image3 = cv2.filter2D(src=image, ddepth=-1, kernel=mask3)

# 5. تحويل مساحة الألوان للصور من BGR إلى RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
sharpened_image1 = cv2.cvtColor(sharpened_image1, cv2.COLOR_BGR2RGB)
sharpened_image2 = cv2.cvtColor(sharpened_image2, cv2.COLOR_BGR2RGB)
sharpened_image3 = cv2.cvtColor(sharpened_image3, cv2.COLOR_BGR2RGB)

# 6. إعداد نافذة العرض (Figure) ومحاور الرسم (Axes)
fig, axs = plt.subplots(1, 4, figsize=(10, 4))

# 7. عرض كل صورة في مكانها المخصص وتعيين عنوان لها
axs[0].imshow(image)
axs[0].set_title('orginal image')
axs[1].imshow(sharpened_image1)
axs[1].set_title('sharpened_image1')
axs[2].imshow(sharpened_image2)
axs[2].set_title('sharpened_image2')
axs[3].imshow(sharpened_image3)
axs[3].set_title('sharpened_image3')

# 8. إزالة أرقام المحاور (Ticks) من على الصور
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# 9. تنظيم العرض وإظهار النافذة
plt.tight_layout()
plt.show()