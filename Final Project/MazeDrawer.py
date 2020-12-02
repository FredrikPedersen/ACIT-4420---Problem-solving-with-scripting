import random
import time
from typing import Dict, List, Set
from Grid import generate_grid
from MazeUtils import *
from Cell import Cell


class MazeDrawer:
    __creationSteps: Dict = {}

    def __init__(self, screen: Union[Surface, SurfaceType]):
        self.__screen = screen
        self.__grid: Dict[Tuple[int, int], Cell] = generate_grid()
    # init()

    def draw(self) -> None:
        """
        Public facing convenience function for performing all drawing tasks of this class
        """
        self.__draw_grid()
        self.__draw_maze()
    # draw()

    # ---------- Grid Functions ---------- #

    def __draw_grid(self) -> None:
        """
        Draws white lines around each cell in the grid.
        """

        for coordinates in self.__grid:
            x: int = coordinates[0]
            y: int = coordinates[1]

            pygame.draw.line(self.__screen, Colour.BLACK.value, [x, y], [x + CELL_SIZE, y])
            pygame.draw.line(self.__screen, Colour.BLACK.value, [x + CELL_SIZE, y + CELL_SIZE], [x, y + CELL_SIZE])
            pygame.draw.line(self.__screen, Colour.BLACK.value, [x + CELL_SIZE, y], [x + CELL_SIZE, y + CELL_SIZE])
            pygame.draw.line(self.__screen, Colour.BLACK.value, [x, y + CELL_SIZE], [x, y])
            pygame.display.update()
    # draw_grid()

    # ---------- Maze Functions ---------- #

    def __draw_backtracking_cell(self, x, y) -> None:
        """
        Draws a red square at position (x, y), then changes the colour back to default after .05 seconds.
        This creates a blinking red cell, used for displaying how the maze-algorithm backtracks through the stack.

        :param x: x-coordinate to draw red cell at
        :param y: y-coordinate to draw red cell at
        """

        # Offsets to make sure the maze's tile colour does not fill over the wall colour.
        rectangle_size: int = CELL_SIZE - 1

        pygame.draw.rect(self.__screen, Colour.RED.value, (x + 1, y + 1, rectangle_size, rectangle_size), 0)
        pygame.display.update()

        if ANIMATIONS_ENABLED:
            time.sleep(.05)

        # Change colour back after the backtracking has been displayed
        draw_maze_cell(x, y, self.__screen)
        pygame.display.update()
    # draw_backtracking_cell()

    def __find_unvisited_neighbours(self, x: int, y: int, visited: Set[Tuple[int, int]]) -> List[Direction]:
        """
        Finds all the existing unvisited neighbour for the current cell (x, y).

        :param x: x-coordinate of current cell.
        :param y: y-coordinate of current cell.
        :param visited: List of all visited cells in the current maze.
        :return: List of the direction of all unvisited neighbours of the current cell (x, y).
        """

        neighbouring_cells: List[Direction] = []

        # Check if right, left, bottom and top cells are already visited and exists, respectively.
        if (x + CELL_SIZE, y) not in visited and (x + CELL_SIZE, y) in self.__grid:
            neighbouring_cells.append(Direction.RIGHT)

        if (x - CELL_SIZE, y) not in visited and (x - CELL_SIZE, y) in self.__grid:
            neighbouring_cells.append(Direction.LEFT)

        if (x, y + CELL_SIZE) not in visited and (x, y + CELL_SIZE) in self.__grid:
            neighbouring_cells.append(Direction.DOWN)

        if (x, y - CELL_SIZE) not in visited and (x, y - CELL_SIZE) in self.__grid:
            neighbouring_cells.append(Direction.UP)

        return neighbouring_cells
    # find_unvisited_neighbours()

    def __draw_maze(self):
        """
        Recursive randomized depth-first search to create a maze on a grid of cells.
        For each step of the algorithm:
            1. Mark the current cell as visited
            2. While the current cell has any unvisited neighbour cells:
                 - Choose one of the unvisited neighbours.
                 - Remove the wall between the current cell and the chosen neighbouring cell.
                 - Invoke the routine for the chosen neighbouring cell.

        Also keeps track of it's creation steps for create a recursive solution for the maze by keeping track of the
        current cell and what was the previous step in a key-value pair, with key being the previous cell, and value
        being the current cell.

        In each case were a neighbour is to be traversed, the neighbouring cell and the current cell has their
        walls (used for solution algorithms) updated accordingly.
        """

        x = ROOT_X
        y = ROOT_Y

        # Mark the starting location as visited, add it to the stack and draw it.
        visited: Set[Tuple[int, int]] = {(x, y)}
        stack: List[Tuple[int, int]] = [(x, y)]

        while len(stack) > 0:

            if ANIMATIONS_ENABLED:
                time.sleep(.05)

            neighbouring_cells: List[Direction] = self.__find_unvisited_neighbours(x, y, visited)

            if len(neighbouring_cells) > 0:

                # Select a neighbour at random
                chosen_neighbour: Direction = (random.choice(neighbouring_cells))

                if chosen_neighbour == Direction.RIGHT:
                    self.__grid[(x, y)].toggle_wall(Direction.RIGHT)
                    self.__grid[x + CELL_SIZE, y].toggle_wall(Direction.LEFT)

                    draw_maze_cell(x, y, self.__screen, Direction.RIGHT)
                    self.__creationSteps[(x + CELL_SIZE, y)] = x, y

                    x = x + CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

                elif chosen_neighbour == Direction.LEFT:
                    self.__grid[(x, y)].toggle_wall(Direction.LEFT)
                    self.__grid[x - CELL_SIZE, y].toggle_wall(Direction.RIGHT)

                    draw_maze_cell(x, y, self.__screen, Direction.LEFT)
                    self.__creationSteps[(x - CELL_SIZE, y)] = x, y

                    x = x - CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

                elif chosen_neighbour == Direction.DOWN:
                    self.__grid[(x, y)].toggle_wall(Direction.DOWN)
                    self.__grid[x, y + CELL_SIZE].toggle_wall(Direction.UP)

                    draw_maze_cell(x, y, self.__screen, Direction.DOWN)
                    self.__creationSteps[(x, y + CELL_SIZE)] = x, y

                    y = y + CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

                elif chosen_neighbour == Direction.UP:
                    self.__grid[(x, y)].toggle_wall(Direction.UP)
                    self.__grid[x, y - CELL_SIZE].toggle_wall(Direction.DOWN)

                    draw_maze_cell(x, y, self.__screen, Direction.UP)
                    self.__creationSteps[(x, y - CELL_SIZE)] = x, y

                    y = y - CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

            else:

                # If all neighbouring cells are visited, remove the current one from the stack
                x, y = stack.pop()
                self.__draw_backtracking_cell(x, y)

    # draw_maze()

    # ---------- Getters and Setters ---------- #

    @property
    def creation_steps(self):
        return self.__creationSteps


