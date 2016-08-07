import sys
import os
from PIL import Image
import math
import shutil
import time
from image_resize_functions import *

# compute maximum zoom level
full_filename, tile_size = sys.argv[1:]
filename, extension = os.path.splitext(full_filename)
max_zoom_level = get_max_zoom_level(full_filename, tile_size)
output_dir = filename + "_tiles"
create_dir(output_dir)

i = int(max_zoom_level)
for zoom_level in range(i, -1, -1):
    filename_for_zoom_level = "{0}_{1}{2}".format(filename, zoom_level, extension)
    dir_name_for_zoom_level = os.path.join(output_dir, str(zoom_level))
    create_dir(dir_name_for_zoom_level)
    # if we are at max zoom level, there is no need to resize
    if zoom_level != i:
        start = time.perf_counter()
        mult = 2 ** (max_zoom_level - zoom_level)
        resized = resize_image(full_filename, mult, filename_for_zoom_level)
        end = time.perf_counter()
        print('Zoom level %d took %d seconds' % (zoom_level, end - start))
