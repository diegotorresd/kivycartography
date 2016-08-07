from PIL import Image
import math
import os
import shutil

def get_max_zoom_level(image_filename, tile_size):
    with Image.open(image_filename) as original_image:
        sizex, sizey = original_image.size
        return math.ceil(math.log(min(sizex, sizey) / int(tile_size), 2))

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def resize_image(image_filename, multiplier, filename_for_zoom_level):
    basename, extension = os.path.splitext(image_filename)
    if not os.path.exists(filename_for_zoom_level):
        shutil.copy(image_filename, filename_for_zoom_level)
    print("Resizing image for multiplier %d" % multiplier)
    with Image.open(filename_for_zoom_level) as image_for_zoom_level:
        print("Image opened")
        resized_image = image_for_zoom_level.resize(
            (s // multiplier for s in image_for_zoom_level.size))
        print("Image resized to size {}x{}".format(*resized_image.size))
        resized_image.save(filename_for_zoom_level)
        print("image saved")
        return resized_image.size
