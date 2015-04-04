import time
import RPi.GPIO as GPIO

class PushButton:

    BUTTONDOWN=3
    BUTTONUP=4

    def __init__(self,button,callback):
        self.button = button
        self.callback = callback

        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.button_event, bouncetime=200)
        return

    def button_event(self,button):
        if GPIO.input(button):
            event = self.BUTTONUP
        else:
            event = self.BUTTONDOWN
	    state = GPIO.input(button)
	    while state == GPIO.input(button):
		time.sleep(0.1)
		event = self.BUTTONDOWN
                self.callback(event)

        self.callback(event)
        return

