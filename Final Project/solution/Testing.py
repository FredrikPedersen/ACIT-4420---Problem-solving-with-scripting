from maze.MazeUtils import *


class Testing:

    __solutionStartX = GRID_WIDTH * CELL_SIZE
    __solutionStartY = GRID_HEIGHT * CELL_SIZE

    def __init__(self, screen: Union[Surface, SurfaceType]):
        self.__screen = screen
    # init()

    # ---------- General Solution Functions ---------- #

    def solve_maze(self):
        self.__mark_start_exit()
        self.__draw_solution()

    def __mark_start_exit(self):
        """
        Convenience function for drawing the solution's start and exit positions as red and green cells, respectively.
        """

        draw_maze_cell(self.__solutionStartX, self.__solutionStartY, self.__screen, None, Colour.RED)
        draw_maze_cell(ROOT_X, ROOT_Y, self.__screen, None, Colour.GREEN)

    # mark_start_exit()

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
    # draw_solution_cell()

    # ---------- Recursive Solution Functions ---------- #

    def __draw_solution(self) -> None:
        print("ASF")
