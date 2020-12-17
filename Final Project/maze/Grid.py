import values.Constants as Constants
from maze.Cell import Cell
from typing import Tuple, Dict


class Grid:

    """
    Singleton class representing the grid a maze is drawn upon.
    Is essentially used to hold the Grid-list and make sure not two grids exists at the same time in the program.
    """

    __instance = None

    @staticmethod
    def get_instance():
        if Grid.__instance is None:
            Grid()

        return Grid.__instance
    # get_instance()

    def __init__(self):
        if Grid.__instance is not None:
            raise Exception("This is a Singleton class, do not try to instantiate it directly. Use get_instance method!")
        else:
            Grid.__instance = self
    # __init__()

    def generate_grid(self) -> Dict[Tuple[int, int], Cell]:
        """
        Generates a N x M Dictionary with Cell objects as values, where N and M are defined constants.py (and are
        intended to be set by the user at runtime). Each cell is given an area equal to CELL_SIZExCELL_SIZE in the grid.

        :return: Dictionary with a Cell object's coordinates as key, and the Cell object itself as value.
        """

        grid: Dict[Tuple[int, int], Cell] = {}
        y: int = Constants.ROOT_Y

        for i in range(0, Constants.GRID_HEIGHT):
            x: int = Constants.ROOT_X
            for j in range(0, Constants.GRID_WIDTH):
                grid[x, y] = Cell(x, y)
                x += Constants.CELL_SIZE

            y += Constants.CELL_SIZE

        self.__grid = grid
        return grid
    # generate_grid()

    @property
    def grid(self) -> Dict[Tuple[int, int], Cell]:
        return self.__grid
