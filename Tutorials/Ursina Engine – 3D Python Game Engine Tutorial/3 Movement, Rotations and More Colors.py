
# https://www.youtube.com/watch?v=dyf8ZaH0hC8&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=3

from ursina import *
from random import randint

def update():    
    cube.x = cube.x - time.dt*.073
    cube.y += time.dt*.013
    cube.z -= time.dt*.924

    print('x,y,z : ', cube.x, cube.y, cube.z)

    cube.rotation_x += time.dt*107.34
    cube.rotation_y -= time.dt*20.7
    cube.rotation_z -= time.dt*73.29

    red = randint(0,100)
    green = randint(0,255)
    blue = randint(0,200)
    cube.color = color.rgb(red, green, blue)

app=Ursina()
cube=Entity(model='cube', 
            scale=1.74,
            # color=color.blue,
            )

txt = Text(text='This is rotating and moving cube.',
           color=color.yellow,
           scale=2.56,
           position=(-.6,.04,2.2),
           )

app.run()
