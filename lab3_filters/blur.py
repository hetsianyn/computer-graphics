from PIL import Image, ImageDraw


# Завантаження зображення
input_image = Image.open("image.png")
input_image.show()
input_pixels = input_image.load()

# Ядро коробчатого лінійного фільтру
box_kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]

# Ядро гаусівського замилення
gaussian_kernel = [[1 / 256, 4 / 256, 6 / 256, 4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256, 4 / 256, 6 / 256, 4 / 256, 1 / 256]]

# Вибір ядра
kernel = gaussian_kernel

# Визначаємо "середину" ядра
offset = len(kernel) // 2

# Створення вихідного зображення
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Обрахунок
for x in range(offset, input_image.width - offset):
    for y in range(offset, input_image.height - offset):
        acc = [0, 0, 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] += pixel[0] * kernel[a][b]
                acc[1] += pixel[1] * kernel[a][b]
                acc[2] += pixel[2] * kernel[a][b]

        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))

output_image.show()
