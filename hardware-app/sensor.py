# sensor.py
# Library for abstraction of getting data from sensor.
import RPi.GPIO as GPIO
import time

def computeDistance():
    # Pin numbers for the Trigger and Echo on the Ultrasonic Sensor
    TRIG = 23
    ECHO = 24

    # Trigger the sensor and get back the distance between itself and the object it is pointed at.
    GPIO.output(TRIG, False)
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    start = time.time()
    end = time.time()
        
    print ("Getting start time...")

    while GPIO.input(ECHO) == 0:
        start = time.time()
        if(start - end > 1):
            break
    print ("Getting end time...")

    while GPIO.input(ECHO) == 1:
        end = time.time()
        if(end - start > 1):
            break

    pulse_length = end - start

    print("Pulse Length: " + str(pulse_length))

    distance = pulse_length / 0.000058
    print(distance)
    return distance
