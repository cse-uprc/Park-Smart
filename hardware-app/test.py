# test.py
# USED FOR TESTING PURPOSES ONLY NOT PART OF FINAL PROJECT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin numbers for the Trigger and Echo on the Ultrasonic Sensor
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Ensure the Trigger pin is set low and let the sensor settle
    GPIO.output(TRIG, False)
    time.sleep(2)

    # Trigger the module for 10 microseconds to create a short pulse.
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    # Get the timestamp for the last low point of the Echo pin
    while GPIO.input(ECHO) == 0:
         pulse_start = time.time()

    # Get the timestamp for the last high point of the Echo pin
    while GPIO.input(ECHO) == 1:
         pulse_end = time.time()

    # Get the elapsed time from the start and end times
    pulse_duration = pulse_end - pulse_start

    # The speed of sound at sea level is 343 m/s
    SPEED_OF_SOUND = 34300

    # Get the distance between the sensor and its object
    distance = (pulse_duration * SPEED_OF_SOUND) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
