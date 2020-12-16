from typing import Dict, List, Tuple

from maze.Cell import Cell
from maze.Grid import Grid
from utilities.DrawUtills import *
from solution.algorithms.Solution import Solution


class MazeSolver:

    """
    Class used for drawing paths calculated by solution algorithms to the maze.
    """

    __solutionSteps: List[Tuple[int, int]]

    def __init__(self, screen: Union[Surface, SurfaceType], solution: Solution, solution_start: Tuple[int, int]):
        grid_instance: Grid = Grid.get_instance()

        self.__screen = screen
        self.__solution: Solution = solution
        self.__grid: Dict[Tuple[int, int], Cell] = grid_instance.grid
        self.__solutionStartX: int = solution_start[0]
        self.__solutionStartY: int = solution_start[1]
    # __init__()

    def draw_maze_solution(self) -> None:
        self.__mark_start_exit()
        self.__solutionSteps = self.__solution.solve_maze()
        self.__draw_solution_cells()
    # solve_maze()

    def __mark_start_exit(self) -> None:
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        draw_maze_cell(self.__solutionStartX, self.__solutionStartY, self.__screen, None, Colour.RED)
        draw_maze_cell(Constants.ROOT_X, Constants.ROOT_Y, self.__screen, None, Colour.GREEN)
    # mark_start_exit()

    def __draw_solution_cells(self) -> None:
        """
        Draws a red circle in the center of the cell at position (x, y).
        Used to draw individual steps in the solution path.
        """

        for step in self.__solutionSteps:
            # Add an offset to place the circle in the center of the cell
            x = step[0] + Constants.CELL_SIZE / 2
            y = step[1] + Constants.CELL_SIZE / 2

            pygame.draw.circle(self.__screen, Colour.RED.value, (x, y), 3)
            pygame.display.update()

            sleep_if_animation(.1)
    # draw_solution_cells()
