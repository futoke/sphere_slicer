import open3d as o3d
from time import sleep

vis = o3d.visualization.Visualizer()
vis.create_window()

pcd = o3d.io.read_point_cloud(f'ply/0000000.ply')
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()

view_control = vis.get_view_control()
view_control.rotate(10.0, 0.0)
view_control.set_zoom(60)

for i in range(1, 909):
    pcd.points = o3d.io.read_point_cloud(f'ply/{i:07d}.ply').points
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()