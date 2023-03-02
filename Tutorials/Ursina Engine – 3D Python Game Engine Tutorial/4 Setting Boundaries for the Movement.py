
# https://www.youtube.com/watch?v=i1CSwOEWPcA&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=4

from ursina import *

def update():
    global speed, speed2

    cube.rotation_x += time.dt*107.34
    cube.rotation_y -= time.dt*20.7
    cube.rotation_z -= time.dt*73.29

    cube.x=cube.x-time.dt*speed
    if abs(cube.x)>5:
        speed=speed*(-1)

    cube2.y=cube2.y+time.dt*speed2
    if abs(cube2.y)>3:
        speed2=speed2*(-1.02)

app=Ursina()
speed=.6
cube=Entity(model='cube',
            color=color.red,
            scale=1.4
            )
speed2=.41
cube2=Entity(model='sphere',
            color=color.blue,
            # position=(.02,-.1,.03)
            )
app.run()