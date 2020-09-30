from imageProcessor import *

image_path = "oslomet.bmp"

imageProcessor = ImageProcessor(image_path, "bmp")

imageProcessor.cut_image(200, 200)