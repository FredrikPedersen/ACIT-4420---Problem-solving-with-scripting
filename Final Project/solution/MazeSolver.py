import values.Constants as Constants
from typing import Dict, List, Tuple
from maze.Grid import Grid
from maze.MazeUtils import *
from values.SolutionType import SolutionType


class MazeSolver:
    __solutionSteps: List[Tuple[int, int]]
    __solutionType: SolutionType

    def __init__(self, screen: Union[Surface, SurfaceType], solution_type: SolutionType, maze_creation_steps: Dict):
        grid_instance: Grid = Grid.get_instance()

        self.__screen = screen
        self.__maze_creation_steps: Dict = maze_creation_steps
        self.__solutionType = solution_type
        self.__grid = grid_instance.grid
        self.__solutionStartX = Constants.MAZE_WIDTH
        self.__solutionStartY = Constants.MAZE_HEIGHT

    # init()

    # ---------- Attribute Modifiers ---------- #
    
    def change_solution_type(self, solution_type: SolutionType):
        self.__solutionType = solution_type
        self.__draw_solution_cells(True)

    # change_solution_type()

    def change_solution_start(self, x: int, y: int) -> None:
        """
        Used for setting a new coordinate for the solution to be calculated from.
        First checks if the parameter coordinates are withing the maze's bounds and not equal to the exit,
        then removes the graphical solution start.

        :param x: new x-coordinate for solution start
        :param y: new y-coordinate for solution start
        """
        if x <= Constants.MAZE_WIDTH and y <= Constants.MAZE_HEIGHT and (x != Constants.ROOT_X and y != Constants.ROOT_Y):
            self.__mark_solution_start(self.__solutionStartX, self.__solutionStartY, True)
            self.__solutionStartX = x
            self.__solutionStartY = y
        else:
            raise Exception("Invalid values for solutionStartX or solutionStartY were given! Please provide values "
                            "confined to the maze's boundaries which are not equal to the entrance's coordinates")

    # change_solution_start()

    # ---------- General Solution Functions ---------- #

    def solve_maze(self) -> None:
        self.__solutionSteps = []
        self.__mark_start_exit()

        if self.__solutionType == SolutionType.BUILD_SOLUTION:
            self.__build_solution()

        if self.__solutionType == SolutionType.RECURSIVE:
            self.__recursive_solution()
            self.__solutionSteps.reverse()

        if self.__solutionType == SolutionType.A_STAR:
            raise Exception("NOT IMPLEMENTED YET!")

        self.__draw_solution_cells()

    # solve_maze()

    def __mark_start_exit(self) -> None:
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        self.__mark_solution_start(self.__solutionStartX, self.__solutionStartY)
        draw_maze_cell(Constants.ROOT_X, Constants.ROOT_Y, self.__screen, None, Colour.GREEN)

    # mark_start_exit()

    def __mark_solution_start(self, x: int, y: int, remove: bool = False) -> None:
        """
        Marks the starting point for the solution in the GUI

        :param x: x-coordinate for the starting point
        :param y: y-coordinate for the starting point
        :param remove: Indicates whether the graphical starting point should be removed.
        """

        if not remove:
            draw_maze_cell(x, y, self.__screen, None, Colour.RED)
        else:
            draw_maze_cell(x, y, self.__screen, None, Colour.WHITE)

    # mark_exit()

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

    # ---------- Recursive Solution Functions ---------- #

    def __recursive_solution(self, x: int = -1, y: int = -1) -> bool:
        """
        Recursive path-finding solution to find the exit, prioritizing going left, right, up and then down.
        Keeps going in a direction until a wall is found in the given direction or the given direction is outside the
        maze's boundaries. Function terminates once the maze's entrance is found.

        :param x: x-coordinate for current cell. Default value used to indicate algorithm start conditions.
        :param y: y-coordinate for current cell. Default value used to indicate algorithm start conditions.
        :return: True if there is another cell in a given direction, false if not. Also returns True when x and y are
                equal to the exit's coordinates, or the current cell has already been visited.
        """
        if x == -1 or y == -1:
            x = self.__solutionStartX
            y = self.__solutionStartY

        if (x, y) == (Constants.ROOT_X, Constants.ROOT_Y):
            self.__solutionSteps.append((x, y))
            return True
        elif self.__grid[x, y].visited_while_solving:
            return False

        self.__grid[x, y].visited_while_solving = True

        if self.__check_left(x, y) or self.__check_right(x, y) or self.__check_up(x, y) or self.__check_down(x, y):
            self.__solutionSteps.append((x, y))
            return True

        return False

    # recursive_solution()

    # Convenience functions for checking each direction in recursive_solution(). Written as separate functions for the sake of readability.
    def __check_left(self, x: int, y: int) -> bool:
        return not self.__grid[x, y].walls[Direction.LEFT] and x - Constants.CELL_SIZE >= Constants.ROOT_X and self.__recursive_solution(x - Constants.CELL_SIZE, y)

    def __check_right(self, x: int, y: int) -> bool:
        return not self.__grid[x, y].walls[Direction.RIGHT] and x + Constants.CELL_SIZE <= Constants.MAZE_WIDTH and self.__recursive_solution(x + Constants.CELL_SIZE, y)

    def __check_up(self, x: int, y: int) -> bool:
        return not self.__grid[x, y].walls[Direction.UP] and y - Constants.CELL_SIZE >= Constants.ROOT_Y and self.__recursive_solution(x, y - Constants.CELL_SIZE)

    def __check_down(self, x: int, y: int) -> bool:
        return not self.__grid[x, y].walls[Direction.DOWN] and y + Constants.CELL_SIZE <= Constants.MAZE_HEIGHT and self.__recursive_solution(x, y + Constants.CELL_SIZE)

    # ---------- A* Solution Functions ---------- #
