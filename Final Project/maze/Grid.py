from values.Constants import *
from maze.Cell import Cell
from typing import Tuple, Dict


def generate_grid() -> Dict[Tuple[int, int], Cell]:
    grid: Dict[Tuple[int, int], Cell] = {}
    y: int = 0

    for i in range(0, GRID_HEIGHT):
        x: int = CELL_SIZE
        y += CELL_SIZE
        for j in range(0, GRID_WIDTH):
            grid[x, y] = Cell()
            x += CELL_SIZE
    return grid

