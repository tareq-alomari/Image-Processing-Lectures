import cv2
import numpy as np

# --- بناء الدالة المخصصة ---
def apply_custom_mean_filter(image, kernel_size):
    """
    تطبق هذه الدالة فلتر المتوسط على صورة باستخدام نواة مخصصة.
    
    Args:
        image: الصورة (الإطار) المراد معالجتها.
        kernel_size (tuple): أبعاد النواة، على سبيل المثال (7, 7).
    
    Returns:
        الصورة بعد تطبيق الفلتر.
    """
    # 1. إنشاء نواة (kernel) فلتر المتوسط
    # النواة هي مصفوفة ممتلئة بالواحدات مقسومة على عدد عناصرها
    k_h, k_w = kernel_size
    mean_kernel = np.ones((k_h, k_w), np.float32) / (k_h * k_w)

    # 2. تطبيق النواة على الصورة باستخدام filter2D
    # ddepth = -1 يعني أن الصورة الناتجة سيكون لها نفس عمق البكسل للأصل
    filtered_image = cv2.filter2D(src=image, ddepth=-1, kernel=mean_kernel)
    
    return filtered_image

# --- الجزء الرئيسي من البرنامج ---

# 3. الوصول إلى الكاميرا
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("خطأ: لا يمكن فتح الكاميرا.")
    exit()

# 4. حلقة مستمرة لقراءة الإطارات
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 5. استدعاء الدالة المخصصة لتطبيق الفلتر
    custom_filtered_frame = apply_custom_mean_filter(frame, kernel_size=(7, 7))

    # 6. عرض الفيديو الأصلي والفيديو المُعالج
    combined_window = np.hstack([frame, custom_filtered_frame])
    cv2.imshow('Original vs. Mean Filter (Custom Function)', combined_window)
    
    # 7. شرط الخروج عند الضغط على 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# 8. تحرير الموارد
cap.release()
cv2.destroyAllWindows()