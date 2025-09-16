import cv2
print(cv2.__version__)

# LAB1: Image processing
# مصدر: [cite: 1]

# --------------------------------------------------
# مقدمة في معالجة الصور و OpenCV
# --------------------------------------------------

# OpenCV هي مكتبة برمجيات مفتوحة المصدر للرؤية الحاسوبية وتعلم الآلة. [cite: 3]
# بدأت OpenCV في إنتل عام 1999 على يد غاري برادسكي وأول إصدار لها كان في عام 2000. [cite: 4]
# OpenCV-Python هي مكتبة بايثون لـ OpenCV، تجمع بين أفضل ميزات واجهة برمجة تطبيقات OpenCV C++ ولغة بايثون. [cite: 5]
# الرؤية الحاسوبية (Computer Vision) هي المجال الذي يسمح لأجهزة الكمبيوتر باكتساب فهم عالي المستوى من الصور الرقمية أو مقاطع الفيديو. [cite: 7]

# --------------------------------------------------
# الأوامر الأساسية وقراءة وعرض الصور
# --------------------------------------------------

# cv.imread(filename, flag): لقراءة صورة من وحدة التخزين. [cite: 28]
# cv.imshow(window_name, Image): لعرض صورة في نافذة. [cite: 29]
# cv.imwrite(filename, Image): لحفظ صورة في وحدة التخزين. [cite: 31]
# cv.waitKey(delay): تنتظر الضغط على أي مفتاح. [cite: 30]
# cv.destroyAllWindows(): لتدمير جميع النوافذ المفتوحة. [cite: 31]

# المثال الأول: قراءة وعرض وحفظ صورة (بدون تعليق حسب الطلب)
# import cv2
# img = cv2.imread("speaknow.PNG")
# cv2.imshow("image1", img)
# cv2.waitKey(0)
# cv2.imwrite("speakNow2.PNG", img)
# cv2.destroyAllWindows()

# --------------------------------------------------
# الوصول للبكسلات وتحويل أنواع الصور
# --------------------------------------------------

import cv2 as c
import numpy as np

# # قراءة صورة ملونة
# img = c.imread("speakNow.PNG") # مصدر: [cite: 76]
# # الوصول إلى قيمة البكسل في الموقع (y=100, x=100)
# # في OpenCV, ترتيب الألوان هو BGR (أزرق, أخضر, أحمر)
# px = img[100, 100] # مصدر: [cite: 77]
# print(px) # مصدر: [cite: 78]
# # طريقة أخرى للوصول إلى كل قناة لونية على حدة
# (B, G, R)= img[100, 50] # مصدر: [cite: 79]
# print(f"R={R}, G={G}, B={B}") # مصدر: [cite: 80, 81, 82]

# --- مثال: التحويل إلى تدرج الرمادي والصورة الثنائية ---

# قراءة صورة الأشجار
# img_trees = c.imread("speakNow.PNG") # مصدر: [cite: 90]

# # تحويل الصورة الملونة إلى صورة بتدرج الرمادي (Grayscale)
# # نستخدم الدالة cvtColor ونحدد نوع التحويل المطلوب وهو COLOR_BGR2GRAY
# grayimg = c.cvtColor(img_trees, c.COLOR_BGR2GRAY) # مصدر: [cite: 92]

# # تحويل الصورة الرمادية إلى صورة ثنائية (Binary) باستخدام حد العتبة (Threshold)
# # الدالة threshold تُرجع قيمتين: الأولى هي قيمة العتبة المستخدمة، والثانية هي الصورة الجديدة
# # أي بكسل بقيمة سطوع أكبر من 127 سيتحول إلى 255 (أبيض)، والباقي إلى 0 (أسود)
# ret, binaryimg = c.threshold(grayimg, 127, 255, c.THRESH_BINARY) # مصدر: [cite: 94]

# # عرض جميع الصور
# c.imshow("color image", img_trees) # مصدر: [cite: 95]
# c.imshow("Gray-scale", grayimg) # مصدر: [cite: 96]
# c.imshow("binary image", binaryimg) # مصدر: [cite: 97]
# c.waitKey(0) # الانتظار حتى يتم الضغط على أي مفتاح
# c.destroyAllWindows() # إغلاق جميع النوافذ

