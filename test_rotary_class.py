import sys
import time
from rotary_class import RotaryEncoder

PIN_A = 2
PIN_B = 3
BUTTON = 4

def switch_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        print "Clockwise"
    elif event == RotaryEncoder.ANTICLOCKWISE:
        print "Anticlockwise"
    elif event == RotaryEncoder.BUTTONDOWN:
        print "Button down"
    elif event == RotaryEncoder.BUTTONUP:
        print "Button up"
    return

rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,switch_event)

while True:
    time.sleep(0.5)
