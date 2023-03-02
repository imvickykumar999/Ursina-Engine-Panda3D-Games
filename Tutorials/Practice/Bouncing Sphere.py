
# https://stackoverflow.com/a/66552214/11493297

from ursina import *

def update():
    global y, speed

    cube.rotation_x += time.dt*50.34
    cube.rotation_y -= time.dt*20.7
    cube.rotation_z -= time.dt*73.29

    y += time.dt*speed*.5
    print(speed)

    if abs(y)>3:
        speed *= -.81
    
    camera.position=(0,y,-25)

app = Ursina()
cube = Entity(model="sphere", 
              color=color.red,
              scale=2.5,
              texture='brick',
              )

y=0
speed=2
app.run()
