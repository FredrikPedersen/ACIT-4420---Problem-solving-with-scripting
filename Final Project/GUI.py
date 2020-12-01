import pygame
import time
import random
from typing import Tuple, List, Dict
from Grid import generate_grid
from Constants import *
from Direction import *

# Initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")


# Maze variables
rootX: int = 20
rootY: int = 20
solutionStart: int = GRID_WIDTH * GRID_HEIGHT
grid: List[Tuple[int, int]] = generate_grid()
solution: Dict = {}


def draw_grid() -> None:
    """
    Draws white lines around each cell in the grid.
    """

    for coordinates in grid:
        x: int = coordinates[0]
        y: int = coordinates[1]

        pygame.draw.line(screen, WHITE, [x, y], [x + CELL_DIMENSION, y])
        pygame.draw.line(screen, WHITE, [x + CELL_DIMENSION, y + CELL_DIMENSION], [x, y + CELL_DIMENSION])
        pygame.draw.line(screen, WHITE, [x + CELL_DIMENSION, y], [x + CELL_DIMENSION, y + CELL_DIMENSION])
        pygame.draw.line(screen, WHITE, [x, y + CELL_DIMENSION], [x, y])
        pygame.display.update()


def draw_maze_cell(x, y, direction=None) -> None:
    """
    Fills out a cell on the grid with a coloured rectangle to indicate part of the maze at coordinates (x, y).
    If a direction is given, the cell in the given direction is also filled out in addition to the cell at (x, y).

    :param x: X-coordinate of current cell
    :param y: Y-coordinate of current cell
    :param direction: Which cell shall be drawn in addition to the current one.
    """

    # Offsets to make sure the maze's tile colour does not fill over the wall colour.
    rectangle_size: int = CELL_DIMENSION - 1
    x += 1
    y += 1

    if direction is None:
        pygame.draw.rect(screen, BLUE, (x, y, rectangle_size, rectangle_size), 0)

    if direction == Direction.LEFT:
        pygame.draw.rect(screen, BLUE, (x - CELL_DIMENSION, y, rectangle_size*2, rectangle_size), 0)

    if direction == Direction.RIGHT:
        pygame.draw.rect(screen, BLUE, (x, y, rectangle_size*2, rectangle_size), 0)

    if direction == Direction.DOWN:
        pygame.draw.rect(screen, BLUE, (x, y, rectangle_size, rectangle_size*2), 0)

    if direction == Direction.UP:
        pygame.draw.rect(screen, BLUE, (x, y - CELL_DIMENSION, rectangle_size, rectangle_size*2), 0)

    pygame.display.update()


def draw_backtracking_cell(x, y):
    rectangle_size: int = CELL_DIMENSION - 1

    pygame.draw.rect(screen, RED, (x + 1, y + 1, rectangle_size, rectangle_size), 0)
    pygame.display.update()


def draw_solution_cell(x, y):
    # Offset to place the circle in the center of the cell
    x += CELL_DIMENSION/2
    y += CELL_DIMENSION/2

    pygame.draw.circle(screen, YELLOW, (x, y), 3)
    pygame.display.update()


def draw_maze(x, y):
    """
    Recursive randomized depth-first search to create a maze on an nxn grid of cells.
    For each step of the algorithm:
        1. Mark the current cell as visited
        2. While the current cell has any unvisited neighbour cells:
             - Choose on of the unvisited neighbours.
             - Remove the wall between the current cell and the chosen neighbouring cell.
             - Invoke the routine for the chosen neighbouring cell.

    :param x: X-coordinate of starting point
    :param y: Y-coordinate of starting point
    """

    # Mark the starting location as visited, add it to the stack and draw it.
    visited: List[Tuple[int, int]] = [(x, y)]
    stack: List[Tuple[int, int]] = [(x, y)]
    draw_backtracking_cell(x, y)

    while len(stack) > 0:
        time.sleep(.05)
        neighbouring_cells: List[Direction] = []

        # Check if right, left, bottom and top cells are already visited and exists, respectively.
        if (x + CELL_DIMENSION, y) not in visited and (x + CELL_DIMENSION, y) in grid:
            neighbouring_cells.append(Direction.RIGHT)

        if (x - CELL_DIMENSION, y) not in visited and (x - CELL_DIMENSION, y) in grid:
            neighbouring_cells.append(Direction.LEFT)

        if (x, y + CELL_DIMENSION) not in visited and (x, y + CELL_DIMENSION) in grid:
            neighbouring_cells.append(Direction.DOWN)

        if (x, y - CELL_DIMENSION) not in visited and (x, y - CELL_DIMENSION) in grid:
            neighbouring_cells.append(Direction.UP)

        if len(neighbouring_cells) > 0:

            # Select a neighbour at random
            chosen_neighbour: Direction = (random.choice(neighbouring_cells))

            if chosen_neighbour == Direction.RIGHT:
                draw_maze_cell(x, y, Direction.RIGHT)
                solution[(x + CELL_DIMENSION, y)] = x, y     # solution = dictionary key = new cell, other = current cell
                x = x + CELL_DIMENSION                       # Mark this cell as the current cell
                visited.append((x, y))
                stack.append((x, y))

            elif chosen_neighbour == Direction.LEFT:
                draw_maze_cell(x, y, Direction.LEFT)
                solution[(x - CELL_DIMENSION, y)] = x, y
                x = x - CELL_DIMENSION
                visited.append((x, y))
                stack.append((x, y))

            elif chosen_neighbour == Direction.DOWN:
                draw_maze_cell(x, y, Direction.DOWN)
                solution[(x, y + CELL_DIMENSION)] = x, y
                y = y + CELL_DIMENSION
                visited.append((x, y))
                stack.append((x, y))

            elif chosen_neighbour == Direction.UP:
                draw_maze_cell(x, y, Direction.UP)
                solution[(x, y - CELL_DIMENSION)] = x, y
                y = y - CELL_DIMENSION
                visited.append((x, y))
                stack.append((x, y))

        else:
            # If all neighbouring cells are visited, remove the current one from the stack
            x, y = stack.pop()
            draw_backtracking_cell(x, y)
            time.sleep(.05)

            # Change colour back after the backtracking has been displayed
            draw_maze_cell(x, y)


def draw_solution(solution_start) -> None:
    x: int = solution_start
    y: int = solution_start

    # Solution list contains all the coordinates to route back to start
    draw_solution_cell(x, y)

    # Loop until cell position == Start position
    while (x, y) != (rootX, rootY):

        # "key value" now becomes the new key
        x, y = solution[x, y]
        draw_solution_cell(x, y)
        time.sleep(.1)


draw_grid()
draw_maze(rootX, rootY)
draw_solution(solutionStart)

running: bool = True
# Pygame Loop
while running:

    for event in pygame.event.get():

        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
