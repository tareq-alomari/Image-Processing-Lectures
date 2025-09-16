# --------------------------------------------------
# عرض بث الكاميرا المباشر والخروج عند النقر
# --------------------------------------------------
import cv2

# متغير عالمي لتتبع ما إذا تم النقر بالماوس
clicked = False # مصدر: [cite: 225]

# دالة رد نداء (Callback Function) خاصة بالماوس
# يتم استدعاؤها تلقائياً عند وقوع حدث للماوس داخل النافذة
def onMouse(event, x, y, flags, param): # مصدر: [cite: 227]
    global clicked 
    # إذا كان الحدث هو رفع زر الماوس الأيسر
    if event == cv2.EVENT_LBUTTONUP: # مصدر: [cite: 229]
        # قم بتغيير قيمة المتغير إلى True
        clicked = True # مصدر: [cite: 230]

# فتح الكاميرا الافتراضية (عادةً كاميرا الويب المدمجة، index 0)
cameraCapture = cv2.VideoCapture(0) # مصدر: [cite: 231, 242]
# إنشاء نافذة باسم محدد
cv2.namedWindow('MyWindow') # مصدر: [cite: 232]
# ربط دالة رد النداء الخاصة بالماوس مع النافذة التي أنشأناها
cv2.setMouseCallback('MyWindow', onMouse) # مصدر: [cite: 266]

print('Showing camera feed. Click window or press any key to stop.') # مصدر: [cite: 250]

# قراءة الإطار الأول من الكاميرا
success, frame = cameraCapture.read() # مصدر: [cite: 254]

# حلقة تستمر طالما:
# 1. success is True (تمت قراءة الإطار بنجاح)
# 2. waitKey(1) == -1 (لم يتم الضغط على أي مفتاح)
# 3. not clicked (لم يتم النقر بالماوس)
while success and cv2.waitKey(1) == -1 and not clicked: # مصدر: [cite: 257]
    # عرض الإطار الحالي في النافذة
    cv2.imshow('MyWindow', frame) # مصدر: [cite: 259]
    # قراءة الإطار التالي من الكاميرا
    success, frame = cameraCapture.read() # مصدر: [cite: 262]

# بعد الخروج من الحلقة، أغلق النافذة وحرر الكاميرا
cv2.destroyWindow('MyWindow') # مصدر: [cite: 265]
cameraCapture.release()