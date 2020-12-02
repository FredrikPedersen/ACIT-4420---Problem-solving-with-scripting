from typing import List
from values.Direction import Direction


class Cell:

    def __init__(self):
        self.__walls: List[bool, bool, bool, bool] = [True, True, True, True]

    def toggle_wall(self, direction: Direction):
        if direction == Direction.LEFT:
            self.__walls[0] = not self.__walls[0]
        if direction == Direction.RIGHT:
            self.__walls[1] = not self.__walls[1]
        if direction == Direction.UP:
            self.__walls[2] = not self.__walls[2]
        if direction == Direction.DOWN:
            self.__walls[3] = not self.__walls[3]

    @property
    def walls(self):
        return self.__walls

    def __str__(self) -> str:
        return str(self.__walls)
