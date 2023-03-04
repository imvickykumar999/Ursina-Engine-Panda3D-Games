
# https://www.youtube.com/watch?v=2Kc64o7i2dQ&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=9

from ursina import *

app=Ursina()

class Player(Entity):
    def __init__(self, x, speed):
        super().__init__()
        
        self.model='cube'
        self.color=color.red
        self.scale_y=2
        self.x=x
        self.speed=speed
        self.texture='white_cube'

    def update(self):
        self.x += held_keys['right arrow']*time.dt*self.speed
        self.x -= held_keys['left arrow']*time.dt*self.speed

    def input(self, key):
        if key=='space':
            self.color = color.random_color()

        if key=='r':
            self.rotation_z += time.dt*500 

        if key=='0':
            Player.reset(self)
        
    def reset(self):
        self.color = color.red
        self.rotation_z = 0
        self.x = x
        

Entity(model='quad',
    #    color=color.green,
       position=(0,0,1),
       scale=1.5,
       rotation=(0,0,45),
       texture='static/pabble.png',
       )

x=-2
speed=10
player = Player(x,speed)

app.run()