import RPi.GPIO as GPIO
import controller
import traceback
import sys

count = 0

BUTTON_PIN = 18
TRIG = 23
ECHO = 24
LED_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def button_callback():
    GPIO.output(LED_PIN, False)
    print("Button Pressed")
    global count
    if count == 0:
        controller.calibrate()
        count += 1
        print("Count: " + str(count))
    else:
        controller.updateRow(count - 1)
        count += 1
        print("Count: " + str(count))

try:
    global count
    while count < 11:
        GPIO.output(LED_PIN, True)
        if GPIO.input(BUTTON_PIN) == 1:
           button_callback()
except KeyboardInterrupt:
   GPIO.cleanup() 

except Exception:
    print("Oof")
    traceback.print_exc(file=sys.stdout)
    GPIO.cleanup()
