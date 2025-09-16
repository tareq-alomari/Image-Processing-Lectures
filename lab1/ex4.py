# استيراد مكتبة OpenCV ومكتبة sys
import cv2 as c
import sys

# قراءة صورة وتحويلها إلى رمادي مباشرة
img = c.imread("speaknow.PNG", 0)

# التحقق مما إذا تم تحميل الصورة بنجاح
if img is None:
    print('Failed to read image from file')
    sys.exit(1)

# عرض الصورة
c.imshow("image", img)

# انتظار الضغط على مفتاح وتخزينه في المتغير k
k = c.waitKey(0)

# إذا كان المفتاح المضغوط هو ESC (رقمه 27)، أغلق النوافذ
if k == 27:
    c.destroyAllWindows()
# إذا كان المفتاح المضغوط هو 's'، احفظ الصورة ثم أغلق النوافذ
elif k == ord('s'):
    c.imwrite("treesgray.png", img)
    c.destroyAllWindows()