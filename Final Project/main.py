from typing import Union

import pygame
from pygame.surface import SurfaceType, Surface

from maze.MazeDrawer import MazeDrawer
from solution.MazeSolver import MazeSolver
from values.Constants import *
from values.SolutionType import SolutionType

# Initalise Pygame
pygame.init()
pygame.mixer.init()
screen: Union[Surface, SurfaceType] = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Solver")

mazeDrawer: MazeDrawer = MazeDrawer(screen)
mazeDrawer.draw()

mazeSolver: MazeSolver = MazeSolver(screen, SolutionType.BUILD_SOLUTION, mazeDrawer.creation_steps)
mazeSolver.solve_maze()

mazeSolver.change_solution_type(SolutionType.RECURSIVE)
mazeSolver.change_solution_start(40, 60)
mazeSolver.solve_maze()



# solutionTests: Testing = Testing(screen, Grid.get_instance())
# solutionTests.solve_maze()


# Pygame Loop
running: bool = True
while running:

    for event in pygame.event.get():

        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
