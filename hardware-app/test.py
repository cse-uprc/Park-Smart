# test.py
# USED FOR TESTING PURPOSES ONLY NOT PART OF FINAL PROJECT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin numbers for the Trigger and Echo on the Ultrasonic Sensor
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for Sensor"
time.sleep(2)

while True:
    GPIO.output(TRIG,True)
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

    sig_time = end - start

    #cm:
    distance = sig_time / 0.000058

    print ('Distance:{} cm'.format(distance))
    time.sleep(.1)
GPIO.cleanup()
