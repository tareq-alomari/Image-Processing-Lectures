# المثال الأول: قراءة وعرض وحفظ صورة (بدون تعليق حسب الطلب)
import cv2
img = cv2.imread("speaknow.PNG")
cv2.imshow("image1", img)
cv2.waitKey(0)
cv2.imwrite("speakNow2.PNG", img)
cv2.destroyAllWindows()
