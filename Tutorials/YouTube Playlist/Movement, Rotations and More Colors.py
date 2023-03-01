
# https://www.youtube.com/watch?v=dyf8ZaH0hC8&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=3

from ursina import *
from random import randint

def update():
    cube.x = cube.x - time.dt*.023
    cube.y += time.dt*.13
    cube.z -= time.dt*1.824

    cube.rotation_x += time.dt*47.34
    cube.rotation_y -= time.dt*260.7
    cube.rotation_z += time.dt*7.29

    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    cube.color = color.rgb(red, green, blue)

app=Ursina()
cube=Entity(model='cube', 
            # color=color.blue,
            )

txt = Text(text='This is rotating and moving cube.',
           color=color.yellow,
           scale=2.56,
           position=(-.6,.04,2.2),
           )

app.run()
