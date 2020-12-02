import time
from typing import Dict
from SolutionType import SolutionType
from MazeUtils import *


class MazeSolver:

    __solutionStartX = GRID_WIDTH * CELL_SIZE
    __solutionStartY = GRID_HEIGHT * CELL_SIZE

    def __init__(self, screen: Union[Surface, SurfaceType], solution_type: SolutionType, maze_creation_steps: Dict):
        self.__screen = screen
        self.__solution: Dict = maze_creation_steps
        self.__solution_type = solution_type
    # init()

    # ---------- General Solution Functions ---------- #

    def solve_maze(self):
        self.__mark_start_exit()

        if self.__solution_type == SolutionType.RECURSIVE:
            self.__draw_recursive_solution()

    def __mark_start_exit(self):
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        draw_maze_cell(self.__solutionStartX, self.__solutionStartY, self.__screen, None, Colour.RED)
        draw_maze_cell(ROOT_X, ROOT_Y, self.__screen, None, Colour.GREEN)

    # mark_start_exit()

    def __draw_solution_cell(self, x, y) -> None:
        """
        Draws a red circle in the center of the cell at position (x, y).
        Used to draw individual steps in the solution path.

        :param x: x-coordinate to draw circle on
        :param y: x-coordinate to draw circle on
        """

        # Add an offset to place the circle in the center of the cell
        x += CELL_SIZE / 2
        y += CELL_SIZE / 2
        pygame.draw.circle(self.__screen, Colour.RED.value, (x, y), 3)
        pygame.display.update()
    # draw_solution_cell()

    # ---------- Recursive Solution Functions ---------- #

    def __draw_recursive_solution(self) -> None:
        """
        Draws the recursive solution for the maze by following the key-value pairs back to the beginning. The key
        corresponding to the current value was the previous step in the path. Updates (x, y) to equal the previous
        cell, and continues retracing the steps until it reaches the maze's start.
        :return:
        """

        x: int = self.__solutionStartX
        y: int = self.__solutionStartY

        # Loop until cell position == Start position
        while (x, y) != (ROOT_X, ROOT_Y):
            x, y = self.__solution[x, y]
            self.__draw_solution_cell(x, y)
            time.sleep(.1)
    # draw_recursive_functions
