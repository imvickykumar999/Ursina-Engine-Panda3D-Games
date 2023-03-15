
from ursina import *
from random import randint
import time

import os
filename = 'Imagine Dragons Believer.mp3'
os.system(filename)

import librosa
y, sr = librosa.load(filename)
t1 = int(time.time())
i=0

app = Ursina()
camera.position = (5,0,-30)

c=0
opt_texture = [
    'sky_default',
    'brick',
    'grass',
    'heightmap_1',
    'horizontal_gradient',
    'noise',
    'radial_gradient',
    'reflection_map_3',
    'shore',
    'sky_sunset',
    'vertical_gradient',
    'white_cube',
]

def update():
    global speed, deatils, cube, c, i
    t2 = int(time.time())
    cube.texture = opt_texture[t2%len(opt_texture)]

    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    cube.color = color.rgb(red, green, blue)
    
    deatils.text = f'''
>>> Details ...
-----------------------------
Time = {(t2-t1)//60} min {(t2-t1)%60} sec
Texture = {str(cube.texture).split('.')[0]}
Speed = {speed}

Coordinate X = {cube.x}
Coordinate Y = {cube.y}
Coordinate Z = {cube.z}
Coordinate W = {cube.scale}
Radius     R = {sqrt((cube.scale.x)**2 + (cube.scale.y)**2 + (cube.scale.z)**2)}

Rotation   X = {cube.rotation_x}
Rotation   Y = {cube.rotation_y}
Rotation   Z = {cube.rotation_z}
'''

    try:
        print(i, sr, y[i], t2-t1)
        cube.scale += (y[i],y[i],y[i])
        i+=int(sr/45)
    except:
        pass

    if held_keys['o']:
        cube.scale += (1,1,1)
    if held_keys['p']:
        cube.scale -= (1,1,1)

    if held_keys['e']:
        speed += 5.0
    if held_keys['q']:
        speed -= 5.0

    cube.rotation_x -= time.dt*speed
    cube.rotation_y -= time.dt*speed
    cube.rotation_z -= time.dt*speed

speed=100.0
cube = Entity(model='sphere',
              color=color.red,
              texture='sky_sunset',
              scale=6,
              )

deatils = Text(origin=(-.6, -.7),
                font='VeraMono.ttf', 
                color=color.red,
                ) 

Sky()
window.fullscreen = 1
app.run()