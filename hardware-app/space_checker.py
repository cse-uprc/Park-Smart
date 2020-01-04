import sensor

THRESHOLD_HEIGHT = 121.92

def isOccupied():
    # Check whether a space is occupied in a row
    distance = sensor.computeDistance()
    if distance < THRESHOLD_HEIGHT:
        return True
    return False