"""
usage: python3 to-pdf.py <dir-name> <pdf-name>

Saves alphabeticalized list of images from '<dir-name>_files' directory to <pdf-name>.pdf. if <pdf-name> is not given, <dir-name> is used
"""

import sys
from os import listdir
from os.path import isfile, join
from PIL import Image

fn = sys.argv[1]
dir = "./" + fn
print(listdir("./" + fn))
files = [f for f in listdir(dir) if isfile(join(dir, f))]
files.sort()
images = [Image.open(dir + "/" + f) for f in files]
try:
	fn = sys.argv[2]
	print('renaming:', fn)
except IndexError:
	print('naming as original folder...')
images[0].save(fn + ".pdf", save_all=True, append_images=images[1:])
