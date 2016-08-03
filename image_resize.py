import sys
import subprocess
import math

# compute maximum zoom level
full_filename, tile_size = sys.argv[1:]
filename, extension = os.path.splitext(full_filename)
file_size = subprocess.check_output('identify -format "%wx%h" ' + filename)
sizex, sizey = map(int, file_size.split('x'))
max_zoom_level = math.ceil(math.log(max(sizex, sizey) / int(tile_size), 2))
output_dir = filename + "_tiles"
os.mkdir(output_dir)

i = int(max_zoom_level)
subprocess.call("copy {0} {1}".format(full_filename, filename + "_" + max_zoom_level ))
while i >= 0:
    os.mkdir(output_dir + "/" + i)
    i = i - 1
