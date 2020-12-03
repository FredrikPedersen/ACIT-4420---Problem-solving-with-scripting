from typing import Union, Dict

import pygame
import sys
from pygame.surface import SurfaceType, Surface

from maze.MazeDrawer import MazeDrawer
from solution.MazeSolver import MazeSolver
from values.Constants import *
from values.SolutionType import SolutionType
from values.Colour import Colour


class GameLoop:

    __instance = None

    @staticmethod
    def get_instance():
        if GameLoop.__instance is None:
            GameLoop()

        return GameLoop.__instance

    def __init__(self):
        if GameLoop.__instance is not None:
            raise Exception("This is a Singleton class, do not try to instantiate it directly. Use get_instance method!")
        else:
            GameLoop.__instance = self
            pygame.init()
            pygame.mixer.init()
            pygame.display.set_caption("Maze Solver")

            self.__screen: Union[Surface, SurfaceType] = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            self.__base_font = pygame.font.Font(None, 32)
            self.__clock = pygame.time.Clock()


    def start_loop(self):
        # Pygame Loop
        input_rect = pygame.Rect(0, 0, 140, 32)
        colour_active = pygame.Color(Colour.WHITE.value)
        colour_passive = pygame.Color("gray15")
        colour = colour_passive
        active = False
        user_text = ""

        while True:

            for event in pygame.event.get():

                # check for closing the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
                    if active is True:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
                if active:
                    colour = colour_active
                else:
                    colour = colour_passive

                text_surface = self.__base_font.render(user_text, True, Colour.BLACK.value)
                input_rect.w = max(100, text_surface.get_width() + 10)
                pygame.draw.rect(self.__screen, colour, input_rect)

                self.__screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

                pygame.display.flip()

                self.__clock.tick(60)

    def get_screen(self):
        return self.__screen

    def get_font(self):
        return self.__base_font

    def get_clock(self):
        return self.__clock
