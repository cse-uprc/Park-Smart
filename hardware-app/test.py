# test.py
# USED FOR TESTING PURPOSES ONLY NOT PART OF FINAL PROJECT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin numbers for the Trigger and Echo on the Ultrasonic Sensor
TRIG = 23
ECHO = 24

print ("Distance Measurement in Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Ensure the Trigger pin is set low and let the sensor settle
GPIO.output(TRIG, False)
print ("Waiting for Sensor to Settle")
time.sleep(2)

# Trigger the module for 10 microseconds to create a short pulse.
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

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
distance = pulse_duration * (SPEED_OF_SOUND / 2)

# Round the distance to 2 decimal places
distance = round(distance, 2)

print ("Distance:", distance, "cm")

GPIO.cleanup()


