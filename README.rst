=================
finder_colors.py
=================

Set or inspect the colors that Apple OSX Finder assigns to files or folders.

Usable as a standalone script, or it can be imported as a python module.

=================
Standalone Usage:
=================

To find out the color of a file or folder: ::

    finder_colors.py $filename

returns: ::

    filename    colorname

You can check multiple files at once, with: ::

    finder_colors.py $file1 $file2 $file3

or from the shell, wildcards ::

    finder_colors.py *.txt

To set the color: ::

    finder_colors.py $color $filename

You can assign multiple files at once by: ::

    finder_colors.py $color $filename $filename2 $filename3 $etc

so in a shell: ::

    finder_colors.py red *.py

would set all python scripts to red.

Options for colors are: ::

    none, gray, green, purple, blue, yellow, red, orange

If you're worried that you may have files in the list which could be valid
color names, then simply invoke using path names ( `./filename` rather than
`filename`, or with wildcards `./*` rather than `*`).

This is good practice in general.

===================
As a python module:
===================

After installing (by PIP): ::

    >>> import finder_colors
    >>> finder_colors.get('/path/to/file')
    'none'

    >>> finder_colors.set('/path/to/file', 'red')
    '\x00........'

The value returned by `set(pathname, color)` is the complete
com.apple.FinderInfo attribute list of that file.  You can probably ignore it.

=============
Installation:
=============

Either with pip ::

    pip install finder_colors

Or simply download the finder_colors.py script, and put it somewhere in
your $PATH (usually /usr/local/bin works...) and run ::

    chmod +x /usr/local/bin/finder_colors.py

========
Licence:
========

MIT Licenced, so pretty much do what you want with it.  Here's the details:

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

Enjoy!
