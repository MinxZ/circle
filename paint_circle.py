import argparse
import optparse
import sys
import turtle
from turtle import *

import numpy as np

parser = optparse.OptionParser(description='paint')
parser.add_option('--name', type=str, default='circle',
                  help='file name')
parser.add_option('--start_length', type=int, default=0, help='number of forwards')
parser.add_option('--end_length', type=int, default=120, help='number of forwards')
parser.add_option('--n_edges', type=int, default=6, help='number_of_edges')
parser.add_option('--pattern', type=int, default=-2, help='index of pattern, e.g. -2, -1, 0, 1, 2, ...')
parser.add_option('--color', type=str, default='monocolor', help='color, e.g. monocolor, red, ...')

(opts, args) = parser.parse_args()
argvs = sys.argv

if opts.color == 'colorful':
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
else:
    colors = [opts.color] * 6


speed(0)
# bgcolor("Black")


def rotation(start_length, end_length, n_edges, pattern, color):
    n = 0
    c = 0
    colormode(255)
    for count in range(start_length, end_length):
        # decide color
        if color == 'monocolor':
            c += int(255 / end_length)
            # pencolor(np.uint8(-c), np.uint8(-c), np.uint8(-c))
            pencolor(np.uint8(c), np.uint8(c), np.uint8(c))
        else:
            # you can change color as you like here
            start = 255
            c += int(start / end_length)
            # pencolor(np.uint8(start - c), np.uint8(start - c), np.uint8(c))
            # pencolor(np.uint8(c), np.uint8(start - c), np.uint8(start - c))
            pencolor(np.uint8(c), np.uint8(0), np.uint8(0))
        for i in range(n_edges):
            if color == 'colorful':
                pencolor(colors[i % 6])
            forward(count)
            left(int(360 / n_edges) + pattern)
        n += 1
        left(3)
        print(count)


penup()
goto(0, 0)
pendown()
rotation(opts.start_length, opts.end_length, opts.n_edges, opts.pattern, opts.color)
hideturtle()
ts = getscreen()
bgcolor("Black")
ts.getcanvas().postscript(file=f"{opts.name}_{opts.end_length}_{opts.n_edges}_{opts.pattern}_{opts.color}.eps")
print('end')
exit()
