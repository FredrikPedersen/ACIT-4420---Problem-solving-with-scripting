import pygame
import time
import random
from typing import Tuple, List, Dict, Union, Set
from pygame.surface import SurfaceType, Surface
from Grid import generate_grid
from Constants import *
from Direction import Direction
from Colour import Colour


class MazeDrawer:

    __rootX: int = 20
    __rootY: int = 20
    __solutionStartX: int = GRID_WIDTH * CELL_SIZE
    __solutionStartY: int = GRID_HEIGHT * CELL_SIZE
    __grid: List[Tuple[int, int]] = generate_grid()
    __recursiveSolution: Dict = {}

    def __init__(self, screen: Union[Surface, SurfaceType]):
        self.__screen = screen

    def draw(self) -> None:
        """
        Public facing convenience function for performing all drawing tasks of this class
        """
        self.__draw_grid()
        self.__draw_maze()
        self.__draw_recursive_solution()

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

    def __draw_maze_cell(self, x, y, direction: Direction = None, colour: Colour = None) -> None:
        """
        Fills out a cell on the grid with a coloured rectangle to indicate part of the maze at coordinates (x, y).
        If a direction is given, the cell in the given direction is also filled out in addition to the cell at (x, y).

        :param x: X-coordinate of current cell
        :param y: Y-coordinate of current cell
        :param direction: Which cell shall be drawn in addition to the current one.
        """

        # Offsets to make sure the maze's tile colour does not fill over the wall colour.
        rectangle_size: int = CELL_SIZE - 1
        x += 1
        y += 1

        if colour is None:
            colour_value = Colour.WHITE.value
        else:
            colour_value = colour.value

        if direction is None:
            pygame.draw.rect(self.__screen, colour_value, (x, y, rectangle_size, rectangle_size), 0)

        if direction == Direction.LEFT:
            pygame.draw.rect(self.__screen, colour_value, (x - CELL_SIZE, y, rectangle_size * 2, rectangle_size), 0)

        if direction == Direction.RIGHT:
            pygame.draw.rect(self.__screen, colour_value, (x, y, rectangle_size * 2, rectangle_size), 0)

        if direction == Direction.DOWN:
            pygame.draw.rect(self.__screen, colour_value, (x, y, rectangle_size, rectangle_size * 2), 0)

        if direction == Direction.UP:
            pygame.draw.rect(self.__screen, colour_value, (x, y - CELL_SIZE, rectangle_size, rectangle_size * 2), 0)

        pygame.display.update()

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

        time.sleep(.05)

        # Change colour back after the backtracking has been displayed
        self.__draw_maze_cell(x, y)
        pygame.display.update()

    def __draw_solution_cell(self, x, y) -> None:
        """
        Draws a red circle in the center of the cell at position (x, y).
        Used to draw individual steps in the solution path.

        :param x: x-coordinate to draw circle on
        :param y: x-coordinate to draw circle on
        """

        # Add an offset to place the circle in the center of the cell
        x += CELL_SIZE / 2
        y += CELL_SIZE / 2
        pygame.draw.circle(self.__screen, Colour.RED.value, (x, y), 3)
        pygame.display.update()

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

    def __draw_maze(self):
        """
        Recursive randomized depth-first search to create a maze on a grid of cells.
        For each step of the algorithm:
            1. Mark the current cell as visited
            2. While the current cell has any unvisited neighbour cells:
                 - Choose one of the unvisited neighbours.
                 - Remove the wall between the current cell and the chosen neighbouring cell.
                 - Invoke the routine for the chosen neighbouring cell.

        Also creates a recursive solution for the maze by keeping track of the current cell and what was the previous
        step in a key-value pair, with key being the previous cell, and value being the current cell.
        """

        x = self.__rootX
        y = self.__rootY

        # Mark the starting location as visited, add it to the stack and draw it.
        visited: Set[Tuple[int, int]] = {(x, y)}
        stack: List[Tuple[int, int]] = [(x, y)]

        while len(stack) > 0:
            time.sleep(.05)
            neighbouring_cells: List[Direction] = self.__find_unvisited_neighbours(x, y, visited)

            if len(neighbouring_cells) > 0:

                # Select a neighbour at random
                chosen_neighbour: Direction = (random.choice(neighbouring_cells))

                if chosen_neighbour == Direction.RIGHT:
                    self.__draw_maze_cell(x, y, Direction.RIGHT)
                    self.__recursiveSolution[(x + CELL_SIZE, y)] = x, y
                    x = x + CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

                elif chosen_neighbour == Direction.LEFT:
                    self.__draw_maze_cell(x, y, Direction.LEFT)
                    self.__recursiveSolution[(x - CELL_SIZE, y)] = x, y
                    x = x - CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

                elif chosen_neighbour == Direction.DOWN:
                    self.__draw_maze_cell(x, y, Direction.DOWN)
                    self.__recursiveSolution[(x, y + CELL_SIZE)] = x, y
                    y = y + CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

                elif chosen_neighbour == Direction.UP:
                    self.__draw_maze_cell(x, y, Direction.UP)
                    self.__recursiveSolution[(x, y - CELL_SIZE)] = x, y
                    y = y - CELL_SIZE
                    visited.add((x, y))
                    stack.append((x, y))

            else:

                # If all neighbouring cells are visited, remove the current one from the stack
                x, y = stack.pop()
                self.__draw_backtracking_cell(x, y)

        self.__mark_start_exit()

    def __mark_start_exit(self):
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        self.__draw_maze_cell(self.__solutionStartX, self.__solutionStartY, None, Colour.RED)
        self.__draw_maze_cell(self.__rootX, self.__rootY, None, Colour.GREEN)

    def __draw_recursive_solution(self) -> None:
        """
        Draws the recursive solution for the maze by following the key-value pairs back to the beginning. The key
        corresponding to the current value was the previous step in the path. Updates (x, y) to equal the previous
        cell, and continues retracing the steps until it reaches the maze's start.
        :return:
        """

        x: int = self.__solutionStartX
        y: int = self.__solutionStartY

        # Loop until cell position == Start position
        while (x, y) != (self.__rootX, self.__rootY):
            x, y = self.__recursiveSolution[x, y]
            self.__draw_solution_cell(x, y)
            time.sleep(.1)


