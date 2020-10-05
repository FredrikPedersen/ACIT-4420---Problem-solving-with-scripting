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

    def create_snow_image(self) -> None:
        snow_image = self.__image.copy()

        snow_image[snow_image > 150] = 255  # Replaces all values in the array which are greater than 150 with 255

        self.__save_new_image(snow_image, "oslomet_snow")

    def create_yellow_image(self) -> None:
        yellow_image = self.__image.copy()

        for row in range(len(yellow_image)):
            for column in range(len(yellow_image[row])):

                # Checking for red and green values > 130 and blue values < 110
                if yellow_image[row, column][0] > 130 and yellow_image[row, column][1] > 130 and yellow_image[row, column][2] < 110:
                    yellow_image[row, column][0] -= 50

                    # Before increasing the green value, make sure it wont surpass the max value of 255.
                    if yellow_image[row, column][1] > 205:
                        yellow_image[row, column][1] = 255
                    else:
                        yellow_image[row, column][1] += 50

        self.__save_new_image(yellow_image, "oslomet_yellow")

    def cut_image(self, pixels_cut_top: int, pixels_cut_sides: int) -> None:
        index_right = 1200 - pixels_cut_sides

        cut_image = self.__image.copy()[pixels_cut_top:1200, pixels_cut_sides:index_right]
        self.__save_new_image(cut_image, "oslomet_small")

    def __save_new_image(self, image: numpy.ndarray, image_name: str) -> None:
        Image.fromarray(image).save(image_name + self.__image_format)
