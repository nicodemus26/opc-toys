#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

numLEDs = 128
client = opc.Client('localhost:7890')

pixels = [ (0,0,0) ] * numLEDs
while True:
    # Let the colors run
    new_pixels = list(pixels)
    for i in range(numLEDs):
        r, g, b = 0, 0, 0
        for offset, mul in [(-2, .05), (-2, .15), (-1, .25), (0, .4), (1, .1), (2, .03)]:
            j = (numLEDs+offset+i) % numLEDs
            r = r + pixels[j][0]*mul
            g = g + pixels[j][1]*mul
            b = b + pixels[j][2]*mul
        new_pixels[i] = max(4, min(255, r)), max(4, min(255, g)), max(4, min(255, b))

    if(random.randint(0,3) > 0):
        # Add a new drop of color...
        drop_spot = random.randint(0, numLEDs)
        drop_color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        for offset, mul in [(0, .25), (1, .5), (2, .75), (3, .5), (4, .25)]:
            i = (offset + drop_spot) % numLEDs
            color = []
            for c in 0, 1, 2:
                color.append(drop_color[c]*mul + new_pixels[i][c]*(1-mul))
            new_pixels[i] = tuple(color)
    pixels = new_pixels
    discretized= [(int(r), int(g), int(b)) for (r, g, b) in pixels]
    client.put_pixels(discretized)
    time.sleep(1/10.)
