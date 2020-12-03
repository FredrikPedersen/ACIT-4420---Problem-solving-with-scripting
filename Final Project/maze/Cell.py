from typing import Dict
from values.Direction import Direction


class Cell:

    def __init__(self):
        self.__walls: Dict[Direction: bool] = {Direction.LEFT: True, Direction.RIGHT: True, Direction.UP: True, Direction.DOWN: True}
        self.__visited_while_solving: bool = False

    def toggle_wall(self, direction: Direction):
        self.__walls[direction] = not self.__walls[direction]

    @property
    def walls(self):
        return self.__walls

    @property
    def visited_while_solving(self):
        return self.__visited_while_solving

    @visited_while_solving.setter
    def visited_while_solving(self, visited: bool):
        self.__visited_while_solving = visited

    def __str__(self) -> str:
        return "Walls: " + str(self.__walls) + ", Visisted: " + str(self.__visited_while_solving)
