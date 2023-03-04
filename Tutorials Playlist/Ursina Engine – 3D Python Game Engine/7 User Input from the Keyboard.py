
# https://www.youtube.com/watch?v=rcqHFqgSgtA&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=7

from ursina import *
from random import randint

def update():
    global speed
    cube.rotation_y += time.dt*speed

def input(key):
    global speed

    if held_keys['r']:
        speed=100
    if held_keys['s']:
        speed=0
        
    if key == 'c':
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        cube.color = color.rgb(red, 
                               green, 
                               blue)

app = Ursina()
cube=Entity(model='cube',
            color=color.red,
            texture='white_cube',
            scale=2,
            )

speed=0
app.run()