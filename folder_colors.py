#!/usr/bin/python
""" folder_colors.py - Setting colours of folders from the commandline.

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

------------------

Usage:

>>> folder_colors.py $filename
outputs which colour it's been set to.

>>> folder_colors.py $filename $color
sets the color.

"""
from xattr import xattr
from sys import argv, stderr

FinderInfo = u'com.apple.FinderInfo'

colors = {'none': 0, 'gray': 2, 'green': 4, 'purple': 6, \
          'blue': 8, 'yellow': 10, 'red': 12, 'orange': 14}
names  = {0: 'none', 2: 'gray', 4: 'green', 6: 'purple', \
          8: 'blue', 10 : 'yellow', 12 : 'red', 14 : 'orange' }

blank = 32*chr(0)

def get(filename):
    attrs = xattr(filename)
    if FinderInfo in attrs:
        return names[ord(attrs.get(FinderInfo)[9])]
    else:
        return names[0]

def set(filename, color=0):
    attrs = xattr(filename)
    if FinderInfo in attrs:
        previous = attrs[FinderInfo]
    else:
        previous = blank

    new = previous[:9] + chr(colors[color]) + previous[10:]
    attrs.set(FinderInfo, new)
    return new

if __name__ == '__main__':
    if len(argv) == 1:
        print 'Usage:\n{0} $filename $color\n'.format(argv[0])
        print 'Where color is one of:'
        print ', '.join(colors)
        print '\nOr just {0}'.format(argv[0]) 
    elif len(argv) == 2:
        try:
            print get(argv[1])
        except Exception as e:
            stderr.write(str(e))
            exit(e.errno)
    elif len(argv) == 3:
        try:
            set(argv[1], argv[2])
        except KeyError as e:
            stderr.write('Invalid color: {0}\n'.format(str(e)))
            stderr.write('Try one of:\n {0}\n'.format(', '.join(colors)))
            exit(1)
        except Exception as e:
            stderr.write(str(e))
            exit(e.errno)
