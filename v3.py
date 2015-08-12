#!/usr/bin/env python
from __future__ import print_function
import glob
import os
import IPython.nbformat
allnotebooks = glob.glob('*.ipynb')
nonv3 = [n for n in allnotebooks if '.v3' not in n]

def newer(thisfile, otherfile):
    return os.path.getmtime(thisfile) > os.path.getmtime(otherfile)

for f in nonv3:
    v3name = f[:-6] + '.v3.ipynb'
    if not os.path.exists(v3name) or newer(f, v3name):
        notebook = IPython.nbformat.read(f, 4)
        IPython.nbformat.write(notebook, v3name, 3)
        print(f)
