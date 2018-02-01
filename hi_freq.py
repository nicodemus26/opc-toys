#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

num_leds = 512
client = opc.Client('localhost:7890')

color_run = [(-2, 1.2), (-2, -.7), (-1, -1), (0, .40), (1, .1), (2, .02)]
drop_blur = [(0, .25), (1, .5), (2, .95), (3, .5), (4, .25)]

# Add horizontal siblings to blur
scale = .8
total = sum([mul for (_, mul) in color_run])
spare = total*(1-scale)
middle = [(off, mul*scale) for (off, mul) in color_run]
left   = [(off-64, mul*spare/2) for (off, mul) in color_run]
right  = [(off+64, mul*spare/2) for (off, mul) in color_run]
color_run = left + middle + right
total = sum([mul for (_, mul) in color_run])
print("Run total: %f" % total)

# Add horizontal drop splash
scale = .8
total = sum([mul for (_, mul) in drop_blur])
spare = total*(1-scale)
middle = [(off, mul*scale) for (off, mul) in drop_blur]
left   = [(off-64, mul*spare/2) for (off, mul) in drop_blur]
right  = [(off+64, mul*spare/2) for (off, mul) in drop_blur]
drop_blur = left + middle + right
total = sum([mul for (_, mul) in drop_blur])
print("Drop total: %f" % total)

pixels = [ (0,0,0) ] * num_leds
while True:
    # Let the colors run
    new_pixels = list(pixels)
    for i in range(num_leds):
        r, g, b = 0, 0, 0
        for offset, mul in color_run:
            j = (num_leds+offset+i) % num_leds
            r = (r + pixels[j][0]*mul) % 256
            g = (g + pixels[j][1]*mul) % 256
            b = (b + pixels[j][2]*mul) % 256
        new_pixels[i] = max(2, min(255, r)), max(2, min(255, g)), max(2, min(255, b))

    for x in range(num_leds*6/64):
        if(random.randint(0,12) == 0):
            # Add a new drop of color...
            drop_spot = random.randint(0, num_leds)
            drop_color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            for offset, mul in drop_blur:
                i = (offset + drop_spot) % num_leds
                color = []
                for c in 0, 1, 2:
                    color.append(drop_color[c]*mul + new_pixels[i][c]*(1-mul))
                new_pixels[i] = tuple(color)
    pixels = new_pixels
    client.put_pixels(pixels)
    time.sleep(.2)
