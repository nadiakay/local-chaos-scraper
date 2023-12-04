"""
usage: python3 ren-localchaos.py <path> ...

renames image files to sort alphabetically. for archiving localchaos.org
"""

import os
import sys
from os import scandir

dirs = [f.path for f in os.scandir('.') if f.is_dir()]
dirs = sorted(dirs)
dirs = sys.argv[1:]
print('dirs',dirs)
paths = ['/home/nadia/Downloads/' + dir for dir in dirs]
print(paths)

for dir in dirs:
	print('dir',dir)
	for file in scandir(dir):
		fn = file.path.split('/')[-1]
		if fn == "frontcover.jpg":
			os.rename(file.path, dir + "/0.jpg")
		if fn == "backcover.jpg":
			os.rename(file.path, dir + "/zback.jpg")
		if fn[:4] == "page":
			fn = fn[4:]
			if len(fn) == 5 or len(fn) == 7 or len(fn) == 8:
			#cases: pageX.jpg ; pageX-X.jpg ; page9-10.jpg
				fn = '0' + fn
			os.rename(file.path, dir + '/' + fn)
