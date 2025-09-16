# الوصول للبكسلات وتحويل أنواع الصور

# استيراد مكتبة OpenCV ومكتبة NumPy
import cv2 as c
import numpy as np

# قراءة صورة ملونة
img = c.imread("speaknow.PNG")

# تحويل الصورة إلى تدرج الرمادي
grayimg = c.cvtColor(img, c.COLOR_BGR2GRAY)

# تحويل الصورة الرمادية إلى صورة ثنائية باستخدام عتبة (threshold)
# أي بكسل بقيمة أكبر من 127 سيصبح 255 (أبيض)، والباقي 0 (أسود)
ret, binaryimg = c.threshold(grayimg, 127, 255, c.THRESH_BINARY)

# عرض الصور
c.imshow("color image", img)
c.imshow("Gray-scale", grayimg)
c.imshow("binary image", binaryimg)

# الانتظار حتى يتم الضغط على أي مفتاح
c.waitKey(0)

# إغلاق جميع النوافذ
c.destroyAllWindows()