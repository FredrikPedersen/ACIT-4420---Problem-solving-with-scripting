import pygame
from typing import Dict
from tkinter import *
from tkinter import ttk
from typing import Union
from maze.MazeDrawer import MazeDrawer
from solution.MazeSolver import MazeSolver
from values.Constants import *
from values.SolutionType import SolutionType
from pygame.surface import SurfaceType, Surface

creationSteps: Dict

root = Tk()
root.title("Maze Solver")

embed = Frame(root, width=200, height=400)  # Creates embed frame for pygame window
embed.grid(columnspan=(600), rowspan=500)   # Adds grid
embed.pack(side=LEFT)   # Pack window to the left

button_window = Frame(root, width=75, height=500)
button_window.pack(side=LEFT)

screen: Union[Surface, SurfaceType] = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.init()
pygame.display.update()
mazeDrawer: MazeDrawer = MazeDrawer(screen)


def draw_maze():
    global creationSteps
    creationSteps = mazeDrawer.draw()


def solve_maze():
    global creationSteps

    if creationSteps is None:
        raise Exception("A maze must be drawn before trying to solve!")
    else:
        maze_solver: MazeSolver = MazeSolver(screen, SolutionType.BUILD_SOLUTION, creationSteps)
        maze_solver.solve_maze()


button1 = Button(button_window, text="Draw", command=draw_maze)
button2 = Button(button_window, text="Solve", command=solve_maze)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

while True:
    root.update()

    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()