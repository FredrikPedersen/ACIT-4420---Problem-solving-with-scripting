from Constants import *
from typing import Tuple, List


def generate_grid() -> List[Tuple[int, int]]:
    grid: List[Tuple[int, int]] = []
    y: int = 0

    for i in range(0, GRID_HEIGHT):
        x: int = CELL_SIZE
        y += CELL_SIZE
        for j in range(0, GRID_WIDTH):

            grid.append((x, y))
            x += CELL_SIZE

    return grid

