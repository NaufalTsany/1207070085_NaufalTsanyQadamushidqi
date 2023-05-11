import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
from skimage.util import invert
import numpy as np

img1 = cv2.imread("image/dodo.jfif")
img2 = cv2.imread("image/img-doc2.png")

RGB_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
RGB_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

Cropped1 = RGB_img1.copy()
Cropped1 = Cropped1[0:256,64:320]

Cropped2 = RGB_img2.copy()
Cropped2 = Cropped2[64:256,128:320]

print("img 1 ori shape: ", RGB_img1.shape)
print("img 1 cropped shape: ", Cropped1.shape)

print("img 2 ori shape: ", RGB_img2.shape)
print("img 2 cropped shape: ", Cropped2.shape)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(RGB_img1)
ax[0].set_title("Citra Input 1")

ax[1].imshow(RGB_img2)
ax[1].set_title('Citra Input 2')

ax[2].imshow(Cropped1)
ax[2].set_title("Citra Output 1")

ax[3].imshow(Cropped2)
ax[3].set_title('Citra Output 2')

plt.show()

inv = invert(Cropped1)
print('Shape Input : ', Cropped1.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(Cropped1)
ax[0].set_title("Citra Input")

ax[1].hist(Cropped1.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')

plt.show()

copyImg = Cropped2.copy().astype(float)

height = copyImg.shape[0]
width = copyImg.shape[1]
output1 = np.zeros(copyImg.shape, dtype=np.uint8)

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
        
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(Cropped2)
ax[0].set_title("Citra Input")

ax[1].hist(Cropped2.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1)
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')

plt.show()