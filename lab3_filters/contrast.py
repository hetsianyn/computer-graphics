from PIL import Image, ImageDraw

# Завантаження зображення
input_image = Image.open("image.png")
input_image.show()
input_pixels = input_image.load()

# Створення вихідного зображення
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Знаходження мінімум та максимум інтенсивності
imin = 255
imax = 0
for x in range(input_image.width):
    for y in range(input_image.height):
        r, g, b = input_pixels[x, y]
        i = (r + g + b) / 3
        imin = min(imin, i)
        imax = max(imax, i)

# Генерування зображення
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b = input_pixels[x, y]
        # Current luminosity
        i = (r + g + b) / 3
        # New luminosity
        ip = 255 * (i - imin) / (imax - imin)
        r = int(r * ip / i)
        g = int(g * ip / i)
        b = int(b * ip / i)
        draw.point((x, y), (r, g, b))

output_image.show()