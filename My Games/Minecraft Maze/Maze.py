
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
n=20 #side

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

y=0
for z in range(n):
    for x in range(n):
        Voxel(position=(x,y,z))

import maze_generator as mzg
y_maze = mzg.returnMaze(n,n)

y=1
# for y in range(1,3):
for z in range(len(y_maze)):
    for x in range(len(y_maze[z])):

        if y_maze[z][x] == 'w':
            voxel = Voxel(position=(x,y,z), 
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
    # if key == 'right mouse down' and mouse.hovered_entity:
    #     destroy(mouse.hovered_entity)


# window.fullscreen = 1
player = FirstPersonController(gravity=1)

def update():
    # print(player.x, player.z)

    if player.x > n-2 and player.z > n-2:
        print_on_screen("You Won", position=(0,0))
        
    if player.y < -10:
        player.y = 10

Sky()
app.run()
