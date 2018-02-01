#!/usr/bin/env python

# Make 16-long bars of white at each end
# Also red, channel black pixels, then blue

import opc, time, random

client = opc.Client('localhost:7890')

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

sleep_time = 1./10
cycles_per_pattern = 32
while True:
    pixels = []
    for chan in range(8):
        for x in range(16):
            pixels.append(white)    
        for x in range(32):
            pixels.append(black)    
        for x in range(16):
            pixels.append(white)    
        pixels[chan*64+32-1-chan] = red
        pixels[chan*64+32] = blue
        pixels[chan*64+32+1+chan] = red
    client.put_pixels(pixels)
    time.sleep(sleep_time)
