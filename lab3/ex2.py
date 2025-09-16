import cv2

# تحميل مصنفات Haar Cascade المدربة مسبقًا للوجه والعين
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# قراءة الصورة
img = cv2.imread('R.jpeg')
# تغيير حجم الصورة لتسريع المعالجة
img = cv2.resize(img, (500, 500))

# تحويل الصورة إلى تدرج الرمادي لأن الكاشف يعمل عليها
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# كشف الوجوه في الصورة الرمادية
faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

# المرور على كل وجه تم اكتشافه
for (x, y, w, h) in faces:
    # رسم مستطيل أزرق حول الوجه
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # تحديد منطقة الاهتمام (ROI) للوجه فقط
    roi_gray = img_gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    
    # كشف العيون داخل منطقة الوجه
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
    
    # المرور على كل عين تم اكتشافها
    for (ex, ey, ew, eh) in eyes:
        # رسم مستطيل أخضر حول العين
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

# عرض الصورة النهائية
cv2.imshow('image1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()