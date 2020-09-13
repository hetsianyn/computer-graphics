# importing necessary modules
import numpy as np
from PIL import Image

# total number of times the process will be repeated
total = 7

# size of the image
size = 3 ** total

# creating an image
square = np.empty([size, size, 3], dtype=np.uint8)
color = np.array([255, 255, 255], dtype=np.uint8)

# filling it black
square.fill(0)

for i in range(0, total + 1):
    stepdown = 3 ** (total - i)
    for x in range(0, 3 ** i):

        # checking for the centremost square
        if x % 3 == 1:
            for y in range(0, 3 ** i):
                if y % 3 == 1:
                    # changing its color
                    square[y * stepdown:(y + 1) * stepdown, x * stepdown:(x + 1) * stepdown] = color

                # saving the image produced
save_file = "sierpinski.jpg"
Image.fromarray(square).save(save_file)

# displaying it in console
i = Image.open("sierpinski.jpg")
i.show()