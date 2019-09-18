import argparse
import optparse
import sys
import turtle
from turtle import *

parser = optparse.OptionParser(description='paint')
parser.add_option('--name', type=str, default='paint.eps',
                  help='file name')
parser.add_option('--n_edges', type=int, default=6, help='number_of_edges')
parser.add_option('--n_forward', type=int, default=120, help='number of forwards')

(opts, args) = parser.parse_args()
argvs = sys.argv

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
speed(0)
bgcolor("Black")
penup()
goto(0, 0)
pendown()
for x in range(opts.n_forward):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
hideturtle()
ts = getscreen()
ts.getcanvas().postscript(file=opts.name)
exit()
