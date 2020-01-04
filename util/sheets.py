OCCUPIED_STRING = "OCCUPIED"

def isThereParking():
    return (spacesAvailable() > 0)
    

def spacesAvailable():
    
    sheetData = # Get CSV from Google Sheets to parse
    
    parkingSpaceCount = 0

    for str in sheetData:
        if (str != OCCUPIED_STRING):
            parkingSpaceCount = parkingSpaceCount + 1
    
    return parkingSpaceCount
   

