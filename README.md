# display_colors.py

Set or inspect the colors of files and folders for OSX Finder from the commandline.

## Usage:

### To find out the color of a file or folder:

``` display_colors.py $filename ```

You can check multiple files at once, with:

``` display_colors.py $file1 $file2 $file3 ```

or from the shell, wildcards.

### To set the color:

``` display_colors.py $color $filename ```

You can assign multiple files at once by:

``` display_colors.py $color $filename $filename2 $filename3 $etc```

so in a shell:

``` display_colors.py red *.py ```

would set all python scripts to red.

Options for colors are:

- none, gray, green, purple, blue, yellow, red, orange

If you're worried that you may have files in the list which could be valid color names,
then simply invoke using path names ( ./filename rather than filename, or with wildcards
./* rather than *).

This is good practice in general.

## Installing:

Copy the display_colors.py to somewhere in your $PATH
(usually /usr/local/bin works...) and run

``` chmod +x /usr/local/bin/display_colors.py ```
