#!/usr/bin/env python

# Make 16-long bars of white at each end
# Also red, channel black pixels, then blue

import opc, time

client = opc.Client('localhost:7890')

sleep_time = 1

def random_color():
    from random import randint
    return (
        randint(0, 256),
        randint(0, 256),
        randint(0, 256),
    )

while True:
    pixels = []
    for x in range(512):
        pixels.append(random_color())
    client.put_pixels(pixels)
    time.sleep(sleep_time)
