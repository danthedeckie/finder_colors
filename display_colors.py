#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
  display_colors.py [options] <file>...
  display_colors.py -h, --help
  display_colors.py --version

Options:
-c, --color=<color>     Set color. Valid values are: none, gray, green, 
                        purple, blue, yellow, red, orange.

Set colours of files/folders from the commandline.
Without "-c" or "--color", the script prints the color of each file.
If -c is set, the script sets the color of each file to <color>
"""

"""
Copyright (c) 2012 Daniel Fairhead <danthedeckie on github>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
from docopt import docopt
from xattr import xattr
from sys import argv, stderr
from os.path import exists

__version__ = 1.0

FinderInfo = u'com.apple.FinderInfo'

colors = {'none': 0, 'gray': 2, 'green': 4, 'purple': 6, 
          'blue': 8, 'yellow': 10, 'red': 12, 'orange': 14}
names  = {0: 'none', 2: 'gray', 4: 'green', 6: 'purple', 
          8: 'blue', 10 : 'yellow', 12 : 'red', 14 : 'orange' }

blank = 32*chr(0)

def get(filename):
    try:
        attrs = xattr(filename)
        color_num = ord(attrs.get(FinderInfo)[9]) & 14 
        # & 14 to mask with "1110" (ie ignore all other bits).
        return names[color_num]
    except Exception:
        return names[0]

def set(filename, color):
    attrs = xattr(filename)
    if FinderInfo in attrs:
        previous = attrs[FinderInfo]
    else:
        previous = blank
    prev_color_extra_bits = ord(previous[9]) & (255-14)
    # these are all the bits in previous[9] not used for color.
    new = previous[:9] + chr(colors[color] + prev_color_extra_bits) + previous[10:]
    attrs.set(FinderInfo, new)
    return new

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    color = args['--color']

    if color:
        if color not in colors:
            print __doc__
        else:
            for filename in args['<file>']:
                set(filename, color)
    else:
        if len(args['<file>']) == 1:
            print get(args['<file>'][0])
        else:
            for filename in args['<file>']:
                    print '\t'.join([filename,get(filename)])