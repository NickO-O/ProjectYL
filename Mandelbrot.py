import math
from random import randint
from numba import njit, prange
import numpy as np
from PIL import Image

@njit
def func(img_x, img_y):
    xa, ya, xb, yb = [-2.0, -1.0, 1.0, 1.0]
    # sizex = randint(15, 30) / 10
    # sizey = sizex / img_x * img_y
    # xa, ya = randint(-20, 10) / 10, randint(-10, 10)
    # xa, ya, xb, yb = [xa, ya, xa + sizex, ya + sizey]
    #print(xa, ya, xb, yb)
    colors = [(randint(0, 20) / 10) for i in range(3)]
    #print(colors)
    max_iteration = 255
    palette = [
        (
            int(255 * math.sin(i / 30 + (colors[0]) ** 2)),
            int(255 * math.sin(i / 30 + (colors[1]) ** 2)),
            int(255 * math.sin(i / 30 + (colors[2]) ** 2))
        ) for i in range(max_iteration - 1)
    ]
    palette.append((0, 0, 0))
    im = np.zeros(shape=(img_y, img_x, 3))
    im += 255
    pen = np.array((0, 0, 0))
    for y in prange(img_y):
        zy = y * (yb - ya) / img_y + ya
        for x in prange(img_x):
            zx = x * (xb - xa) / img_x + xa
            c, z = zx + zy * 1j, 0
            for cnt in prange(max_iteration):
                if abs(z) > 4.0:
                    break
                z = z * z + c

            pen = np.array(palette[cnt])
            im[y, x] = pen.copy()
    return im

def random_fragment(img_x, img_y):
    while True:
        im = func(img_x, img_y)
        alln = 0
        n = 0

        for i in range(im.shape[0]):
            for j in range(im.shape[1]):
                if not im[i, j].any():
                    n += 1
                alln += 1
        #print(alln, n, 'end')
        if n / alln * 100 > 10 and n / alln * 100 < 50:
            break
    return im


def return_binary(img_x, img_y):
    Image.fromarray(np.uint8(random_fragment(img_x, img_y))).convert('RGB').save('mid.png')


if __name__ == '__main__':
    Image.fromarray(np.uint8(random_fragment(600 * 10, 400 * 10))).convert('RGB').save('mandel0.png')