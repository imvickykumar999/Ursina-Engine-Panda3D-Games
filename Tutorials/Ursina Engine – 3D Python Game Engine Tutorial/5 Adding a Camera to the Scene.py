
from ursina import *

def update():
    global z, speed

    # cube.rotation_x += time.dt*107.34
    cube.rotation_y -= time.dt*20.7
    # cube.rotation_z -= time.dt*73.29

    z -= time.dt*speed

    if abs(z)>5:
        speed *= -1
    
    # camera.position=(x,1.5,-50)
    camera.rotation_z=z*10


app = Ursina()

cube = Entity(model="cube", 
              color=color.orange,
              scale=(1,2,5),
              texture='brick',
              )

z=0
speed=1
app.run()
