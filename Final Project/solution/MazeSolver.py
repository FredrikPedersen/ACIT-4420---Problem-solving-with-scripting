import values.Constants as Constants
import heapq
from typing import Dict, List, Tuple
from maze.Grid import Grid
from maze.MazeUtils import *
from maze.Cell import Cell
from values.SolutionType import SolutionType


class MazeSolver:
    __solutionSteps: List[Tuple[int, int]]
    __solutionType: SolutionType
    __movement_cost: int = 10

    def __init__(self, screen: Union[Surface, SurfaceType], solution_type: SolutionType, maze_creation_steps: Dict, solution_start: Tuple[int]):
        grid_instance: Grid = Grid.get_instance()

        self.__screen = screen
        self.__maze_creation_steps: Dict = maze_creation_steps
        self.__solutionType = solution_type
        self.__grid = grid_instance.grid
        self.__solutionStartX = solution_start[0]
        self.__solutionStartY = solution_start[1]

    # init()

    # ---------- General Solution Functions ---------- #

    def solve_maze(self) -> None:
        self.__solutionSteps = []
        self.__mark_start_exit()

        if self.__solutionType == SolutionType.BUILD_SOLUTION:
            self.__build_solution()

        if self.__solutionType == SolutionType.RECURSIVE_WALK:
            self.__recursive_walk_solution()
            self.__solutionSteps.reverse()

        if self.__solutionType == SolutionType.A_STAR:
            self.__a_star_solution()

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

    def __direction_has_wall(self, x: int, y: int, direction: Direction) -> bool:
        return self.__grid[x, y].walls[direction]

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

    def __recursive_walk_solution(self, x: int = -1, y: int = -1) -> bool:
        """
        Recursive path-finding solution to find the exit, prioritizing going left, right, up and then down.
        Keeps going in a direction until a wall is found in the given direction or the given direction is outside the
        maze's boundaries. Function terminates once the maze's entrance is found.

        Note that in combination with a very large or complex maze, this may produce a RecursionError due to maximum
        recursion depth being exceeded.

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
        return not self.__direction_has_wall(x, y, Direction.LEFT) and x - Constants.CELL_SIZE >= Constants.ROOT_X and self.__recursive_walk_solution(x - Constants.CELL_SIZE, y)

    def __check_right(self, x: int, y: int) -> bool:
        return not self.__direction_has_wall(x, y, Direction.RIGHT) and x + Constants.CELL_SIZE <= Constants.MAZE_WIDTH and self.__recursive_walk_solution(x + Constants.CELL_SIZE, y)

    def __check_up(self, x: int, y: int) -> bool:
        return not self.__direction_has_wall(x, y, Direction.UP) and y - Constants.CELL_SIZE >= Constants.ROOT_Y and self.__recursive_walk_solution(x, y - Constants.CELL_SIZE)

    def __check_down(self, x: int, y: int) -> bool:
        return not self.__direction_has_wall(x, y, Direction.DOWN) and y + Constants.CELL_SIZE <= Constants.MAZE_HEIGHT and self.__recursive_walk_solution(x, y + Constants.CELL_SIZE)

    # ---------- A* Solution Functions ---------- #

    def __a_star_solution(self):

        open_cells: List[Tuple[int, Cell]] = list()   # List of cells to explore
        closed_cells = set()  # List of already explored cells

        starting_cell = self.__grid[self.__solutionStartX, self.__solutionStartY]
        open_cells.append((starting_cell.movement_sum, starting_cell))

        while len(open_cells):

            movement_sum, cell = open_cells.pop()
            closed_cells.add(cell)

            if cell is self.__grid[Constants.ROOT_X, Constants.ROOT_Y]:
                print(self.__create_path())

            adjacent_cells: List[Cell] = self.__find_neighbouring_cells(cell)

            for adjacent_cell in adjacent_cells:
                if adjacent_cell not in closed_cells:
                    if (adjacent_cell.movement_sum, adjacent_cell) in open_cells:
                        if adjacent_cell.cost_from_start > cell.cost_from_start + self.__movement_cost:
                            self.__update_cell(adjacent_cell, cell)
                    else:
                        self.__update_cell(adjacent_cell, cell)
                        open_cells.append((adjacent_cell.movement_sum, adjacent_cell))

        return None

    def __create_path(self):
        cell = self.__grid[Constants.ROOT_X, Constants.ROOT_Y]
        path = [(cell.x, cell.y)]

        while cell.parent is not self.__grid[self.__solutionStartX, self.__solutionStartY]:
            cell = cell.parent
            path.append((cell.x, cell.y))

        path.append((self.__solutionStartX, self.__solutionStartY))
        path.reverse()
        return path

    def __calculate_heuristic_cost(self, cell: Cell):
        return self.__movement_cost * (abs(cell.x - Constants.ROOT_X) + abs(cell.y - Constants.ROOT_Y))

    def __find_neighbouring_cells(self, cell: Cell) -> List[Cell]:
        neighbours: List[Cell] = list()
        x = cell.x
        y = cell.y

        if not self.__direction_has_wall(x, y, Direction.LEFT) and x - Constants.CELL_SIZE >= Constants.ROOT_X:
            neighbours.append(self.__grid[x - Constants.CELL_SIZE, y])
        if not self.__direction_has_wall(x, y, Direction.RIGHT) and x + Constants.CELL_SIZE <= Constants.MAZE_WIDTH:
            neighbours.append(self.__grid[x + Constants.CELL_SIZE, y])
        if not self.__direction_has_wall(x, y, Direction.UP) and y - Constants.CELL_SIZE >= Constants.ROOT_Y:
            neighbours.append(self.__grid[x, y - Constants.CELL_SIZE])
        if not self.__direction_has_wall(x, y, Direction.DOWN) and y + Constants.CELL_SIZE <= Constants.MAZE_HEIGHT:
            neighbours.append(self.__grid[x, y + Constants.CELL_SIZE])

        return neighbours

    def __update_cell(self, adjacent_cell: Cell, current_cell: Cell):

        adjacent_cell.cost_from_start = current_cell.cost_from_start + self.__movement_cost
        adjacent_cell.cost_to_end = self.__calculate_heuristic_cost(adjacent_cell)
        adjacent_cell.parent = current_cell


