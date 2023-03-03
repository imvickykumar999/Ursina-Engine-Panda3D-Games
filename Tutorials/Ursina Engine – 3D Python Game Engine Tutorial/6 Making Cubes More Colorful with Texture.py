
from ursina import *

app=Ursina()

def update():
    for entity in cubes:
        entity.rotation_y += time.dt * 100

cubes=[] # used in update function

cube=Entity(model='cube',
            # color=color.blue,
            rotation=(45,45,0),
            texture='static/pabble.png',
            )
cubes.append(cube)

cube2 = Entity(model='cube',
            color=color.red,
            rotation=(45,45,0),
            texture='white_cube',
            position=(2,0,0),
            )
cubes.append(cube2)

cube3 = Entity(model='cube',
            color=color.green,
            rotation=(45,45,0),
            texture='brick',
            position=(-2,0,0),
            )
cubes.append(cube3)

cube4 = Entity(model='cube',
            color=color.orange,
            rotation=(45,45,0),
            texture='radial_gradient',
            position=(0,2,0),
            )
cubes.append(cube4)

cube5 = Entity(model='cube',
            color=color.violet,
            rotation=(45,45,0),
            texture='sky_sunset',
            position=(0,-2,0),
            )
cubes.append(cube5)

app.run()