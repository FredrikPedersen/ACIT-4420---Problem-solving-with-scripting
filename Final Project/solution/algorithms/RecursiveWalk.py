from typing import List, Tuple

import values.Constants as Constants
from solution.algorithms.SolutionABC import SolutionABC


class RecursiveWalk(SolutionABC):

    def __init__(self, solution_start: Tuple[int, int]):
        super().__init__(solution_start)
        self.__solutionSteps: List[Tuple[int, int]] = list()

    def solve_maze(self) -> List[Tuple[int, int]]:
        self.__recursive_walk()
        self.__solutionSteps.reverse()
        return self.__solutionSteps

    def __recursive_walk(self, x: int = -1, y: int = -1) -> bool:
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
            x = self._solutionStartX
            y = self._solutionStartY

        if (x, y) == (Constants.ROOT_X, Constants.ROOT_Y):
            self.__solutionSteps.append((x, y))
            return True
        elif self._grid[x, y].visited_while_solving:
            return False

        self._grid[x, y].visited_while_solving = True

        if self.__check_left(x, y) or self.__check_right(x, y) or self.__check_up(x, y) or self.__check_down(x, y):
            self.__solutionSteps.append((x, y))
            return True

        return False
    # recursive_solution()

    def __check_left(self, x: int, y: int) -> bool:
        return super()._check_left(x, y) and self.__recursive_walk(x - Constants.CELL_SIZE, y)

    def __check_right(self, x: int, y: int) -> bool:
        return super()._check_right(x, y) and self.__recursive_walk(x + Constants.CELL_SIZE, y)

    def __check_up(self, x: int, y: int) -> bool:
        return super()._check_up(x, y) and self.__recursive_walk(x, y - Constants.CELL_SIZE)

    def __check_down(self, x: int, y: int) -> bool:
        return super()._check_down(x, y) and self.__recursive_walk(x, y + Constants.CELL_SIZE)
