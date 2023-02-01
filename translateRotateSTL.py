import numpy as np
from stl import mesh
import math as math 
stl_data = mesh.Mesh.from_file('cube_mesh_test.stl')
stl_data.rotate([1, 0.0, 0.0], math.radians(90))
stl_data.save('cube_mesh_test_mod.stl')
