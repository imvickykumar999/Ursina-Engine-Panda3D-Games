
from ursina import *
from random import randint

def update():
    if held_keys['d']:
        cube.x += time.dt*5
    if held_keys['w']:
        cube.y += time.dt*5
    if held_keys['a']:
        cube.x -= time.dt*5
    if held_keys['s']:
        cube.y -= time.dt*5
        print(held_keys['s'])

def input(key):
    if key == 'r':
        text.origin=(-1.3, -.8)
        text.text = f'''
                    LUDO Game

                    Dice : {randint(1,6)}
                    '''

app = Ursina()
cube = Entity(model='cube',
              color=color.violet,
              texture='sky_sunset',
              scale=2,
              )

instructions = f'''
LUDO Game
'''

text = Text(instructions, 
            font='VeraMono.ttf', 
            color=color.yellow,
            resolution=100*Text.size,
            ) 

app.run()