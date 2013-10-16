#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" finder_colors.py - Setting colours of files/folders from the commandline.

Copyright (c) 2013 Daniel Fairhead <danthedeckie on github>
--------
Contributors:
 - Panayotis Vryonis <vrypan on github>

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

------------------

Usage:

$finder_colors.py <filename>

outputs which colour it's been set to.

$finder_colors.py <color> <filename>

sets the color.

------------------

You can also include this as a python module, and use the two functions:

set(filename, color)

and

get(filename)

which work pretty much as you'd expect.

"""

from __future__ import print_function
from xattr import xattr
from sys import argv, stderr

__version__ = '0.9.3'

_FINDER_INFO_TAG = u'com.apple.FinderInfo'

COLORS = {'none': 0, 'gray': 2, 'green': 4, 'purple': 6, 
          'blue': 8, 'yellow': 10, 'red': 12, 'orange': 14}
NAMES  = {0: 'none', 2: 'gray', 4: 'green', 6: 'purple', 
          8: 'blue', 10 : 'yellow', 12 : 'red', 14 : 'orange' }

BLANK = 32*chr(0)

def get(filename):
    ''' Get OSX Finder Color (extended attribute) of path (file or folder) '''

    try:
        attrs = xattr(filename)
        color_num = ord(attrs.get(_FINDER_INFO_TAG)[9]) & 14 
        # & 14 to mask with "1110" (ie ignore all other bits).
        return NAMES[color_num]

    except IOError as err:
        if err.errno == 93: # attribute not found...
            return NAMES[0]
        # else
        raise err
    except KeyError as err:
        return NAMES[0]

def set(filename, color): # pylint: disable=W0622
    ''' Set OSX Finder Color (extended attribute) of path (file or folder) '''

    attrs = xattr(filename)
    if _FINDER_INFO_TAG in attrs:
        previous = attrs[_FINDER_INFO_TAG]
    else:
        previous = BLANK

    prev_color_extra_bits = ord(previous[9]) & (255-14)

    # these are all the bits in previous[9] not used for color.
    new = previous[:9] \
        + chr(COLORS[color] \
        + prev_color_extra_bits) \
        + previous[10:]

    attrs.set(_FINDER_INFO_TAG, new)
    return new


###############################################################################
# If this is used as a stand-alone script:

if __name__ == '__main__':

    def display(pathname):
        ''' display filename\tcolor '''
        print(pathname, get(pathname), sep='\t')

    def usage(): # pylint: disable=C0111
        print ('Usage:\n\n'
               '{0} <filename(s)>\n\n'
               'to find out what colour a file is.\n'
               'Output format is <filename><TAB><color><NEWLINE>\n\n'
               'or\n\n'
               '{0} [color] <filename(s)>\n\n'
               'to set the color of those file(s).\n\n'
               'Possible colors are:'.format(argv[0]))
        print (*COLORS, sep=', ') # pylint: disable=W0142


    try:

        if len(argv) == 1: # No arguments, so display a usage message.
            usage()
        elif len(argv) == 2: # One argument, so presumably a file.
            display(argv[1])

        else: # At least 2 arguments...

            # If there are more args, then the last one *could* be a color,
            # in which case, set all preceding mentioned files to that color.
            # Otherwise, if it's a pathname, then display it and all the
            # other paths and their colors:

            if argv[1] in COLORS:
                for fn in argv[2:]:
                    set(fn, argv[1])

                    display(fn)
            else:
                for f in argv[1:]:
                    display(f)

    except Exception as err: # pylint: disable=W0703
        print(err, file=stderr)

        if hasattr(err,'errno') and err.errno != 0:
            exit(err.errno)
        else:
            exit(1)
