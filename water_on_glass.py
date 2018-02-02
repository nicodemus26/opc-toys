#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time, random

strands = 8
num_leds = 64*strands
client = opc.Client('localhost:7890')

pulses = []
fps = 10
pps = 3
burstiness = 10
pulse_chance = float(pps)/(fps*burstiness):
print("%f chances per frame at %f probability each to generate a pulse" % (burstiness, pulse_chance))

class Pulse:
    position = -5
    height_mu = None
    height_sigma = None
    color = (255,255,255)
    pace_mu = None
    pace_sigma = None
    magnitude_mu = None
    magnitude_sigma = None
    def __init__(self):
        self.height_mu = max(.25, random.gauss(.5, 1))
        self.height_sigma = max(.25, random.gauss(.5, 1))
        self.pace_mu = max(.25, random.gauss(1, 3))
        self.pace_sigma = max(.25, random.gauss(.5, 1))
        self.magnitude_mu = min(.8, max(.2, random.gauss(.5, .2)))
        self.magnitude_sigma = min(.5, max(.05, random.gauss(.5, 1))
        color = (random.randint(0, 256), random.randint(0,256), random.randint(0,256))
    

def add_pulse():
    pass

def advance_pulses():
    pass

render_pulses():

while True:
    # Construct new pulses
    for x in range(burstiness):
        if random.random() > (pps/(fps*burstiness)):
            add_pulse()
    advance_pulses()
    client.put_pixels(render_pulses())
    time.sleep(1./fps)