# # --------------------------------------------------
# # خصائص الصورة (الشكل والحجم)
# # --------------------------------------------------

import cv2 as c

# # قراءة صورة بتدرج الرمادي مباشرةً عن طريق إضافة 0 كمعامل ثانٍ
# img_gray = c.imread("speakNow.PNG", 0) # مصدر: [cite: 124]

# # img.shape: تُرجع tuple يحتوي على (عدد الصفوف، عدد الأعمدة) للصور الرمادية
# # أو (عدد الصفوف، عدد الأعمدة، عدد القنوات) للصور الملونة
# print("shape->dimensions: ", img_gray.shape) # مصدر: [cite: 125]

# # img.size: تُرجع العدد الإجمالي للبكسلات في الصورة
# print("size->numbers of pixels: ", img_gray.size) # مصدر: [cite: 126]

# # img.dtype: تُرجع نوع بيانات بكسلات الصورة، وعادة ما يكون 'uint8'
# # 'uint8' تعني عدد صحيح غير سالب مكون من 8 بت (أي قيمة من 0 إلى 255)
# print("Type: ", img_gray.dtype) # مصدر: [cite: 127]

# # قراءة صورة ملونة
# img2_color = c.imread("speakNow.PNG") # مصدر: [cite: 129]
# print('image2') # مصدر: [cite: 130]
# print("shape->dimensions: ", img2_color.shape) # مصدر: [cite: 131]
# print("size->numbers of pixels: ", img2_color.size) # مصدر: [cite: 131]
# print("Type: ", img2_color.dtype) # مصدر: [cite: 132]

# c.imshow("image", img_gray) # مصدر: [cite: 128]
# c.imshow("image2", img2_color) # مصدر: [cite: 133]
# c.waitKey(0) # مصدر: [cite: 134]
# c.destroyAllWindows() # مصدر: [cite: 135]

# # --------------------------------------------------
# # التحكم باستخدام لوحة المفاتيح
# # --------------------------------------------------

import cv2 as c
import sys

# # قراءة الصورة
# img = c.imread("speakNow.PNG", 0) # مصدر: [cite: 155]

# # التحقق مما إذا تم تحميل الصورة بنجاح
# if img is None: # مصدر: [cite: 156]
#     print('Failed to read image from file') # مصدر: [cite: 157]
#     sys.exit(1) # مصدر: [cite: 157]

# c.imshow("image", img) # مصدر: [cite: 158]

# # waitKey(0) تجعل البرنامج ينتظر إلى الأبد حتى يتم الضغط على مفتاح
# # عند الضغط على مفتاح، تُرجع الدالة قيمة ASCII الخاصة به
# k = c.waitKey(0) # مصدر: [cite: 160]

# # قيمة ASCII لمفتاح الخروج (ESC) هي 27
# if k == 27: # مصدر: [cite: 161]
#     # إذا ضغط المستخدم على ESC، أغلق جميع النوافذ
#     c.destroyAllWindows() # مصدر: [cite: 162]
# # ord('s') تُرجع قيمة ASCII لحرف 's'
# elif k == ord('s'): # مصدر: [cite: 163]
#     # إذا ضغط المستخدم على 's'، احفظ الصورة ثم أغلق النوافذ
#     c.imwrite("treesgray.png", img) # مصدر: [cite: 164]
#     c.destroyAllWindows() # مصدر: [cite: 165]

# # --------------------------------------------------
# # قراءة وكتابة الفيديو
# # --------------------------------------------------

import cv2

# VideoCapture يستخدم لفتح ملف فيديو أو كاميرا
videoCapture = cv2.VideoCapture('v1.mp4') # مصدر: [cite: 169]

# isOpened() تتحقق مما إذا كان الفيديو قد فُتح بنجاح
if not videoCapture.isOpened(): # مصدر: [cite: 177]
    print("Error: Could not open video file.") # مصدر: [cite: 171]
    exit() # مصدر: [cite: 171]

