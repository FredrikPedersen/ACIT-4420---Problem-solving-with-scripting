import abc
from abc import ABC
import values.Constants as Constants
from typing import Dict, List, Tuple, Set
from maze.Cell import Cell
from maze.Grid import Grid
from values.Direction import Direction


class SolutionABC(ABC):

    """
    Abstract Base Class for all maze-solution algorithms.
    """

    def __init__(self, solution_start: Tuple[int, int]):
        grid_instance: Grid = Grid.get_instance()

        self._grid: Dict[Tuple[int, int], Cell] = grid_instance.grid
        self._solutionStartX: int = solution_start[0]
        self._solutionStartY: int = solution_start[1]
    # __init__()

    @abc.abstractmethod
    def solve_maze(self) -> List[Tuple[int, int]]:
        pass

    def _check_left(self, x: int, y: int) -> bool:
        return not self._grid[x, y].walls[Direction.LEFT] and x - Constants.CELL_SIZE >= Constants.ROOT_X

    def _check_right(self, x: int, y: int) -> bool:
        return not self._grid[x, y].walls[Direction.RIGHT] and x + Constants.CELL_SIZE <= Constants.MAZE_WIDTH

    def _check_up(self, x: int, y: int) -> bool:
        return not self._grid[x, y].walls[Direction.UP] and y - Constants.CELL_SIZE >= Constants.ROOT_Y

    def _check_down(self, x: int, y: int) -> bool:
        return not self._grid[x, y].walls[Direction.DOWN] and y + Constants.CELL_SIZE <= Constants.MAZE_HEIGHT
