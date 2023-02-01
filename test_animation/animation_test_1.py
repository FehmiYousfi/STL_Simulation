import vtk
import time
# Create a reader for the STL file
reader = vtk.vtkSTLReader()
reader.SetFileName("/home/fehmi_yousfi/Desktop/Python_STL/Drone_Design.stl")
reader.Update()

# Create a mapper for the STL file
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

# Create an actor for the STL file
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.SetSize(601,601)
render_window.AddRenderer(renderer)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the interactor
python32 interactor.Initialize()
interactor.Start()

# Set the initial position of the STL file
actor.SetPosition(0, 0, 0)
polyData = vtk.vtkProperty

print(polyData)

actor.RotateX(0)
actor.RotateY(0)
actor.RotateZ(0)
# Update the position of the STL file in real-time
for i in range (int(60*(3.14/8))):
    actor.RotateX(i/60)
    actor.RotateY(0)
    actor.RotateZ(0)
    render_window.Render()
for i in range (int(60*(3.14/8))):
    actor.RotateX(0)
    actor.RotateY(i/60)
    actor.RotateZ(0)
    render_window.Render()
for i in range (int(60*(3.14/8))):
    actor.RotateX(0)
    actor.RotateY(0)
    actor.RotateZ(i/60)
    render_window.Render()
