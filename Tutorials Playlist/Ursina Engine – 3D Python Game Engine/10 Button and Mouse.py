
# https://www.youtube.com/watch?v=WajEJsTMH60&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=10

from ursina import *
from random import randint

def printText():
    B.color = color.random_color()

    x = randint(-3,3)*.1
    y = randint(-3,3)*.1

    print_on_screen("Hello",
                    position=(x, y),
                    )

app = Ursina()

B = Button(
        text='Find me',
        text_color=color.red,
        text_origin=(-.3,.4),
        color=color.azure,
        scale=.25,
        icon='sword',
    )

B.on_click = printText
B.tooltip = Tooltip('Click here')

mouse.visible = False
app.run()
