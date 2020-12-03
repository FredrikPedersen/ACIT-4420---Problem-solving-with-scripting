from values.Constants import *
from maze.Cell import Cell
from typing import Tuple, Dict


class Grid:

    __instance = None

    @staticmethod
    def get_instance():
        if Grid.__instance is None:
            Grid()

        return Grid.__instance

    def __init__(self):
        if Grid.__instance is not None:
            raise Exception("This is a Singleton class, do not try to instantiate it directly. Use get_instance method!")
        else:
            Grid.__instance = self
            self.__grid: Dict[Tuple[int, int], Cell] = self.__generate_grid()

    def __generate_grid(self) -> Dict[Tuple[int, int], Cell]:
        grid: Dict[Tuple[int, int], Cell] = {}
        y: int = ROOT_Y

        for i in range(0, GRID_HEIGHT):
            x: int = ROOT_X
            for j in range(0, GRID_WIDTH):
                grid[x, y] = Cell()
                x += CELL_SIZE

            y += CELL_SIZE
        return grid

    @property
    def grid(self) -> Dict[Tuple[int, int], Cell]:
        return self.__grid
