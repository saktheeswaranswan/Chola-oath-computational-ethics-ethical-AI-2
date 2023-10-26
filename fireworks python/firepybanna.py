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

def create_and_explode_firework(x, y):
    create_firework(x, y, 0, 0, "black")  # Create a point at the click position
    explode_firework(x, y)

def keyPress(event):
    if event.char == 'd':
        x = random.randint(0, 600)  # Random x-coordinate within the canvas
        y = random.randint(0, 600)  # Random y-coordinate within the canvas
        create_and_explode_firework(x, y)

frame.bind("<KeyPress>", keyPress)
frame.focus_set()  # Set focus on the canvas to capture key events
mainloop()

