#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

num_leds = 512
client = opc.Client('localhost:7890')

yellow = 51
purple = 57
purple_rocket = 0
while True:
    if (num_leds + purple + 1) % num_leds == (num_leds + yellow) % num_leds:
        yellow = (num_leds + yellow - 1) % num_leds
    else:
        if random.randint(0, 10) > (8 if (purple_rocket > 0) else 4):
            yellow = (num_leds + yellow - 1) % num_leds
        else:
            purple = (num_leds + purple - 1) % num_leds
    pixels = [(0, 0, 0)] * num_leds
    if purple_rocket != 0:
        pixels[(purple+1)%num_leds] = (64, 0, 64)
        pixels[(purple+2)%num_leds] = (32, 0, 32)
        pixels[(purple+3)%num_leds] = (64, 0, 32)
        pixels[(purple+4)%num_leds] = (32, 16, 16)
        purple_rocket = purple_rocket - 1
    elif random.randint(0, 50) == 0:
        purple_rocket = 15
    pixels[purple] = (128, 0, 128)
    pixels[yellow] = (128, 72, 0)
    client.put_pixels(pixels)
    time.sleep(.02)
