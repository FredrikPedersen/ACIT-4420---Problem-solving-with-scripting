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
    __control_panel_height: int = 300
    __control_panel_width: int = 400

    def __init__(self):
        self.__root_window: Tk = self.__initialize_root_window()
        self.__screen: Union[Surface, SurfaceType] = self.__initialize_pygame()

    def __initialize_root_window(self) -> Tk:
        root_window: Tk = Tk()
        root_window.title("Maze Solver")
        root_window.geometry(f"{self.__control_panel_height}x{self.__control_panel_width}")
        self.__initialize_input_form(root_window)

        return root_window

    def __initialize_pygame(self) -> Union[Surface, SurfaceType]:
        pygame.display.init()
        return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def __initialize_input_form(self, window: Tk):

        title_label = Label(window, text="Control Panel", font=("bold", 20))
        title_label.grid(row=1, column=2, pady=2)

        maze_label = Label(window, text="Maze", font=("bold", 15))
        maze_label.grid(row=3, column=1, pady=2)

        width_label = Label(window, text="Width", font=("bold", 10))
        width_label.grid(row=4, column=1, pady=4)
        scale_width = Scale(window, from_=5, to=30, orient=HORIZONTAL)
        scale_width.grid(row=4, column=2, pady=2)

        height_label = Label(window, text="Height", font=("bold", 10))
        height_label.grid(row=5, column=1, pady=4)
        scale_height = Scale(window, from_=5, to=30, orient=HORIZONTAL)
        scale_height.grid(row=5, column=2, pady=2)

        #sample for how to retrieve values
        print(f"{scale_width.get()} x {scale_height.get()}")

        draw_button = Button(window, text="Draw Maze", command=self.__draw_maze)
        draw_button.grid(row=6, column=2, pady=4)

        solution_label = Label(window, text="Solution", font=("bold", 15))
        solution_label.grid(row=7, column=1, pady=2)

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
