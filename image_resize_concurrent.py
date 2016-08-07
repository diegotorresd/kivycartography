import sys
import os
import shutil
import time
from PIL import Image
import concurrent.futures
from image_resize_functions import *

# compute maximum zoom level
full_filename, tile_size = sys.argv[1:]
basename, extension = os.path.splitext(full_filename)
max_zoom_level = get_max_zoom_level(full_filename, tile_size)
output_dir = basename + "_tiles"
create_dir(output_dir)
executor = concurrent.futures.ProcessPoolExecutor()
i = int(max_zoom_level)
results = {}

for zoom_level in range(6, 4, -1):
    filename_for_zoom_level = "{0}_{1}{2}".format(basename, zoom_level, extension)
    mult = 2 ** (max_zoom_level - zoom_level)
    print("Sending resize operation for level %s to executor..." % zoom_level)
    start = time.perf_counter()
    f = executor.submit(resize_image, full_filename, mult, filename_for_zoom_level)
    # f = executor.submit(im.resize,
    #     (s // (2 ** (max_zoom_level - zoom_level)) for s in original_image.size))
    results[f] = filename_for_zoom_level
for future in concurrent.futures.as_completed(results, timeout=90):
    try:
        image_result_size = future.result()
        print(image_result_size)
    except Exception as exc:
        print('An exception occurred: %s' % exc)
    else:
        end = time.perf_counter()
        print('File %s took %d seconds' % (results[future], (end - start)))

executor.shutdown()
