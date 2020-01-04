# sensor.py
# Library for abstraction of getting data from sensor.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin numbers for the Trigger and Echo on the Ultrasonic Sensor
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def computeDistance():
    # Trigger the sensor and get back the distance between itself and the object it is pointed at.
    GPIO.output(TRIG, False)
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    end = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()
        if(start - end > 1):
            break

    while GPIO.input(ECHO) == 1:
        end = time.time()
        if(end - start > 1):
            break

    pulse_length = end - start

    distance = pulse_length / 0.000058

    time.sleep(.1)
    GPIO.cleanup()

    return distance
