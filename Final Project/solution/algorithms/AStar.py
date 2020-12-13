from typing import List, Tuple, Set

import values.Constants as Constants
from maze.Cell import Cell
from solution.algorithms.SolutionABC import SolutionABC


class AStar(SolutionABC):

    """
    Class used for solving mazes based on the A* search algorithm.
    Detailed information on the algorithm can be found on Wikipedia by searching for "A* search algorithm".
    """

    __movement_cost: int = 10

    def __init__(self, solution_start: Tuple[int, int]):
        super().__init__(solution_start)

    def solve_maze(self) -> List[Tuple[int, int]]:
        """
        Start by marking the cell where the algorithm shall start searching from as open.

        While there are open cells remaining, do the following with the current cell:
        1: Mark it as closed
            1.1: If the cell is the exit, the algorithm has found the path.
        2: Find all adjacent cells
        3: For each adjacent cell:
            3.1: That is not closed, is already marked as open and has a movement cost larger than the current cell's
                 movement cost + one more step, update both cell's movement cost and set the current cell as the adjacent
                 cell's parent.
            3.2: That is not closed and not marked as open, update both cell's movement cost and set the current cell as
                the adjacent cell's parent, mark the adjacent cell as open.
            3.3: If neither 3.1 or 3.2 applies, an error has occurred in the algorithm logic.

        :return: A list with the coordinates of the cheapest path from the algorithm's start position to the maze's exit.
        """

        closed_cells: Set[Cell] = set()
        open_cells: List[Cell] = list()

        starting_cell = self._grid[self._solutionStartX, self._solutionStartY]
        open_cells.append(starting_cell)

        while len(open_cells):

            cell = open_cells.pop()
            closed_cells.add(cell)

            if cell is self._grid[Constants.ROOT_X, Constants.ROOT_Y]:
                return self.__create_path()

            adjacent_cells: List[Cell] = self.__find_adjacent_cells(cell)

            for adjacent_cell in adjacent_cells:

                if adjacent_cell not in closed_cells:
                    if adjacent_cell in open_cells:
                        if adjacent_cell.cost_from_start > cell.cost_from_start + self.__movement_cost:
                            self.__update_cell(adjacent_cell, cell)
                    else:
                        self.__update_cell(adjacent_cell, cell)
                        open_cells.append(adjacent_cell)

        raise Exception("Something went wrong, Maze Entry not found!")
    # solve_maze()

    def __create_path(self) -> List[Tuple[int, int]]:
        """
        Iterates through all the cells on the cheapest path in the grid from the solution's start coordinates by
        following their parent-cells to the exit.

        :return: A list with the coordinates of the cheapest path from the algorithm's start position to the maze's exit.
        """

        solution_steps: List[Tuple[int, int]] = list()

        cell = self._grid[Constants.ROOT_X, Constants.ROOT_Y]
        solution_steps.append((cell.x, cell.y))

        while cell.parent is not self._grid[self._solutionStartX, self._solutionStartY]:
            cell = cell.parent
            solution_steps.append((cell.x, cell.y))

        solution_steps.append((self._solutionStartX, self._solutionStartY))
        solution_steps.reverse()

        return solution_steps
    # create_path()

    def __find_adjacent_cells(self, cell: Cell) -> List[Cell]:
        """
        Checks for neighbouring cells to the left, right, up and down from the current cell.
        Cells separated by a wall is not considered an adjacent cell.

        :param cell: The current cell one wishes to find all neighbouring cells for.
        :return: A list of all adjacent cells to the current/parameter cell.
        """

        neighbours: List[Cell] = list()
        x = cell.x
        y = cell.y

        if super()._check_left(x, y):
            neighbours.append(self._grid[x - Constants.CELL_SIZE, y])
        if super()._check_right(x, y):
            neighbours.append(self._grid[x + Constants.CELL_SIZE, y])
        if super()._check_up(x, y):
            neighbours.append(self._grid[x, y - Constants.CELL_SIZE])
        if super()._check_down(x, y):
            neighbours.append(self._grid[x, y + Constants.CELL_SIZE])

        return neighbours
    # find_neighbouring_cells()

    def __update_cell(self, adjacent_cell: Cell, current_cell: Cell):
        adjacent_cell.cost_from_start = current_cell.cost_from_start + self.__movement_cost
        adjacent_cell.cost_to_end = self.__calculate_heuristic_cost(adjacent_cell)
        adjacent_cell.parent = current_cell

    def __calculate_heuristic_cost(self, cell: Cell):
        """
        Calculates a heuristic cost for moving from the given cell to the exit.
        This is not an optimal way of calculating the estimated movement cost through the maze (hence the function name)
        as the result will be differ from the actual cost if the randomly generated maze is very complex (lots of twists
        and turns rather than a straight path to the exit).

        :param cell: The cell one wishes to calculate the cost of moving from to the exit.
        :return: Movement cost of moving from given cell to the exit.
        """

        return self.__movement_cost * (abs(cell.x - Constants.ROOT_X) + abs(cell.y - Constants.ROOT_Y))
