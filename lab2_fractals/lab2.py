import matplotlib.pyplot as plt
import numpy as np
import cv2




def is_point_in_path(x: int, y: int, poly) -> bool:
    num = len(poly)
    i = 0
    j = num - 1
    c = False
    for i in range(num):
        if (((poly[i][1] > y) != (poly[j][1] > y)) and
                (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                 (poly[j][1] - poly[i][1]))):
            c = not c
        j = i
    return c




def genTrianglePoints(triangle_verticies, step=0.01):
    x_max, y_max = triangle_verticies.max(axis=0)
    points = []
    for x in np.arange(0, x_max, step=step):
        for y in np.arange(0, y_max, step=step):
            if is_point_in_path(x, y, triangle_verticies):
                points.append(np.array([x, y]))

    return np.array(points)




def plot_img(img, figsize=(10, 10), cmap='gray', save=False):
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    plt.figure(figsize=(10, 10))
    plt.imshow(img, cmap='gray');
    plt.show()
    plt.axis('off');
    if save:
        plt.imsave('fractal.png', img)




def read_matrices_from_file(path, b_scale=1):
    with open(path, 'r') as f:
        n = int(f.readline())
        f.readline()
        res = []
        for i in range(n):
            A = []
            for j in range(2):
                row = [float(item) for item in f.readline().split()]
                A.append(row.copy())

            A = np.array(A)
            B = np.array([float(item) for item in f.readline().split()])
            # B *= b_scale

            res.append([A, B])

            f.readline()

    return res




class Fractal:
    def __init__(self, matrices, img_size=255, n=2):
        self.matrices = matrices
        self.img_size = img_size
        self.img = np.zeros((img_size, img_size, 3), np.uint8)
        self.n = n
        self.i = 0

    def draw_(self, point, level):
        if level == self.n:
            self.fractal_set[self.i] = (point[0], point[1], self.i)
            self.i += 1
        else:
            for i, (A, B) in enumerate(self.matrices):
                new_point = A.dot(point[:2]) + B
                self.draw_(new_point, level + 1)

    def fit(self, start_points):
        self.fractal_set = np.zeros((len(start_points) * len(self.matrices) ** self.n, 3))
        for point in start_points:
            self.draw_(point, 0)

    def gen_img(self):
        self.fractal_set -= self.fractal_set.min(axis=0)
        self.fractal_set /= self.fractal_set.max(axis=0)
        self.fractal_set *= self.img_size - 1

        for point in self.fractal_set:
            x, y = point[:2]
            x, y = int(round(x)), int(round(y))
            clr = (point[2] + 1)
            #             print(clr)
            self.img[x, y] = 255





# points.shape



img_size = 126

matrices = read_matrices_from_file('triangle.txt')

triangleVerticies = np.array([[0, 0],
                              [1, 0],
                              [0.5, np.sin(np.pi / 3)]])
points = genTrianglePoints(triangleVerticies, step=0.01)

fractal = Fractal(matrices, img_size, 3)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img, save=True)



## Other



img_size = 512

matrices = read_matrices_from_file('farn.txt')
points = np.array([[1.5, 1.5]])

fractal = Fractal(matrices, img_size, 8)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img)


img_size = 512

matrices = read_matrices_from_file('leaf.txt')
points = np.array([[1.5, 1.5]])

fractal = Fractal(matrices, img_size, 16)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img)


img_size = 512

matrices = read_matrices_from_file('plant.txt')
points = np.array([[1.5, 1.5]])

fractal = Fractal(matrices, img_size, 9)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img)

img_size = 512

matrices = read_matrices_from_file('snow.txt')
points = np.array([[1.5, 1.5]])

fractal = Fractal(matrices, img_size, 15)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img)


img_size = 512

matrices = read_matrices_from_file('def.txt')
points = np.array([[1.5, 1.5]])

fractal = Fractal(matrices, img_size, 15)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img)



img_size = 512

matrices = read_matrices_from_file('tree.txt')
points = np.array([[1.5, 1.5]])

fractal = Fractal(matrices, img_size, 8)
fractal.fit(points)
fractal.gen_img()
plot_img(fractal.img)



