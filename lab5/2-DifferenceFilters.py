import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(r"E:\INFORMATION TECHNOLOGY\learn programing\DIP\lab5\images\natural.jpg")

# تعريف مرشحات الاتجاهات المختلفة
mask_vertical=np.array([
    [0,1,0],
    [0,1,0],
    [0,-1,0]
]) # تم تصحيح الخطأ المطبعي في الملف الأصلي

mask_horizontal=np.array([
    [0,0,0],
    [1,1,-1],
    [0,0,0]
])

mask_diagonal1=np.array([
    [1,0,0],
    [0,1,0],
    [0,0,-1]
]) # تم تصحيح الخطأ المطبعي في الملف الأصلي

mask_diagonal2=np.array([
    [0,0,1],
    [0,1,0],
    [-1,0,0]
])

# تطبيق المرشحات بشكل متسلسل
sharpened_image1=cv2.filter2D(src=image, ddepth=-1, kernel=mask_vertical)
sharpened_image1=cv2.filter2D(src=sharpened_image1, ddepth=-1, kernel=mask_horizontal)
sharpened_image1=cv2.filter2D(src=sharpened_image1, ddepth=-1, kernel=mask_diagonal1)
sharpened_image1=cv2.filter2D(src=sharpened_image1, ddepth=-1, kernel=mask_diagonal2)

# تحويل الألوان وعرض الصور (بنفس طريقة الكود السابق)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
sharpened_image1 = cv2.cvtColor(sharpened_image1, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1, 2, figsize=(10,4))

axs[0].imshow(image)
axs[0].set_title('orginal image')
axs[1].imshow(sharpened_image1)
axs[1].set_title('sharpened_image1') # تم تصحيح الخطأ المطبعي في الملف الأصلي

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()