# الحصول على معدل الإطارات في الثانية (FPS) من الفيديو الأصلي
fps = videoCapture.get(cv2.CAP_PROP_FPS) # مصدر: [cite: 188]
# الحصول على عرض وارتفاع الإطار
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))) # مصدر: [cite: 189]

# VideoWriter يُستخدم لإنشاء ملف فيديو جديد
# 'mp4v' هو كود الترميز (FourCC) الخاص بفيديو MP4
videoWriter = cv2.VideoWriter('2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, size) # مصدر: [cite: 190, 191]

# قراءة أول إطار من الفيديو
success, frame = videoCapture.read() # مصدر: [cite: 199]

# حلقة تستمر طالما أن هناك إطارات ناجحة للقراءة
while success: # مصدر: [cite: 199]
    # كتابة الإطار الحالي في ملف الفيديو الجديد
    videoWriter.write(frame) # مصدر: [cite: 201]
    # عرض الإطار في نافذة للمعاينة
    cv2.imshow('Video Preview', frame) # مصدر: [cite: 204]

    # قراءة الإطار التالي للاستمرار في الحلقة
    success, frame = videoCapture.read() # مصدر: [cite: 210, 216]
    
    # انتظر لمدة 1 ميلي ثانية، وإذا تم الضغط على 'q' اخرج من الحلقة
    if cv2.waitKey(1) == ord('q'): # مصدر: [cite: 195]
        break # مصدر: [cite: 209]

# تحرير الموارد وإغلاق الملفات والنوافذ بعد الانتهاء
videoCapture.release() # مصدر: [cite: 218]
videoWriter.release() # مصدر: [cite: 219]
cv2.destroyAllWindows() # مصدر: [cite: 220]
print("Video copying completed successfully.") # مصدر: [cite: 221]

# # --------------------------------------------------
# # عرض بث الكاميرا المباشر والخروج عند النقر
# # --------------------------------------------------
# import cv2

# # متغير عالمي لتتبع ما إذا تم النقر بالماوس
# clicked = False # مصدر: [cite: 225]

# # دالة رد نداء (Callback Function) خاصة بالماوس
# # يتم استدعاؤها تلقائياً عند وقوع حدث للماوس داخل النافذة
# def onMouse(event, x, y, flags, param): # مصدر: [cite: 227]
#     global clicked 
#     # إذا كان الحدث هو رفع زر الماوس الأيسر
#     if event == cv2.EVENT_LBUTTONUP: # مصدر: [cite: 229]
#         # قم بتغيير قيمة المتغير إلى True
#         clicked = True # مصدر: [cite: 230]

# # فتح الكاميرا الافتراضية (عادةً كاميرا الويب المدمجة، index 0)
# cameraCapture = cv2.VideoCapture(0) # مصدر: [cite: 231, 242]
# # إنشاء نافذة باسم محدد
# cv2.namedWindow('MyWindow') # مصدر: [cite: 232]
# # ربط دالة رد النداء الخاصة بالماوس مع النافذة التي أنشأناها
# cv2.setMouseCallback('MyWindow', onMouse) # مصدر: [cite: 266]

# print('Showing camera feed. Click window or press any key to stop.') # مصدر: [cite: 250]

# # قراءة الإطار الأول من الكاميرا
# success, frame = cameraCapture.read() # مصدر: [cite: 254]

# # حلقة تستمر طالما:
# # 1. success is True (تمت قراءة الإطار بنجاح)
# # 2. waitKey(1) == -1 (لم يتم الضغط على أي مفتاح)
# # 3. not clicked (لم يتم النقر بالماوس)
# while success and cv2.waitKey(1) == -1 and not clicked: # مصدر: [cite: 257]
#     # عرض الإطار الحالي في النافذة
#     cv2.imshow('MyWindow', frame) # مصدر: [cite: 259]
#     # قراءة الإطار التالي من الكاميرا
#     success, frame = cameraCapture.read() # مصدر: [cite: 262]

# # بعد الخروج من الحلقة، أغلق النافذة وحرر الكاميرا
# cv2.destroyWindow('MyWindow') # مصدر: [cite: 265]
# cameraCapture.release()