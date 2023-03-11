
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
n=20 # side
c=0  # texture index

opt_texture = [
    'arrow_down',
    'arrow_right',
    'brick',
    'circle',
    'circle_outlined',
    'cobblestone',
    'cursor',
    'file_icon',
    'folder',
    'grass',
    'heightmap_1',
    'horizontal_gradient',
    'noise',
    'radial_gradient',
    'reflection_map_3',
    'shore',
    'sky_default',
    'sky_sunset',
    'ursina_logo',
    'ursina_wink_0000',
    'ursina_wink_0001',
    'vertical_gradient',
    'white_cube',
]

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
            highlight_color=color.yellow,
            color=default_color,
        )


import MAZE_generator as mzg
y_maze = mzg.returnMaze(n,n)
# print(y_maze)

import MAZE_solver as mzs
s_maze = mzs.solve_maze(y_maze)
# print(s_maze)

y=0
for z in range(len(s_maze)):
    for x in range(len(s_maze[z])):

        if y_maze[z][x] == 'p':
            Voxel(position=(x,y,z), 
                        texture=opt_texture[c%len(opt_texture)],
                        default_color=color.blue,
                        )
            c+=1
        else:
            voxel = Voxel(position=(x,y,z))
            
# y=1
for y in range(1,3):
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


window.fullscreen = 1
player = FirstPersonController(gravity=.4)

def update():
    # print(player.x, player.z)

    if player.x > n-2 and player.z > n-2:
        print_on_screen("You Won", position=(0,0))
        
    if player.y < -10:
        player.y = 10

Sky()
app.run()
