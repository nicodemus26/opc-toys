#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

num_leds = 128
client = opc.Client('localhost:7890')

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

sleep_time = 1./10
cycles_per_pattern = 32
while True:
    # red/blue alternate per strip
    for x in range(cycles_per_pattern):
        pixels = []
        if x % 2 == 0:
            while(len(pixels) < num_leds):
                pixels = pixels + ([red]*64)
                pixels = pixels + ([blue]*64)
        else:
            pixels = ([black]*num_leds)
        client.put_pixels(pixels)
        time.sleep(sleep_time)

    # white blinks
    for x in range(cycles_per_pattern/2):
        pixels = []
        if x % 2 == 0:
            while(len(pixels) < num_leds):
                pixels = pixels + ([white]*16)
                pixels = pixels + ([black]*16)
        else:
            while(len(pixels) < num_leds):
                pixels = pixels + ([black]*16)
                pixels = pixels + ([white]*16)
        client.put_pixels(pixels)
        time.sleep(sleep_time)

    # red/blue alternate per strip
    for x in range(cycles_per_pattern):
        pixels = []
        if int((float(x) / cycles_per_pattern)*8) %2 ==0:
            if x%2 == 0:
                pixels = ([red]*num_leds)
            else:
                pixels = ([black]*num_leds)
        else:
            if x%2 == 0:
                pixels = ([blue]*num_leds)
            else:
                pixels = ([black]*num_leds)
        client.put_pixels(pixels)
        time.sleep(sleep_time)

    # white blinks
    for x in range(cycles_per_pattern/2):
        pixels = []
        if x % 2 == 0:
            while(len(pixels) < num_leds):
                pixels = pixels + ([white]*16)
                pixels = pixels + ([black]*16)
        else:
            while(len(pixels) < num_leds):
                pixels = pixels + ([black]*16)
                pixels = pixels + ([white]*16)
        client.put_pixels(pixels)
        time.sleep(sleep_time)
