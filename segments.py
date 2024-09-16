import numpy as np
import trimesh

segments = np.random.random((100, 2, 3))
print(segments)
trimesh.load_path(segments)
p = trimesh.load_path(segments)

p.show()
