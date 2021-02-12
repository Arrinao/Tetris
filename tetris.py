import sys
import pathlib
import random
import time
import tkinter
from tkinter import ttk

game_speed = 0.5
rec_x = rec_y = 25
width = 10
height = 20
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


root = tkinter.Tk()
root.resizable(False, False)

tetris_canvas = tkinter.Canvas(root, width=400, height=800, background='black')
tetris_canvas.grid()

class TetrisGUI:
    def __init__(self, speed, canvas):
        self.speed = speed
        self.canvas = canvas
        self.rect_size = 25

    def draw_board(self):
        """
        Draws the board of rectangles on top of the canvas
        """
        x_gap = 25
        y_gap = 25
        for x in range(10):
            for y in range(20):
                y_gap += 25
                tetris_canvas.create_rectangle(20, 20, 200, 50, fill='red', outline='blue')
            x_gap += 25

    def draw_shape():

        """
        Draws the different shapes on the board
        """



tetris_gui = TetrisGUI(game_speed, root)

x = int(width/2)
y = 0

landed_shapes = [(6, 10)]
shape_choice = []

def shapes():
    shapes = {
        'L': [(x-1, y), (x,y), (x+1, y), (x+1, y+1)],
        'L_rev': [(x-1, y+1), (x-1, y), (x, y), (x+1, y)],
        'O': [(x-1, y), (x, y), (x-1, y+1), (x, y+1)],
        'E': [(x, y), (x-1, y+1), (x, y+1), (x+1, y+1)],
        'Z': [(x-1, y), (x, y), (x, y+1), (x-1, y+1)],
        'Z_rev': [(x+1, y), (x, y), (x, y+1), (x-1, y+1)],
        'I': [(x-2, y), (x-1, y), (x, y), (x+1, y)]
    }
    shape_choice.append(random.choice(list(shapes.values())))
    if len(shape_choice) < 2:
        shape_choice.append(random.choice(list(shapes.values())))
    print(shape_choice)
    shape_mover(shape_choice[0])


def shape_mover(shape_coords):
    time.sleep(0.5)
    for shape in shape_coords:
        print (f'Deleted at {shape[0]}, {shape[1]}.')
    if any((x, y+1) in landed_shapes for (x, y) in shape_coords) or any(y+1 == height for (x, y) in shape_coords):
        for coord in shape_coords:
            landed_shapes.append(coord)
        shape_choice.pop(0)
        print(landed_shapes)
        shapes()
    else:
        shape_coords = [(x, y+1) for x, y in shape_coords]
        for shape in shape_coords:
            print(shape[0], shape[1])
        shape_mover(shape_coords)

def user_input_left(event):
    print('Going left!')
    for (x, y) in shape_coords:
        return (x-1, y)


def user_input_right(event):
    print('Going right!')
    for (x, y) in shape_coords:
        return (x+1, y)


root.bind('<Left>', user_input_left)
root.bind('<Right>', user_input_right)



#tetris_gui.draw_board()
root.mainloop()
shapes()
