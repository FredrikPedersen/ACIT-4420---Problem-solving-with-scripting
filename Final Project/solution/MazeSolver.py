import values.Constants as Constants
from typing import Dict, List, Tuple, Set
from maze.Grid import Grid
from maze.MazeUtils import *
from maze.Cell import Cell
from values.SolutionType import SolutionType
from solution.algorithms.AStar import AStar
from solution.algorithms.RecursiveWalk import RecursiveWalk


class MazeSolver:

    __solutionSteps: List[Tuple[int, int]]
    __solutionType: SolutionType

    def __init__(self, screen: Union[Surface, SurfaceType], solution_type: SolutionType, maze_creation_steps: Dict, solution_start: Tuple[int]):
        grid_instance: Grid = Grid.get_instance()

        self.__screen = screen
        self.__maze_creation_steps: Dict = maze_creation_steps
        self.__solutionType: SolutionType = solution_type
        self.__grid: Dict[Tuple[int, int], Cell] = grid_instance.grid
        self.__solutionStartX: int = solution_start[0]
        self.__solutionStartY: int = solution_start[1]

    # init()

    # ---------- General Solution Functions ---------- #

    def solve_maze(self) -> None:
        self.__solutionSteps = []
        self.__mark_start_exit()
        solution_start_coordinates: Tuple[int, int] = (self.__solutionStartX, self.__solutionStartY)

        if self.__solutionType == SolutionType.BUILD_SOLUTION:
            self.__build_solution()

        if self.__solutionType == SolutionType.RECURSIVE_WALK:
            self.__solutionSteps = RecursiveWalk(solution_start_coordinates).recursive_walk_solution()

        if self.__solutionType == SolutionType.A_STAR:
            self.__solutionSteps = AStar(solution_start_coordinates).a_star_solution()

        self.__draw_solution_cells()

    # solve_maze()

    def __mark_start_exit(self) -> None:
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        draw_maze_cell(self.__solutionStartX, self.__solutionStartY, self.__screen, None, Colour.RED)
        draw_maze_cell(Constants.ROOT_X, Constants.ROOT_Y, self.__screen, None, Colour.GREEN)

    # mark_start_exit()

    def __draw_solution_cells(self, remove: bool = False) -> None:
        """
        Draws a red circle in the center of the cell at position (x, y).
        Used to draw individual steps in the solution path.

        :param remove: Indicate whether the function should be used to remove existing solution cells already drawn
                        on the canvas.
        """
        for step in self.__solutionSteps:
            # Add an offset to place the circle in the center of the cell
            x = step[0] + Constants.CELL_SIZE / 2
            y = step[1] + Constants.CELL_SIZE / 2

            if not remove:
                pygame.draw.circle(self.__screen, Colour.RED.value, (x, y), 3)
            else:
                pygame.draw.circle(self.__screen, Colour.WHITE.value, (x, y), 3)

            pygame.display.update()

            sleep_if_animation(.1)

    # draw_solution_cells()

    # ---------- Build Solution Functions ---------- #

    def __build_solution(self) -> None:
        """
        Creates a solution for the maze by following the key-value pairs generated while building the maze
        back to the entrance.

        The key corresponding to the current value was the previous step in the path. Updates
        (x, y) to equal the previous cell, and continues retracing the steps until it reaches the maze's start.
        """

        x: int = self.__solutionStartX
        y: int = self.__solutionStartY

        # Loop until cell position == Start position
        while (x, y) != (Constants.ROOT_X, Constants.ROOT_Y):
            x, y = self.__maze_creation_steps[x, y]
            self.__solutionSteps.append((x, y))

    # build_solution()