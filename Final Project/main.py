import pygame
from typing import Union
from pygame.surface import SurfaceType, Surface
from MazeDrawer import MazeDrawer
from Constants import *

# Initalise Pygame
pygame.init()
pygame.mixer.init()
screen: Union[Surface, SurfaceType] = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Solver")

mazeDrawer: MazeDrawer = MazeDrawer(screen)
mazeDrawer.draw()

# Pygame Loop
running: bool = True
while running:

    for event in pygame.event.get():

        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
