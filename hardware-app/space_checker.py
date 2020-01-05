import sensor
import statistics

threshold = 121.92

def isOccupied():
    # Check whether a space is occupied in a row
    distance = sensor.computeDistance()
    if distance < threshold:
        return True
    return False

def calibrate():
    threshold = getDistance()
    threshold = threshold * .70


    
def getDistance():
    distances = []

    for trial in range(0, 9):
        distances[trial] = sensor.computeDistance()
    
    medianDistance = statistics.median(distances)
    
    return medianDistance
