import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import random

rng = default_rng()
size = (100, 100)

img_red = rng.integers(low = 0, high = 255, size = size).astype(np.float32)
img_green = rng.integers(low = 0, high = 255, size = size).astype(np.float32)
img_blue = rng.integers(low = 0, high = 255, size = size).astype(np.float32)
change_rates_red = rng.integers(low = 1, high = 5, size = size).astype(np.float32)
change_rates_green = rng.integers(low = 1, high = 5, size = size).astype(np.float32)
change_rates_blue = rng.integers(low = 1, high = 5, size = size).astype(np.float32)

'''rgb_image = np.stack([img_red, img_green, img_blue], axis = -1)
rgb_image = rgb_image.astype(np.uint8)
average_color = rgb_image.mean(axis=(0,1))
print(average_color)

print("Shape of RGB image array:", rgb_image.shape)
plt.figure(figsize=(5, 5))
plt.imshow(rgb_image)
plt.title("RGB Random Image")
plt.show()'''

plt.ion()

fig, ax = plt.subplots(figsize=(6,6))
ax.set_title("RGB Change Animation")

initial_image = np.stack([img_red, img_green, img_blue], axis= -1).astype(np.float32)
im = ax.imshow(initial_image)

try:
    while True:
        img_red += change_rates_red
        img_green += change_rates_green
        img_blue += change_rates_blue

        img_red %= 255
        img_green %= 255
        img_blue %= 256

        rgb_image = np.stack([img_red, img_green, img_blue], axis = -1)

        im.set_data(rgb_image.astype(np.uint8))

        plt.pause(0.001)
except Exception as e:
    print("\n Window closed, closing the program.")
