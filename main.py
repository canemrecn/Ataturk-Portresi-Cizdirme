from sketchpy import canvas
import cv2
# 'a.png' adlı bir görüntünün okunması
im = cv2.imread('a.png')
# Görüntünün boyutunun yazdırılması
print(im.shape)
# 'a.png' adlı görüntüden bir 'canvas' nesnesi oluşturulması
obj = canvas.sketch_from_image('a.png')
# Belirli bir eşik değeriyle eskizi çizme
obj.draw(threshold=100)