
# https://www.youtube.com/watch?v=i1CSwOEWPcA&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i&index=4

from ursina import *

def update():
    global speed1, speed2

    cube1.rotation_x -= time.dt*107.34
    cube1.rotation_y += time.dt*speed1*50

    cube1.x += time.dt*speed1*1.05
    sphere1.y += time.dt*speed2

    if abs(cube1.x)>5:
        speed1 *= -1.04

    if abs(sphere1.y)>3:
        speed2 *= -1

app = Ursina()
speed1 = 1.02
speed2 = -1

cube1=Entity(model = 'cube', 
            color = color.red,
            scale=1.2,
            )

sphere1=Entity(model = 'sphere', 
            color = color.blue,
            position=(-.01,.03,-.16),        
            )

app.run()



'''
Speed : -4.222377550487301e+257
Speed : 5.404643264623745e+257
Speed : -6.917943378718394e+257
Speed : 8.854967524759545e+257
Speed : inf
Speed : -inf
Assertion failed: !pos.is_nan() at line 402 of c:\buildslave\sdk-windows-amd64\build\panda\src\pgraph\transformState.cxx
* interrupt by keyboard
'''

# Above `speed` are Last few lines before error 
# for, speed *= -1.58 
# XD...
# https://stackoverflow.com/a/74376546/11493297
# AssertionError: !mat.is_nan() at line 322 of c:\buildslave\sdk-windows-amd64\build\panda\src\pgraph\transformState.cxx
