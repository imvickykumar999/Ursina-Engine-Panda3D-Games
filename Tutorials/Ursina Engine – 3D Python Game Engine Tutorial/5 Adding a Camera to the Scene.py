
from ursina import *

def update():
    global x, speed
    x += time.dt*speed*1.2

    if abs(x)>5:
        speed *= -1
    
    camera.position=(x,1.5,-20)


app = Ursina()

cube = Entity(model="cube", 
              color=color.orange,
              scale=(1,2,5),
              texture='brick',
              )

x=0
speed=1
app.run()
