# https://www.researchgate.net/figure/The-spherical-spiral-with-a-constant-angular-increase-left-and-its-equidistant_fig1_224989037
# https://gist.github.com/justvanrossum/0a1d1997089559062dda
# https://stackoverflow.com/questions/75416188/get-evenly-spaced-points-from-a-curved-shape

import matplotlib.pyplot as plt
import numpy as np
import trimesh
import open3d as o3d

from time import sleep
from itertools import count
from math import sin, cos, acos, pi, log, log2, e


counter = count()


ax = plt.figure().add_subplot(projection='3d')
plt.xlim(-40, 40)
plt.ylim(-40, 40)
ax = plt.gca()
ax.set_zlim(-40, 40)
ax.set_aspect('equal', adjustable='box')


def create_helix(r, num_points, num_turns):
    a_max = 2 * (np.pi * num_turns)

    a = np.linspace(0, a_max, num_points)
    b = -np.pi/2 + (a*np.pi)/a_max

    x = (r/2) * np.cos(a) * np.cos(b)
    y = (r/2) * np.sin(a) * np.cos(b)
    z = -(r/2) * np.sin(b)

    points = np.array([x, y, z])
    return np.transpose(points)


# Производные спирали
def helix_derivative(t):
    h = 1e-5  # Шаг для численного дифференцирования
    return (spiral(t + h) - spiral(t)) / h


# Функция для расчета длины дуги
def arc_length(t):
    dx, dy, dz = spiral_derivative(t)
    return np.sqrt(dx**2 + dy**2 + dz**2)


mesh = trimesh.load_mesh("models/cat-2.stl")
mesh.vertices -= mesh.center_mass

scene = []
layer = 0.5
step = 0.1
width = 0.4

all_points = np.empty(shape=(0, 3))

r0 = 0.5   

pcd_array = []
layer_points = 1
n = 1

while True:
    # Расчет количества точек исходя из отношения площадей сфер
    layer_points *= 1 + (2 / (r0 + n)) + (1 / (r0**2 + 2*r0*n*step + n**2))
    print(int(layer_points))
    points = create_helix(
        layer, 
        int(layer_points), 
        int((pi*layer) / width)
    )

    contained = mesh.contains(points)

    # all_points = np.append(all_points, points[contained], axis=0)
    # trimesh.PointCloud(all_points).export(f'ply/{next(counter):07d}.ply', encoding="ascii")


    # ax.plot(points[:, 0], points[:, 1], points[:, 2])

    # Рисуем точки в numpy
    # ax.scatter(
    #     points[contained][:, 0], 
    #     points[contained][:, 1], 
    #     points[contained][:, 2],
    #     s=0.1
    # )

    # scene += [trimesh.PointCloud(points)]
    # scene += [trimesh.PointCloud(points[contained])]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[contained])
    pcd_array += [pcd]

    n += 1
    layer += step
    print(f"Высота слоя {layer:.2f}")

    if np.all(contained == False):
        break

# print(total_points)
o3d.visualization.draw_geometries(pcd_array)


# points = create_helix(10, 1000, 10)


# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(points)
# o3d.visualization.draw_geometries([pcd])

# trimesh.Scene(scene).show()
# plt.show()