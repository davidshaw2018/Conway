"""
Just for testing methods in Conway game of life
"""
from string import *
from os import getcwd

import sys
# Dictionary mapping color names to RGB values
#
# colors: { ColorName: (red, green, blue) }
colors = defaultdict(lambda: None)

lines = None

with open('rgb.txt') as file_handle:
    lines = file_handle.readlines()

# Drop the first line which is not useful
lines = [1:]

# Loop through each line
for line in lines:
    # Split based on spaces
    line = line.split(" ")

    # Remove all empty strings
    line = [item for item in line if item != ""]

    red = line[0]
    green = line[1]
    blue = line[2]

    name = line[3]

    # Save the color to a dict
    colors[name] = (red, green, blue)

print line[5]