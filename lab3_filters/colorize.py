from PIL import Image, ImageDraw

# Сума квадратів між двома пікселями
def distance2(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

color_to_change = (255, 0, 0)
threshold = 190

# Завантаження зображення
input_image = Image.open("image.png")
input_image.show()
input_pixels = input_image.load()

# Створення вихідного зображення
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Генерування зображення
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b = input_pixels[x, y]
        if distance2(color_to_change, input_pixels[x, y]) < threshold ** 2:
            r = int(r * .5)
            g = int(g * .5)
            b = int(b * 1.5)
        draw.point((x, y), (r, g, b))

output_image.show()
