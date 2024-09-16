import math
import numpy as np
import matplotlib.pyplot as plt


def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


def split(start, end):
    segments = round(math.dist(start, end))

    x_delta = (end[0] - start[0]) / float(segments)
    y_delta = (end[1] - start[1]) / float(segments)

    points = []

    for i in range(1, segments):
        points.append([round(start[0] + i*x_delta), round(start[1] + i*y_delta)])
    return [start] + points + [end]


line  = [0, 0], [-120, -470]
points = split(*line)

length = 0
for i, point in enumerate(points):
    if i == 0:
        continue
    seg = math.dist(points[i], points[i-1])
    print(seg)
    length += seg
print(length)

for point in points:
    plt.plot(*point, 'ro-')

plt.show()