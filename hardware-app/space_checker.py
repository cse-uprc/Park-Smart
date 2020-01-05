import sensor
import statistics

threshold = 121.92

def isOccupied():
    # Check whether a space is occupied in a row
    global threshold
    distance = getDistance()
    if distance < threshold:
        return True
    return False

def calibrate():
    global threshold
    threshold = getDistance()
    threshold = threshold * .9
    print ("New threshold: " + str(threshold))


    
def getDistance():
    distances = []

    s = 0

    while s < 5:
        distances.append(sensor.computeDistance())
        s += 1
    
    medianDistance = statistics.median(distances)
    
    return medianDistance
