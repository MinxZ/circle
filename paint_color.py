import argparse
import optparse
import sys
import turtle
from turtle import *

import numpy as np

parser = optparse.OptionParser(description='paint')
parser.add_option('--name', type=str, default='paint',
                  help='file name')
parser.add_option('--n_edges', type=int, default=6, help='number_of_edges')
parser.add_option('--n_forward', type=int, default=120, help='number of forwards')
parser.add_option('--pattern', type=int, default=-2, help='index of pattern, e.g. -2, -1, 0, 1, 2, ...')
parser.add_option('--color', type=str, default='monocolor', help='color, e.g. monocolor, red, ...')

(opts, args) = parser.parse_args()
argvs = sys.argv

# fibonacci_numbers = [0, 1]
# for i in range(2, opts.n_forward):
#     fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
#

# if opts.color == 'colorful':
#     colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# else:
#     colors = [opts.color] * 6
#


speed(0)
bgcolor("Black")


def rotation():
    n = 0
    c = 0
    colormode(255)
    for count in range(opts.n_forward):
        # decide color
        if opts.color == 'monocolor':
            c += int(255 / opts.n_forward)
            # pencolor(np.uint8(-c), np.uint8(-c), np.uint8(-c))
            pencolor(np.uint8(c), np.uint8(c), np.uint8(c))
        else:
            # you can change color as you like here
            start = 255
            c += int(start / opts.n_forward)
            # pencolor(np.uint8(start - c), np.uint8(start - c), np.uint8(c))
            # pencolor(np.uint8(c), np.uint8(start - c), np.uint8(start - c))
            pencolor(np.uint8(-c), np.uint8(0), np.uint8(0))
        # draw an n_edges polygon
        for i in range(opts.n_edges):
            # pencolor(colors[x % 6])
            forward(count)
            left(int(360 / opts.n_edges) + opts.pattern)
        n += 1
        left(3)
        print(count)


penup()
goto(0, 0)
pendown()
rotation()
hideturtle()
ts = getscreen()
bgcolor("Black")
ts.getcanvas().postscript(file=f"{opts.name}_{opts.n_forward}_{opts.n_edges}_{opts.pattern}_{opts.color}.eps")
print('end')
exit()
