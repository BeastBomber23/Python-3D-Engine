from gasp import *
import numpy as np

#Settings
back = color.BLACK
dot = color.WHITE
linec = color.GRAY
scale = 200
timestep = 0.05
distance = 2

#Dont mess with the ones below

centerx = 0
centery = 0

angle = 0

points = np.array([

    [-0.5, -0.5, -0.5],
    [0.5, -0.5, -0.5],
    [0.5, 0.5, -0.5],
    [-0.5, 0.5, -0.5],

    [-0.5, -0.5, 0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, 0.5],
    [-0.5, 0.5, 0.5]

])

def draw():

    rotationZ = np.array([ #These have to be inside the function because angle will still static when initiailzing.

        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]

    ])

    rotationX = np.array([

        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)],

    ])

    rotationY = np.array([

        [np.cos(angle), 0, -np.sin(angle)],
        [0, 1, 0],
        [np.sin(angle), 0, np.cos(angle)]

    ])

    projected = []

    for v in points:
        rotatedY = np.matmul(rotationY, v)
        rotatedX = np.matmul(rotationX, rotatedY)
        rotatedZ = np.matmul(rotationZ, rotatedX)

        z = 1 / (distance - rotatedZ[2])
        projection = np.array([

            [z, 0, 0],
            [0, z, 0]

        ])

        projected2d = np.matmul(projection, rotatedZ)
        projected2d = projected2d * scale
        point(projected2d[0], projected2d[1])
        projected.append(projected2d)

    for i in range(4):
        connect(i, (i + 1) % 4, projected)
        connect(i + 4, ((i + 1) % 4) + 4, projected)
        connect(i, i + 4, projected)

def createWindow():
    begin_graphics(width=800, height=600, title="3D Renderer", background=back)
    return 400, 300

def point(x, y):
    Circle((x + centerx, y + centery), 2, True, dot, 5)

def connect(i, j, points):
    a = points[i]
    b = points[j]
    Line((a[0] + centerx, a[1] + centery), (b[0] + centerx, b[1] + centery), linec)

def clear():
    clear_screen()

centerX, centerY = createWindow()
centerx = centerX
centery = centerY

while True:
    draw()
    time.sleep(timestep)
    clear()
    angle = angle + 0.1
