
# https://www.youtube.com/watch?v=IFORdb2vOWo&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=2

from ursina import *

app = Ursina()

cube = Entity(model="cube", 
              scale_x=2,
              scale_y=4,
              scale_z=3,
              position=(3,1,2),
              rotation=(60,30,45),
              color=color.red,
            #   color=color.rgb(255,0,0),
              )

txt = Text(text='This is red cuboid.',
           color=color.green,
           scale=2.56,
           position=(-.1,.3,2.2),
        #    x=-.3,
        #    y=.4,
           )
app.run()
