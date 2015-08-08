# PytoJ_Demo
Sample Python application calling J functions. It's a simple PyGame application that uses J to perform most of the logic.
## Dependencies
* Python 2.7
* PyGame: > http://www.pygame.org/download.shtml
* J: Linux : `libj.so` , Windows `j.dll` > http://jsoftware.com/

## How to use
After all dependencies are installed,
``` python uipytoj.py```


It is only a demonstration, and the main point of this project is the file `pytoj.py`. This file is entirely based on the Python J interface given here:
> http://www.jsoftware.com/pipermail/programming/2013-November/033974.html

This file allows calling verbs and returning J values from Python.

## Why?
This is a demonstration of another way to communicate between J and other programming languages. For a similar C/C++ interface see
> https://github.com/jonghough/CPP2J_Demo
