from PIL import Image, ImageDraw

# Коефіціент
luminosity = 40

# Завантаження зображення
input_image = Image.open("image.png")
input_image.show()
input_pixels = input_image.load()

# Створення вихідного зображення
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Генерація зображення
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b = input_pixels[x, y]
        r = int(r + luminosity)
        g = int(g + luminosity)
        b = int(b + luminosity)
        draw.point((x, y), (r, g, b))

output_image.show()