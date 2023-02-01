import os 
import vtk
from vtk.util import numpy_support
path = os.getcwd()
parts_list = os.listdir(path)
reader_list = []
mapper_list = []
actor_list = []
dimensions_list = []
current_position_list =[]

position_list =[(1/5,0,0),(-1/5,0,0),(0,1/5,0),(0,-1/5,0),(0,0,0)]
orientation_list =[(0,90,45),(0,90,-45),(0,90,135),(0,90,-135),(0,0,0)]
renderer_list = []

for itera in parts_list:
    reader = vtk.vtkSTLReader()
    reader.SetFileName(path +"/"+ itera)
    reader.Update()
    reader_list.append(reader)

    polydata = reader.GetOutput()
    bounds = polydata.GetBounds()
    dimensions_list.append((bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4]))
    
    

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    mapper_list.append(mapper)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    #actor.SetPosition(position_list[parts_list.index(itera)][0],position_list[parts_list.index(itera)][1],position_list[parts_list.index(itera)][2])
    actor.RotateX(orientation_list[parts_list.index(itera)][0])
    actor.RotateY(orientation_list[parts_list.index(itera)][1])
    actor.RotateZ(orientation_list[parts_list.index(itera)][2])
    current_position_list.append(actor.GetPosition())
    actor_list.append(actor)
    axes = vtk.vtkAxesActor()
    axes.SetTotalLength(0.1, 0.1, 0.1)


    
    
combined = vtk.vtkMultiBlockDataSet()
for itera in reader_list :
    combined.SetBlock(reader_list.index(itera), itera.GetOutput())
mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(combined)

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer and render window to display the actor
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(800, 600)

# Start the VTK render loop
render_window.Render()
vtk.vtkRenderWindowInteractor().Start()
