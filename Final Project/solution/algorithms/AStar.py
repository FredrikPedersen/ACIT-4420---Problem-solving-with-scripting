from typing import List, Tuple, Set

import values.Constants as Constants
from maze.Cell import Cell
from solution.algorithms.SolutionABC import SolutionABC


class AStar(SolutionABC):

    __movement_cost: int = 10

    def __init__(self, solution_start: Tuple[int, int]):
        super().__init__(solution_start)

    def solve_maze(self) -> List[Tuple[int, int]]:
        closed_cells: Set[Cell] = set()
        open_cells: List[Cell] = list()

        starting_cell = self._grid[self._solutionStartX, self._solutionStartY]
        open_cells.append(starting_cell)

        while len(open_cells):

            cell = open_cells.pop()
            closed_cells.add(cell)

            if cell is self._grid[Constants.ROOT_X, Constants.ROOT_Y]:
                return self.__create_path()

            adjacent_cells: List[Cell] = self.__find_neighbouring_cells(cell)

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

    def __calculate_heuristic_cost(self, cell: Cell):
        return self.__movement_cost * (abs(cell.x - Constants.ROOT_X) + abs(cell.y - Constants.ROOT_Y))

    def __find_neighbouring_cells(self, cell: Cell) -> List[Cell]:
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
