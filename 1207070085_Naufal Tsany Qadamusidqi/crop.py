# Import library yang digunakan
import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
from skimage.util import invert
import numpy as np

# Membaca gambar dengan OpenCV
img1 = cv2.imread("image/dodo.jfif")
img2 = cv2.imread("image/img-doc2.png")

# Mengubah format warna gambar dari BGR ke RGB
RGB_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
RGB_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Mengambil bagian tertentu dari gambar pertama (crop)
Cropped1 = RGB_img1.copy()
Cropped1 = Cropped1[0:256,64:320]

# Mengambil bagian tertentu dari gambar kedua (crop)
Cropped2 = RGB_img2.copy()
Cropped2 = Cropped2[64:256,128:320]

# Menampilkan informasi mengenai bentuk (shape) gambar asli dan hasil cropping
print("img 1 ori shape: ", RGB_img1.shape)
print("img 1 cropped shape: ", Cropped1.shape)

print("img 2 ori shape: ", RGB_img2.shape)
print("img 2 cropped shape: ", Cropped2.shape)

# Membuat subplot untuk menampilkan gambar dan judulnya
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

# Menampilkan gambar asli pertama
ax[0].imshow(RGB_img1)
ax[0].set_title("Citra Input 1")

# Menampilkan gambar asli kedua
ax[1].imshow(RGB_img2)
ax[1].set_title('Citra Input 2')

# Menampilkan hasil cropping gambar pertama
ax[2].imshow(Cropped1)
ax[2].set_title("Citra Output 1")

# Menampilkan hasil cropping gambar kedua
ax[3].imshow(Cropped2)
ax[3].set_title('Citra Output 2')

# Menampilkan subplot
plt.show()

# Membalikkan (inverting) gambar pertama menggunakan fungsi invert dari scikit-image
inv = invert(Cropped1)

# Menampilkan informasi mengenai bentuk (shape) gambar asli dan hasil flipping
print('Shape Input : ', Cropped1.shape)
print('Shape Output : ',inv.shape)

# Membuat subplot baru untuk menampilkan gambar asli, histogramnya, gambar hasil flipping, dan histogramnya
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

# Menampilkan gambar asli
ax[0].imshow(Cropped1)
ax[0].set_title("Citra Input")

# Menampilkan histogram gambar asli
ax[1].hist(Cropped1.ravel(), bins=256)
ax[1].set_title('Histogram Input')

# Menampilkan gambar hasil flipping
ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

# Menampilkan histogram gambar hasil flipping
ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')

# Menampilkan subplot
plt.show()

# Membuat salinan dari gambar kedua dan mengubahnya menjadi tipe data float
copyImg = Cropped2.copy().astype(float)

# Mengambil dimensi gambar yang disalin
height = copyImg.shape[0]
width = copyImg.shape[1]

# Membuat matriks kosong dengan ukuran yang sama dengan gambar yang disalin
output1 = np.zeros(copyImg.shape, dtype=np.uint8)

# Melakukan peningkatan kecerahan pada setiap piksel gambar
for y in range(0, height-1):
    for x in range(0, width-1):
        red = copyImg[y][x][0]
        red += 100
        if red > 255:
            red = 255
        if red < 0:
            red = 0
        green = copyImg[y][x][1]
        green += 100
        if green > 255:
            green = 255
        if green < 0:
            green = 0
        blue = copyImg[y][x][2]
        blue += 100
        if blue > 255:
            blue = 255
        if blue < 0:
            blue = 0
        output1[y][x] = (red, green, blue)

# Membuat subplot baru untuk menampilkan gambar asli, histogramnya, gambar hasil peningkatan kecerahan, dan histogramnya     
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

#Menampilkan gambar asli
ax[0].imshow(Cropped2)
ax[0].set_title("Citra Input")

# Menampilkan histogram gambar asli
ax[1].hist(Cropped2.ravel(), bins=256)
ax[1].set_title('Histogram Input')

# Menampilkan gambar hasil peningkatan kecerahan
ax[2].imshow(output1)
ax[2].set_title('Citra Output (Brightnes)')

# Menampilkan histogram gambar hasil peningkatan kecerahan
ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')

# Menampilkan subplot
plt.show()