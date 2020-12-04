from tkinter import *
from typing import Dict
from typing import Union

import pygame
from pygame.surface import SurfaceType, Surface

from maze.MazeDrawer import MazeDrawer
from solution.MazeSolver import MazeSolver
from values.Constants import *
from values.SolutionType import SolutionType


class Gui:

    __creationSteps: Dict

    def __init__(self):
        self.__root_window: Tk = self.__initialize_root_window()
        self.__screen: Union[Surface, SurfaceType] = self.__initialize_pygame()

    def __initialize_root_window(self) -> Tk:
        root_window: Tk = Tk()
        root_window.title("Maze Solver")
        root_window.geometry("300x400")
        self.__initialize_input_form(root_window)

        return root_window

    def __initialize_pygame(self) -> Union[Surface, SurfaceType]:
        pygame.display.init()
        return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def __initialize_input_form(self, window: Tk):
        maze_dimensions_label = Label(window, text="Control Panel", font=("bold", 20))
        maze_dimensions_label.place(x=60, y=20)

        maze_dimensions_label = Label(window, text="Maze", font=("bold", 15))
        maze_dimensions_label.place(x=10, y=80)

        width_label = Label(window, text="Width", font=("bold", 10))
        width_label.place(x=10, y=135)
        scale_width = Scale(window, from_=5, to=30, orient=HORIZONTAL)
        scale_width.place(x=60, y=115)

        height_label = Label(window, text="Height", font=("bold", 10))
        height_label.place(x=10, y=180)
        scale_height = Scale(window, from_=5, to=30, orient=HORIZONTAL)
        scale_height.place(x=60, y=160)

        draw_button = Button(window, text="Draw Maze", command=self.__draw_maze)
        draw_button.place(x=10, y=220)

    def __draw_maze(self):
        maze_drawer: MazeDrawer = MazeDrawer(self.__screen)
        self.__creationSteps = maze_drawer.draw()

    def __solve_maze(self):

        if self.__creationSteps is None:
            raise Exception("A maze must be drawn before trying to solve!")
        else:
            maze_solver: MazeSolver = MazeSolver(self.__screen, SolutionType.BUILD_SOLUTION, self.__creationSteps)
            maze_solver.solve_maze()

    def run_gui_loop(self):
        while True:
            self.__root_window.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
