import pygame
from typing import Union
from pygame.surface import SurfaceType, Surface
from maze.MazeDrawer import MazeDrawer
from values.Constants import *
from solution.Testing import Testing

# Initalise Pygame
pygame.init()
pygame.mixer.init()
screen: Union[Surface, SurfaceType] = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Solver")

mazeDrawer: MazeDrawer = MazeDrawer(screen)
mazeDrawer.draw()

#mazeSolver: MazeSolver = MazeSolver(screen, SolutionType.RECURSIVE, mazeDrawer.creation_steps)
#mazeSolver.solve_maze()

solutionTests: Testing = Testing(screen)
solutionTests.solve_maze()


# Pygame Loop
running: bool = True
while running:

    for event in pygame.event.get():

        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
