import sys
import os
from image_resize_functions import *
from vipsCC import *

OUTPUT_FILENAME_FORMAT = 'x%d_y%d.png'

full_filename, tilesizearg = sys.argv[1:]
tile_size = int(tilesizearg)
basename, extension = os.path.splitext(full_filename)
max_zoom_level = int(get_max_zoom_level(full_filename, tile_size))
output_dir = basename + "_tiles"
create_dir(output_dir)

try:
    im = VImage.VImage(full_filename)
    for zoom_level in range(max_zoom_level - 1, -1, -1):
        print("Creating tiles for level %d" % zoom_level)
        dir_name_for_zoom_level = os.path.join(output_dir, str(zoom_level))
        create_dir(dir_name_for_zoom_level)
        for y in range(0, im.Ysize(), tile_size):
            for x in range(0, im.Xsize(), tile_size):
                filename = OUTPUT_FILENAME_FORMAT % (x / tile_size, y / tile_size)
                width = min(im.Xsize() - x, tile_size)
                height = min(im.Ysize() - y, tile_size)
                im.extract_area(x, y, width, height).embed(0, 0, 0, tile_size, tile_size).write(os.path.join(dir_name_for_zoom_level,filename))
        # if im.XSize() <= tile_size and im.YSize() <= tile_size:
        #     break
        shrink = im.rightshift_size(1, 1, im.BandFmt())
        im = shrink.write(VImage.VImage ("temp", "t"))

except VError.VError as e:
    e.perror(sys.argv[0])
