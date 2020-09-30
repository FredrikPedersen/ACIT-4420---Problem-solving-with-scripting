from typing import Tuple
from PIL import Image
import numpy


class ImageProcessor:

    def __init__(self, image_path: str, image_format: str):
        self.__image = numpy.array(Image.open(image_path))
        self.__image_format = "." + image_format

    def get_image_size(self, image: numpy.ndarray = None) -> Tuple[int, int]:
        if image is None:
            image = self.__image

        return image.shape[:2]

    def create_snow_image(self):
        image_copy = self.__image.copy()
        return

    def cut_image(self, pixels_cut_top: int, pixels_cut_sides: int):
        index_right = 1200 - pixels_cut_sides

        cut_image = self.__image.copy()[pixels_cut_top:1200, pixels_cut_sides:index_right]
        self.__save_new_image(cut_image, "oslomet_small")

    def __save_new_image(self, image: numpy.ndarray, image_name: str) -> None:
        Image.fromarray(image).save(image_name + self.__image_format)