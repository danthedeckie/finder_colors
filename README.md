# display_colors.py

Set or inspect the colors of files and folders for OSX Finder from the commandline.

## Usage:

``` display_colors.py $filename ```
Returns the folder color.

``` display_colors.py $filename $color ```
Sets the color.

Options for colors are:

- none, gray, green, purple, blue, yellow, red, orange

You can also do multiple files at a time:

``` display_colors.py * ```

or

``` display_colors.py this_file.txt ./that_file.png /etc/passwd ```

Displays each filename and it's color (each line is one file, and the filename and color are separated by a tab)

``` display_colors.py * red ```

Sets all the files to red.  If the final argument is a valid color, then it will be used.  If you're worried that
you may have files in the list which could be valid color names, then simply invoke using path names ( ./filename rather than filename, for instance).


## Installing:

Copy the display_colors.py to somewhere in your $PATH
(usually /usr/local/bin works...) and run

``` chmod +x /usr/local/bin/display_colors.py ```
