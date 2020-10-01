from imageProcessor import *

image_path = "oslomet.bmp"

imageProcessor = ImageProcessor(image_path, "bmp")

imageProcessor.get_image_size()
imageProcessor.create_snow_image()
imageProcessor.create_yellow_image()