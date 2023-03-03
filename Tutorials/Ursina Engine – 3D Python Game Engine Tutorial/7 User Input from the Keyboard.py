
# https://www.youtube.com/watch?v=rcqHFqgSgtA&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=7

from ursina import *
from random import randint

def update():
    if held_keys['d']:
        cube.x += time.dt
    if held_keys['w']:
        cube.y += time.dt
    if held_keys['a']:
        cube.x -= time.dt
    if held_keys['s']:
        cube.y -= time.dt

    if held_keys['r']:
        cube.z += time.dt*10
    if held_keys['f']:
        cube.z -= time.dt*10

    if held_keys['q']:
        cube.rotation_y -= time.dt*100
    if held_keys['e']:
        cube.rotation_z -= time.dt*100
    if held_keys['c']:
        cube.rotation_x -= time.dt*100

    camera.position = (0,0,-30)

app = Ursina()
cube = Entity(model='cube',
              color=color.violet,
              texture='sky_sunset',
              scale=2,
              )

instructions = '''

Camera Angle is Z = -30

    Press w to move up
    Press s to move down
    Press a to move left
    Press d to move right

    Press r to move ahead
    Press f to move back

Press c to rotate in x axis
Press q to rotate in y axis
Press e to rotate in z axis
'''

text = Text(instructions, 
            origin=(-1.3, -.8),
            font='VeraMono.ttf', 
            color=color.yellow,
            resolution=100*Text.size,
            ) 

app.run()