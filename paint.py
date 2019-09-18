import argparse
import optparse
import sys
import turtle
from turtle import *

import numpy as np

parser = optparse.OptionParser(description='paint')
parser.add_option('--name', type=str, default='paint',
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

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
speed(0)
scale = 5  # This isn't a turtle module setting.  This is just for us.

# Move the little buddy over to the left side to give him more room to work
penup()
setpos(0, 0)
# setpos(-390, 0)
pendown()

current = 0   # Here's how we know where we are
seen = set()  # Here's where we'll keep track of where we've been


def rotation(start_length, end_length, heading=90, n_edges=6, pattern=0, color='monocolor'):
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
            if heading == 90:
                left(int(360 / n_edges) + pattern)
            else:
                right(int(360 / n_edges) + pattern)
        n += 1
        left(3)
        print(count)


# Step increases by 1 each time
for step_size in range(1, 100):

    backwards = current - step_size

    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        forward(int(scale * step_size / 2))
        forward(int(scale * step_size / 2))
        setheading(90)  # 90 degrees is pointing straight up
        # 180 degrees means "draw a semicircle"
        circle(1, 180)
        rotation(start_length=int(scale * step_size / 2) - 1, end_length=int(scale * step_size / 2), heading=90)
        current = backwards
        seen.add(current)
        print(scale * step_size / 2)

    # Otherwise, go forwards
    else:
        setheading(270)  # 270 degrees is straight down
        circle(1, 180)
        rotation(start_length=int(scale * step_size / 2) - 1, end_length=int(scale * step_size / 2), heading=270)
        current += step_size
        seen.add(current)
        print(scale * step_size / 2)


hideturtle()
ts = getscreen()
bgcolor("Black")
ts.getcanvas().postscript(file=f"{opts.name}_{opts.end_length}_{opts.n_edges}_{opts.pattern}_{opts.color}.eps")
exit()
