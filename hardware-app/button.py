import RPi.GPIO as GPIO
import controller

count = 0

BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_callback(channel):
    global count
    if count == 0:
        controller.calibrate()
        count += 1
    else:
        controller.updateRow()
        count += 1

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback(channel))

GPIO.cleanup()