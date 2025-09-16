import cv2
from matplotlib import pyplot as plt

# قراءة الصورتين
img1 = cv2.imread('balloons.jpg')
img2 = cv2.imread('boat.jpg')

# تحويل الصور إلى RGB للعرض
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# توحيد حجم الصورتين
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))

# مزج الصورتين: 70% من الصورة الأولى و 30% من الصورة الثانية
res = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# إعداد نافذة العرض
fig, axs = plt.subplots(1, 3, figsize=(10, 4))

# عرض الصور
axs[0].imshow(img1)
axs[0].set_title('Image1')
axs[1].imshow(img2)
axs[1].set_title('Image2')
axs[2].imshow(res)
axs[2].set_title('addImage')

# عرض المخطط
plt.show()