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
