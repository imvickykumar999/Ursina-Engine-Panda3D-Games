
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
n=13 #side

class Voxel(Button):
    def __init__(self, position=(0,0,0), 
                 texture='grass',
                 default_color=color.green,
                 ):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            highlight_color=color.red,
            color=default_color,
        )

# garden
for z in range(n):
    for x in range(n):
        voxel = Voxel(position=(x,0,z))

# https://youtu.be/vX4l-qozib8?list=PLmP1LNMzp97pQe1FiGpdOLKeWYfTMZM7n
# w=n
# for i in range(w*w):
#     bud = Entity(model='cube', color=color.orange,
#                  texture='brick')
#     bud.x = i/w
#     bud.z = i%w
#     bud.y=1

# brick maze, need better logic to create bhul-bhulaiya !!!
for y in range(1,3):
    for z in range(0,n,3):
        for x in range(n):
            Voxel(position=(x,y,z), 
                    texture='brick',
                    default_color=color.orange,
                    )

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=100)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, 
                  texture='brick',
                  default_color=color.orange,
                  )
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

# window.fullscreen = 1
player = FirstPersonController(gravity=1)
# https://stackoverflow.com/a/75692459/11493297

def update():
    if player.y < -10:
        player.y = 10

Sky()
app.run()

# ---------------------------

# import df_maze as df
# print(df.returnMaze())

'''
w   c   w   w   w   w   w   w   w   w   w   w   w

w   c   w   c   w   w   c   w   c   w   c   w   w

w   c   c   c   w   w   c   w   c   w   c   c   w

w   w   w   c   w   c   c   w   c   w   c   w   w

w   w   w   c   w   w   c   c   c   c   c   c   w

w   c   c   c   w   w   w   w   w   c   w   w   w

w   w   w   c   w   c   w   w   c   c   c   c   w

w   c   w   c   w   c   w   c   c   w   c   w   w

w   c   c   c   c   c   w   c   w   w   w   w   w

w   w   w   c   w   c   c   c   c   w   w   c   w

w   w   w   w   w   c   w   w   c   c   w   c   w

w   c   c   c   c   c   c   w   w   c   c   c   w

w   w   w   w   w   w   w   w   w   w   w   c   w

[['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['w', 'c', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w'], ['w', 'c', 'c', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w'], ['w', 'w', 'w', 'c', 'w', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'], ['w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'], ['w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'w'], ['w', 'w', 'w', 'c', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'w'], ['w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w', 'c', 'w', 'w'], ['w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'w'], ['w', 'w', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'w', 'c', 'w'], ['w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'w', 'c', 'w'], ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'w'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']]
'''