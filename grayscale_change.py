import numpy as np
import matplotlib.pyplot as plt

img = np.array([[255, 160], 
                   [80, 0]], dtype=np.float32)

change_rates = np.array([[1, 1],
                  [1, 1]], dtype=np.float32)

print(img)

plt.ion()

fig, ax = plt.subplots(figsize=(4,4))
plt.title("Grayscale change animation")

im = ax.imshow(img, cmap='gray', vmin = 0, vmax = 255, interpolation = 'nearest')

try:
    while True:
        img = img + change_rates
        mask = img >= 255
        img[mask] = 0
        im.set_data(img)
        plt.pause(0.001)
except Exception as e:
    print("Window closed, finishing program.")
