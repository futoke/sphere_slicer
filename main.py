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


def create_helix_ng(r, seg_num, num_turns=40):
    N = num_turns # Количество витков.
    delta_z = 2*r / seg_num

    x = []
    y = []
    z = []

    i = 1

    while i <= seg_num:
        z_i = -r + i * delta_z
        x_i = r * sin(acos(z_i / r)) * cos(((N * pi * z_i) / r) + 1)
        y_i = r * sin(acos(z_i / r)) * sin(((N * pi * z_i) / r) + 1)
        
        x += [x_i]
        y += [y_i]
        z += [z_i]

        i += 0.1
    return np.array([x, y, z]).transpose()


def merge_points(points, tolerance=1):
    dist = 0
    res = np.empty((0, 3))
    res = np.append(res, points[0].reshape((1, 3)), axis=0)
    
    for idx, _ in enumerate(points):
        if idx + 1 < len(points):
            length = np.linalg.norm(points[idx] - points[idx + 1])
            dist += length
            if dist > tolerance:
                res = np.append(res, points[idx + 1].reshape((1, 3)), axis=0)
                dist = 0
    
    return res


# def test_segments():
    # points = create_helix_ng(30, 1000)
    # print(points.size, points.shape)
    # points = merge_points(points)
    # print(points.size, points.shape)
    # trimesh.PointCloud(points).show()

    # x, y, z = points[:, 0], points[:, 1], points[:, 2]
    # ax.plot(x, y, z)

    # for i in range(0, len(y), 1):
    #     normal = np.array([y[i], y[i], y[i]])
    #     normal = normal / np.linalg.norm(normal)  # Нормализуем вектор нормали

    #     ax.quiver(x[i], y[i], z[i], normal[0], normal[1], normal[2], color='g', length=3, normalize=True)

    # plt.show()
            
# test_segments()

# mesh = trimesh.load_mesh("models/cat-2.stl")
# mesh.vertices -= mesh.center_mass

scene = []
layer = 1
step = 0.1

all_points = np.empty(shape=(0, 3))

POINTS_MULTIPLEXER = 2
TURNS_MULTEPLEXER = 10

# Это для анимации
pcd_array = []

# while True:
#     # Расчет количества точек исходя из отношения площадей сфер
#     layer_points = int(np.pi * (layer**2))
#     points = create_helix(
#         layer, 
#         POINTS_MULTIPLEXER * layer_points, 
#         TURNS_MULTEPLEXER * layer
#     )

#     # points = merge_points(points)
#     contained = mesh.contains(points)

#     all_points = np.append(all_points, points[contained], axis=0)
#     trimesh.PointCloud(all_points).export(f'ply/{next(counter):07d}.ply', encoding="ascii")


#     # ax.plot(points[:, 0], points[:, 1], points[:, 2])

#     # Рисуем точки в numpy
#     # ax.scatter(
#     #     points[contained][:, 0], 
#     #     points[contained][:, 1], 
#     #     points[contained][:, 2],
#     #     s=0.1
#     # )

#     # scene += [trimesh.PointCloud(points)]
#     # scene += [trimesh.PointCloud(points[contained])]

#     pcd = o3d.geometry.PointCloud()
#     pcd.points = o3d.utility.Vector3dVector(points[contained])
#     pcd_array += [pcd]

#     layer += step
#     print(f"Высота слоя {layer:.2f}")

#     if np.all(contained == False):
#         break

# print(total_points)
# o3d.visualization.draw_geometries(pcd_array)


points = create_helix(10, 1000, 10)


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
# pcd.colors = o3d.utility.Vector3dVector(colors/65535)
# pcd.normals = o3d.utility.Vector3dVector(normals)
o3d.visualization.draw_geometries([pcd])

# trimesh.Scene(scene).show()
# plt.show()