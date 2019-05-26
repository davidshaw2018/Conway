"""
Just for testing methods in Conway game of life
"""
from string import *
from os import getcwd
import collections
import os
import random


import sys
# Dictionary mapping color names to RGB values
#
# colors: { ColorName: (red, green, blue) }
# colors = collections.defaultdict[lambda:None]

# colors = collections.defaultdict(lambda:None)
colors = dict()

lines = None
MYDIR = os.path.dirname(__file__)
color_file = 'rgb.txt'

with open(os.path.join(MYDIR,color_file)) as file_handle:
    lines = file_handle.readlines()

# Drop the first line which is not useful
lines = lines[2:len(lines)-2]

# Loop through each line

for line in lines:
    # Split based on spaces
    line = line.strip("\t\n")
    line = line.replace('\t'," ",2)
    line = line.split(" ")
    line = [item for item in line if item != ""]
    
    
    red = line[0]
    green = line[1]
    blue = line[2]
    
    
    name = line[3]

    # Save the color to a dict
    colors[name] = (int(red), int(green), int(blue))
    

print colors[random.choice(colors.keys())]