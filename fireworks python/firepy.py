from tkinter import *
import time
import math
import random

master = Tk()
frame = Canvas(master, width=600, height=600, bg="white")
frame.pack()

def create_firework(x, y, length, angle, color):
    x1 = x
    y1 = y
    x2 = x1 + length * math.cos(angle)
    y2 = y1 - length * math.sin(angle)
    frame.create_line(x1, y1, x2, y2, fill=color)

def explode_firework(x, y):
    colors = ["red", "green", "blue", "orange", "purple", "yellow"]
    for _ in range(12):
        angle = random.uniform(0, 2 * math.pi)
        length = random.uniform(20, 100)
        color = random.choice(colors)
        create_firework(x, y, length, angle, color)

def mouseClick(event):
    x, y = event.x, event.y
    create_firework(x, y, 0, 0, "black")
    explode_firework(x, y)

def keyPressed(event):
    if event.char == 'd':
        explode_firework(event.x, event.y)

frame.bind("<Button-1>", mouseClick)
frame.bind("<Key>", keyPressed)

mainloop()

