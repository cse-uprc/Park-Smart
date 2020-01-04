import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = []
creds = []

sheet = None
client = None

# Getters

def isThereParking():
    return (spacesAvailable() > 0)

def occupiedStatusList():
    # Returns a list of bools that signify which parking spots are occupied

    connectSheet() # Refresh the sheet values
    statusList = sheet.col_values(2)[1:] # Get all booleans concerning occupation status

    for status in statusList: # Cast all values to boolean for sanity checking
        status = bool(status)

    return statusList

def spacesAvailable():
    occupiedStatuses = occupiedStatusList()  # Get CSV from Google Sheets to parse

    parkingSpaceCount = 0

    for i in range(0, len(occupiedStatuses)):
        if isOccupied(i):
            parkingSpaceCount = parkingSpaceCount + 1

    return parkingSpaceCount

def isOccupied(zeroIndexedSpaceNumber):
    occupiedStatuses = occupiedStatusList() # Get CSV from Google Sheets to parse
    return occupiedStatuses[zeroIndexedSpaceNumber].lower() == "true" # Get from list, cast to bool

def getParkingSpaceCount():
    occupiedStatuses = occupiedStatusList() # get list of booleans from Google Sheets spreadsheet
    return len(occupiedStatuses) # Return the number of booleans in the list.

# Setters

def setOccupied(zeroIndexedSpaceNumber):
    connectSheet() # Refresh state
    sheet.update_cell(2 + zeroIndexedSpaceNumber, 2, True); # Set the specified space to be occupied

def setVacant(zeroIndexedSpaceNumber):
    connectSheet() # Refresh state
    sheet.update_cell(2 + zeroIndexedSpaceNumber, 2, False); # Set the specified space to be unoccupied

def setParkingSpaceCount(oneIndexedSpaceNumber):
    if (oneIndexedSpaceNumber < 1):
        return

    initialIndex = getParkingSpaceCount() # Get number of parking spaces in lot.

    # If the index is greater than the list length, then allocate more rows
    #  to the table and ID accordingly.
    if oneIndexedSpaceNumber > initialIndex:
        for i in range( (initialIndex + 2),(oneIndexedSpaceNumber + 2) ):
            sheet.update_cell(i, 1, i-2)
            sheet.update_cell(i, 2, False)
    # Otherwise, if lesser, eliminate all items indexed at/after oneIndexedSpaceNumber.
    elif oneIndexedSpaceNumber < initialIndex:
        for i in range( (oneIndexedSpaceNumber + 2),(initialIndex + 2)):
            sheet.update_cell(i, 1, "")
            sheet.update_cell(i, 2, "")

    # If the length is the same as it already is, make no changes.

#
# All backend stuff to do with google sheets stuff
#

def connectSheet():
    if uninitialized():
        makeConnection()

def uninitialized():
    return (sheet == None)

def makeConnection():
    # Make the connection to the Google Spreadsheet
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    global client
    client = gspread.authorize(creds)
    global sheet
    sheet = client.open('parking-status').sheet1

# ALL CODE THAT IS RUN FOR CERTAIN IS RUN HERE
