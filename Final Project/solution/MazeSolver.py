from typing import Dict, List

from maze.Grid import Grid
from maze.MazeUtils import *
from values.SolutionType import SolutionType


class MazeSolver:

    __solutionStartX = MAZE_WIDTH
    __solutionStartY = MAZE_HEIGHT
    __solutionSteps: List[Tuple[int, int]]

    def __init__(self, screen: Union[Surface, SurfaceType], solution_type: SolutionType, maze_creation_steps: Dict):
        grid_instance: Grid = Grid.get_instance()

        self.__screen = screen
        self.__build_solution: Dict = maze_creation_steps
        self.__solution_type = solution_type
        self.__grid = grid_instance.grid
    # init()

    # ---------- General Solution Functions ---------- #

    def solve_maze(self) -> None:
        self.__solutionSteps = []
        self.__mark_start_exit()

        if self.__solution_type == SolutionType.BUILD_SOLUTION:
            self.__recursive_build_solution()

        if self.__solution_type == SolutionType.RECURSIVE:
            self.__recursive_solution()
            self.__solutionSteps.reverse()

        self.__draw_solution_cells()

    def __mark_start_exit(self) -> None:
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        draw_maze_cell(self.__solutionStartX, self.__solutionStartY, self.__screen, None, Colour.RED)
        draw_maze_cell(ROOT_X, ROOT_Y, self.__screen, None, Colour.GREEN)

    # mark_start_exit()

    def __draw_solution_cells(self) -> None:
        """
        Draws a red circle in the center of the cell at position (x, y).
        Used to draw individual steps in the solution path.
        """

        for step in self.__solutionSteps:

            # Add an offset to place the circle in the center of the cell
            x = step[0] + CELL_SIZE / 2
            y = step[1] + CELL_SIZE / 2

            pygame.draw.circle(self.__screen, Colour.RED.value, (x, y), 3)
            pygame.display.update()

            sleep_if_animation(.1)
    # draw_solution_cells()

    # ---------- Recursive Solution Functions ---------- #

    def __recursive_build_solution(self) -> None:
        """
        Creates a solution for the maze by following the key-value pairs generated while building the maze
        back to the entrance.

        The key corresponding to the current value was the previous step in the path. Updates
        (x, y) to equal the previous cell, and continues retracing the steps until it reaches the maze's start.
        """

        x: int = self.__solutionStartX
        y: int = self.__solutionStartY

        # Loop until cell position == Start position
        while (x, y) != (ROOT_X, ROOT_Y):
            x, y = self.__build_solution[x, y]
            self.__solutionSteps.append((x, y))

    # recursive_build_solution

    def __recursive_solution(self, x=__solutionStartX, y=__solutionStartY) -> bool:
        """
        Recursive path-finding solution to find the exit, prioritizing going left, right, up and then down.
        Keeps going in a direction until a wall is found in the given direction or the given direction is outside the
        maze's boundaries. Function terminates once the maze's entrance is found.

        :param x: x-coordinate for current cell.
        :param y: y-coordinate for current cell.
        :return: true if there is another cell in a given direction, false if not. Also returns true when the exit is
                found, or the current cell has already been visited.
        """

        if (x, y) == (ROOT_X, ROOT_Y):
            return True
        elif self.__grid[x, y].visited_while_solving:
            return False

        self.__grid[x, y].visited_while_solving = True

        if self.__check_left(x, y) or self.__check_right(x, y) or self.__check_up(x, y) or self.__check_down(x, y):
            self.__solutionSteps.append((x, y))
            return True

        return False

    # recursive_solution

    # Convenience functions for readability in recursive_solution
    def __check_left(self, x, y) -> bool:
        return not self.__grid[x, y].walls[Direction.LEFT] and x - CELL_SIZE > 0 and self.__recursive_solution(x - CELL_SIZE, y)

    def __check_right(self, x, y) -> bool:
        return not self.__grid[x, y].walls[Direction.RIGHT] and x + CELL_SIZE <= MAZE_WIDTH and self.__recursive_solution(x + CELL_SIZE, y)

    def __check_up(self, x, y) -> bool:
        return not self.__grid[x, y].walls[Direction.UP] and y - CELL_SIZE > 0 and self.__recursive_solution(x, y - CELL_SIZE)

    def __check_down(self, x, y) -> bool:
        return not self.__grid[x, y].walls[Direction.DOWN] and y + CELL_SIZE <= MAZE_HEIGHT and self.__recursive_solution(x, y + CELL_SIZE)

    # ---------- A* Solution Functions ---------- #
