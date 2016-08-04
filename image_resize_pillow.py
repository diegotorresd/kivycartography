import sys
import os
from PIL import Image
import math
import shutil

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

# compute maximum zoom level
full_filename, tile_size = sys.argv[1:]
filename, extension = os.path.splitext(full_filename)
original_image = Image.open(full_filename)
sizex, sizey = original_image.size
max_zoom_level = math.ceil(math.log(max(sizex, sizey) / int(tile_size), 2))
output_dir = filename + "_tiles"
create_dir(output_dir)
original_image.close()

i = int(max_zoom_level)
prev_filename = full_filename
for zoom_level in range(i, -1, -1):
    filename_for_zoom_level = "{0}_{1}{2}".format(filename, zoom_level, extension)
    dir_name_for_zoom_level = os.path.join(output_dir, str(zoom_level))
    create_dir(dir_name_for_zoom_level)
    # if we are at max zoom level, there is no need to resize
    if zoom_level == i:
        shutil.copy(prev_filename, filename_for_zoom_level)
    # otherwise, resize image to half
    if not os.path.exists(filename_for_zoom_level):
        prev_image = Image.open(prev_filename)
        image_for_zoom_level = prev_image.resize(s // 2 for s in prev_image.size)
        image_for_zoom_level.save(filename_for_zoom_level)
        prev_image.close()
        # tile the image 
        image_for_zoom_level.close()
    prev_filename = filename_for_zoom_level
