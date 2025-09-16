import cv2
import matplotlib.pyplot as plt
import numpy as np

#image = cv2.imread('images/natural.jpg')
image = cv2.imread(r"E:\INFORMATION TECHNOLOGY\learn programing\DIP\lab5\coins.jpg")

mask1=np.array([
    [0,-1,0],
    [-1,4,-1],
    [0,-1,0]
])

mask2=np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])

mask3=np.array([
    [-2,1,-2],
    [1,4,1],
    [-2,1,-2]
])

sharpened_image1 = cv2.filter2D(src=image, ddepth=-1, kernel=mask1)
sharpened_image2 = cv2.filter2D(src=image, ddepth=-1, kernel=mask2)
sharpened_image3 = cv2.filter2D(src=image, ddepth=-1, kernel=mask3)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
sharpened_image1 = cv2.cvtColor(sharpened_image1, cv2.COLOR_BGR2RGB)
sharpened_image2 = cv2.cvtColor(sharpened_image2, cv2.COLOR_BGR2RGB)
sharpened_image3 = cv2.cvtColor(sharpened_image3, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1, 4, figsize=(10, 4))

axs[0].imshow(image)
axs[0].set_title('orginal image')
axs[1].imshow(sharpened_image1)
axs[1].set_title('sharpened_image1')
axs[2].imshow(sharpened_image2)
axs[2].set_title('sharpened_image2')
axs[3].imshow(sharpened_image3)
axs[3].set_title('sharpened_image3')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()