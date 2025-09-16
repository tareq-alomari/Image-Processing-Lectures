# اقتصاص منطقة الاهتمام (ROI)
# استيراد مكتبة OpenCV
import cv2 as c

# قراءة الصورة الأصلية
img = c.imread('planet_glow.jpg')

# تحديد إحداثيات منطقة الاهتمام (بداية ونهاية الصفوف والأعمدة)
startRow = 155
endRow = 315
startCol = 440
endCol = 596

# اقتصاص المنطقة الأولى
ROI = img[startRow:endRow, startCol:endCol]

# اقتصاص المنطقة الثانية
ROI2 = img[152:295, 211:446]

# عرض الصورة الأصلية والمناطق المقتصة
c.imshow('orginal image', img)
c.imshow('cropping1', ROI)
c.imshow('cropping2', ROI2)

# انتظار الضغط على أي مفتاح
c.waitKey()

# إغلاق جميع النوافذ
c.destroyAllWindows()