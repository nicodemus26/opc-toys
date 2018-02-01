#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

numLEDs = 512
client = opc.Client('localhost:7890')

colors = []
for i in range(0, 255):
    r = i
    g = 0
    b = 255-i
    colors.append((r,g,b))
for i in range(0, 255):
    g = i
    b = 0
    r = 255-i
    colors.append((r,g,b))
for i in range(0, 255):
    b = i
    r = 0
    g = 255-i
    colors.append((r,g,b))
while True:
    for x in colors:
        pixels = [ x ] * numLEDs
        client.put_pixels(pixels)
        time.sleep(.01)
