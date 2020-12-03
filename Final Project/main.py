import sys
from typing import Dict

import pygame

from maze.MazeDrawer import MazeDrawer
from solution.MazeSolver import MazeSolver
from values.Colour import Colour
from values.Constants import *
from values.SolutionType import SolutionType
from gui.GameLoop import GameLoop

# Initalise Pygame

gameLoop: GameLoop = GameLoop.get_instance()
screen = gameLoop.get_screen()
base_font = gameLoop.get_font()
clock = gameLoop.get_clock()

mazeDrawer: MazeDrawer = MazeDrawer(screen)
creation_steps: Dict = mazeDrawer.draw()

mazeSolver: MazeSolver = MazeSolver(screen, SolutionType.BUILD_SOLUTION, creation_steps)
mazeSolver.solve_maze()

mazeSolver.change_solution_type(SolutionType.RECURSIVE)
mazeSolver.change_solution_start(ROOT_X + 20, ROOT_Y + 40)
mazeSolver.solve_maze()

gameLoop.start_loop()

