import time
import threading, Queue

from rotary_class import RotaryEncoder
from Adafruit_CharLCD import Adafruit_CharLCD

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

while True:
    time.sleep(0.2)
    if(
