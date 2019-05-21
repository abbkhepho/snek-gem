from random import randint
from tkinter import *

master = Tk()

C = Canvas(master, bg = "black", height = 480, width = 640)
C.pack()

w = 24
h = 32
x = 0
y = 0
size = 20

snek = [5, 5]
snek_x = snek[0] * size
snek_y = snek[1] * size
coord = snek_x, snek_y, snek_x + size, snek_y + size
Snake = C.create_rectangle(coord, fill = "white")

for row in range(0, w):
    for collumn in range(0, h):
        coord = x, y, x + size, y + size
        x += size
        
        C.create_rectangle(coord)

    y += size
    x = 0

mainloop()