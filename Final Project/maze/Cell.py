from typing import Dict
from values.Direction import Direction


class Cell:

    def __init__(self):
        self.__walls: Dict[Direction: bool] = {Direction.LEFT: True, Direction.RIGHT: True, Direction.UP: True, Direction.DOWN: True}

        # Values used specifically for Recursive Walk Algorithm
        self.__visited_while_solving: bool = False

        # Values used specifically for A* algorithm
        self.__cost_from_start: int = 0
        self.__cost_to_end: int = 0
        self.__movement_sum: int = 0
        self.__parent: Cell = None

    def toggle_wall(self, direction: Direction):
        self.__walls[direction] = not self.__walls[direction]

    def __update_movement_sum(self):
        self.__movement_sum = self.__cost_from_start + self.__cost_to_end

    @property
    def walls(self):
        return self.__walls

    @property
    def visited_while_solving(self) -> bool:
        return self.__visited_while_solving

    @property
    def cost_from_start(self) -> int:
        return self.__cost_from_start

    @property
    def cost_to_end(self) -> int:
        return self.__cost_to_end

    @property
    def movement_sum(self) -> int:
        return self.__movement_sum

    @property
    def parent(self):
        return self.__parent

    @visited_while_solving.setter
    def visited_while_solving(self, visited: bool):
        self.__visited_while_solving = visited

    @cost_from_start.setter
    def cost_from_start(self, value):
        self.__cost_from_start = value
        self.__update_movement_sum()

    @cost_to_end.setter
    def cost_to_end(self, value):
        self.__cost_to_end = value
        self.__update_movement_sum()

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    def __str__(self) -> str:
        return "Walls: " + str(self.__walls) + ", Visisted: " + str(self.__visited_while_solving)
