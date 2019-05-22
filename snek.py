from random import randint
from tkinter import *
import keyboard
import time

master = Tk()

C = Canvas(master, bg = "black", height = 480, width = 640)
C.pack()

w = 32
h = 24
x = 0
y = 0
size = 20
dir = [0, 0]
map_coord = x, y, x + size, y + size

food_x = 0
food_y = 0
foodsize_x = 0
foodsize_y = 0
food_coord = 0

snek = [5, 5]
snek_body = [[4, 5], [3, 5]]

snek_x = snek[0] * size
snek_y = snek[1] * size
snek_coord = snek_x, snek_y, snek_x + size, snek_y + size
    
def genFood():
    global food_entity
    global food
    food_x = randint(0, w)
    food_y = randint(0, h)
    food = [food_x, food_y]
    foodsize_x = food_x * size
    foodsize_y = food_y * size
    food_coord = foodsize_x, foodsize_y, foodsize_x + size, foodsize_y + size
    food_entity = C.create_rectangle(food_coord, fill = "yellow")

def eatFood():
    del food[0]
    C.delete(food_entity)
    genFood()
 
def move(position):
    dx = position[0] * size 
    dy = position[1] * size
    snek_body.append(snek)
    C.move(Snake, dx, dy)
    snek[0] += position[0]
    snek[1] += position[1]

for row in range(0, w):
    
    for collumn in range(0, h):
        y += size
        
        C.create_rectangle(map_coord)

    x += size
    y = 0

C.update()
genFood()

Snake = C.create_rectangle(snek_coord, fill = "white")

while True:
    if keyboard.is_pressed('w') and dir[1] != 1:
        dir = [0, 0]
        dir[1] = -1
    if keyboard.is_pressed('s') and dir[1] != -1:
        dir = [0, 0]
        dir[1] = 1
    if keyboard.is_pressed('a') and dir[0] != 1:
        dir = [0, 0]
        dir[0] = -1
    if keyboard.is_pressed('d') and dir[0] != -1:
        dir = [0, 0]
        dir[0] = 1

    if snek == food:
        eatFood()

    if snek[0] < 0:
        master.destroy()
    elif snek[0] > 31:
        master.destroy()

    if snek[1] < 0:
        master.destroy()
    elif snek[1] > 23:
        master.destroy()

    time.sleep(0.2)
    move(dir)
    C.update()

mainloop()