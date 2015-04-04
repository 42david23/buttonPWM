import time
import threading, Queue
import RPi.GPIO as GPIO

from button_class import PushButton
from Adafruit_CharLCD import Adafruit_CharLCD

BUTTON1 = 2
BUTTON2 = 3 
PWM = 14

class PrinterWorkerThread(threading.Thread):
    def __init__(self, print_q):
        super(PrinterWorkerThread, self).__init__()
        self.print_q = print_q
        self.stoprequest = threading.Event()
        self.lcd = Adafruit_CharLCD()
        self.lcd.begin(16,1)
        self.lcd.clear()

    def run(self):
        while not self.stoprequest.isSet():
            try:
                to_print = self.print_q.get(True, 0.05)
                self.lcd.clear()
                self.lcd.message('%s' %(to_print))
                #self.lcd.message("Test")
                print("%s") % (to_print)
            except Queue.Empty:
                continue

    def join(self,timeout=None):
        self.stoprequest.set()
        super(PrinterWorkerThread, self).join(timeout)

print_q = Queue.Queue()

printer_thread = PrinterWorkerThread(print_q)

printer_thread.start()

def switch_event1(event):
    if event == PushButton.BUTTONDOWN:
	print_q.put("UP")
    elif event == PushButton.BUTTONUP:
	print_q.put("DOWN")
    return    
def switch_event2(event):
    if event == PushButton.BUTTONDOWN:
	print_q.put("UP2")
    elif event == PushButton.BUTTONUP:
	print_q.put("DOWN2")
    return

pbutton1 = PushButton(BUTTON1,switch_event1)
pbutton2 = PushButton(BUTTON2,switch_event2)

while True:
    time.sleep(0.2)