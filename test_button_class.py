import sys
import time
from button_class import PushButton

BUTTON = 2 

def switch_event(event):
    if event == PushButton.BUTTONDOWN:
        print "Button down"
    elif event == PushButton.BUTTONUP:
        print "Button up"
    return

pbutton = PushButton(BUTTON,switch_event)

while True:
    time.sleep(0.5)
