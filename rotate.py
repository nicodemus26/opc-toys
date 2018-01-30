#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

numLEDs = 128
client = opc.Client('localhost:7890')

colors = []
for i in range(0, 256):
    r = i
    g = 0
    b = 256-i
    colors.append((r,g,b))
for i in range(0, 256):
    g = i
    b = 0
    r = 256-i
    colors.append((r,g,b))
for i in range(0, 256):
    b = i
    r = 0
    g = 256-i
    colors.append((r,g,b))
while True:
    for x in colors:
        pixels = [ x ] * numLEDs
        client.put_pixels(pixels)
        time.sleep(.01)
