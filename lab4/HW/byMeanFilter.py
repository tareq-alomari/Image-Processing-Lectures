import cv2
import numpy as np

# 1. الوصول إلى الكاميرا. الرقم 0 يعني الكاميرا الافتراضية.
cap = cv2.VideoCapture(0)

# التحقق مما إذا تم فتح الكاميرا بنجاح
if not cap.isOpened():
    print("خطأ: لا يمكن فتح الكاميرا.")
    exit()

# 2. حلقة مستمرة لقراءة الإطارات من الفيديو
while True:
    # قراءة إطار (frame) من الكاميرا
    # ret تكون True إذا تمت القراءة بنجاح
    ret, frame = cap.read()

    # إذا لم يتم قراءة الإطار بنجاح، نخرج من الحلقة
    if not ret:
        print("لا يمكن استقبال الإطار. يتم الخروج...")
        break

    # 3. تطبيق فلتر المتوسط باستخدام الدالة الجاهزة
    # (frame, (7, 7)) يعني تطبيق الفلتر على الإطار باستخدام نواة بحجم 7x7
    mean_filtered_frame = cv2.blur(frame, (7, 7))

    # 4. عرض الفيديو الأصلي والفيديو المُعالج
    # ندمج الصورتين أفقيًا لعرضهما في نافذة واحدة
    combined_window = np.hstack([frame, mean_filtered_frame])
    cv2.imshow('Original vs. Mean Filter (Built-in)', combined_window)

    # 5. شرط الخروج من الحلقة عند الضغط على مفتاح 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# 6. تحرير الكاميرا وإغلاق جميع النوافذ
cap.release()
cv2.destroyAllWindows()