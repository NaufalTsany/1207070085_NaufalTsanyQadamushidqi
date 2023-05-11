# Import library yang digunakan
import numpy as np
import imageio
import matplotlib.pyplot as plt

# Membuat fungsi brighter untuk menu mengatur kecerahan
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)

# Membuat fungsi rgbbrighter untuk menu mengatur kecerahan gambar RGB
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbrightness[y][x] = (red, green, blue)

# Membuat fungsi contrass untuk menu mengatur tingkat kontras gambar
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray *= nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)

# Membuat fungsi autocontrass untuk menu mengatur tingkat kontras gambar secara automatis
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)

# Membaca gambar dengan imageio
img = imageio.imread("image/messi.jfif")

img_height = img.shape[0] # digunakan untuk mendapatkan tinggi (jumlah baris) dari gambar.
img_width = img.shape[1] # digunakan untuk mendapatkan lebar (jumlah kolom) dari gambar.
img_channel = img.shape[2] # digunakan untuk mendapatkan jumlah kanal warna (misalnya 3 untuk gambar RGB).
img_type = img.dtype # digunakan untuk mendapatkan tipe data dari piksel gambar (misalnya uint8 untuk representasi nilai 0-255).

# Membuat matriks kosong dengan ukuran yang sama dengan gambar yang disalin
img_brightness = np.zeros(img.shape, dtype=np.uint8)
img_rgbbrightness = np.zeros(img.shape, dtype=np.uint8)
img_contrass = np.zeros(img.shape, dtype=np.uint8)
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)

# Memanggil fungsi brighter dan menampilkan plot
brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()

# Memanggil fungsi brighter dan menampilkan plot
brighter(100)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()

# Memanggil fungsi rgbbrighter dan menampilkan plot
rgbbrighter(-100)
plt.imshow(img_rgbbrightness)
plt.title("Brightness -100")
plt.show()

# Memanggil fungsi rgbbrighter dan menampilkan plot
rgbbrighter(100)
plt.imshow(img_rgbbrightness)
plt.title("Brightness 100")
plt.show()

# Memanggil fungsi contrass dan menampilkan plot
contrass(2)
plt.imshow(img_contrass)
plt.title("Contrass 2")
plt.show()

# Memanggil fungsi contrass dan menampilkan plot
contrass(3)
plt.imshow(img_contrass)
plt.title("Contrass 3")
plt.show()

# Memanggil fungsi autocontrass dan menampilkan plot
autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")
plt.show()