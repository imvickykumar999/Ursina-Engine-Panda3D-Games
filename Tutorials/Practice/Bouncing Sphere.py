
# https://stackoverflow.com/a/66552214/11493297

from ursina import *

def update():
    global y, speed

    cube.rotation_x += time.dt*150.34
    # cube.rotation_y -= time.dt*120.7
    # cube.rotation_z -= time.dt*73.29

    y += time.dt*speed
    print(y, speed)

    if abs(y) > 3:
        speed *= -1

    # camera.position=(0,y,-30)
    cube.y += time.dt*speed

app = Ursina()
cube = Entity(model="sphere", 
              color=color.red,
              scale=2,
              texture='brick',
              )

y=0
speed=1

# time.sleep(1)
app.run()
