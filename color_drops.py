#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

numLEDs = 128
client = opc.Client('localhost:7890')

pixels = [ (0,0,0) ] * numLEDs
while True:
    new_pixels = list(pixels)
    for i in range(numLEDs):
        r, g, b = 0, 0, 0
        for offset, mul in [(-2, .20), (-1, .6), (0, .19), (1, .2), (2, -.20)]:
            j = (numLEDs+offset+i) % numLEDs
            r = r + pixels[j][0]*mul
            g = g + pixels[j][1]*mul
            b = b + pixels[j][2]*mul
        new_pixels[i] = min(255, r), min(255, g), min(255, b)
    drop_spot = random.randint(0, numLEDs)
    drop_color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    for i in range(drop_spot, drop_spot+3):
        i = i % numLEDs
        new_pixels[i] = drop_color
    pixels = new_pixels
    discretized= [(int(r), int(g), int(b)) for (r, g, b) in pixels]
    client.put_pixels(discretized)
    time.sleep(1)
