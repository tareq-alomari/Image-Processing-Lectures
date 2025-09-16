# خصائص الصورة (الشكل والحجم)
import cv2 as c

# قراءة صورة بتدرج الرمادي مباشرةً عن طريق إضافة 0 كمعامل ثانٍ
img_gray = c.imread("speaknow.PNG", 0) # 

# img.shape: تُرجع tuple يحتوي على (عدد الصفوف، عدد الأعمدة) للصور الرمادية
# أو (عدد الصفوف، عدد الأعمدة، عدد القنوات) للصور الملونة
print("shape->dimensions: ", img_gray.shape) # 125]

# img.size: تُرجع العدد الإجمالي للبكسلات في الصورة
print("size->numbers of pixels: ", img_gray.size) # 126]

# img.dtype: تُرجع نوع بيانات بكسلات الصورة، وعادة ما يكون 'uint8'
# 'uint8' تعني عدد صحيح غير سالب مكون من 8 بت (أي قيمة من 0 إلى 255)
print("Type: ", img_gray.dtype) # 127]

# قراءة صورة ملونة
img2_color = c.imread("speaknow.PNG") # 129]
print('image2') # 130]
print("shape->dimensions: ", img2_color.shape) # 131]
print("size->numbers of pixels: ", img2_color.size) # 131]
print("Type: ", img2_color.dtype) # 132]

c.imshow("image", img_gray) # 128]
c.imshow("image2", img2_color) # 133]
c.waitKey(0) # 134]
c.destroyAllWindows() # 135]