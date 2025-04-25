import cv2

image = cv2.imread("logo.png")

if image is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

h,w,c = image.shape
print(f"Görüntü Boyutları: {w}x{h} piksel, {c} kanal (RGB)")

cv2.imshow("Goruntu",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_logo.jpg", image_gray)

cv2.imshow("Gri Goruntu",image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()