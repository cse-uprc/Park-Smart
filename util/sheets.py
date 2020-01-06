import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from datetime import *

scope = []
creds = []

sheet = None
logSheet = None
client = None

DATE_FORMAT_STRING = "%Y-%m-%d %H:%M:%S EST"

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
    index = 2 + zeroIndexedSpaceNumber

    if not isOccupied(zeroIndexedSpaceNumber): # If there is a state change, log it in the log sheet.
        logOccupation()

    sheet.update_cell(index, 2, True); # Set the specified space to be occupied

def setVacant(zeroIndexedSpaceNumber):
    connectSheet() # Refresh state
    index = 2 + zeroIndexedSpaceNumber

    if isOccupied(zeroIndexedSpaceNumber): # If there is a state change, log it in the log sheet.
        logVacancy()

    sheet.update_cell(index, 2, False); # Set the specified space to be unoccupied

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
    if isUninitialized():
        makeConnection()

def isUninitialized():
    return (sheet == None)

def makeConnection():
    # Make the connection to the Google Spreadsheet
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    global client
    client = gspread.authorize(creds)
    global sheet
    global logSheet
    sheet = client.open('parking-status').get_worksheet(0)
    logSheet = client.open("parking-status").get_worksheet(1)

#
# DateTime stuff
#

def dateTimeFormat(dateTimeValue):
    return dateTimeValue.strftime(DATE_FORMAT_STRING)

def logVacancy(dateTimeValue = datetime.now()):
    timeListIndex = len(logSheet.col_values(1)) + 1    # Get row to insert time in
    logSheet.update_cell(timeListIndex, 1, dateTimeFormat(dateTimeValue)) # Insert time into list.
    newLogValue = int(logSheet.cell(timeListIndex - 1, 2).value) - 1 # Get new count of people in lot
    logSheet.update_cell(timeListIndex, 2, newLogValue) # Set new count of people in lot to sheet

def logOccupation(dateTimeValue = datetime.now()):
    columnLength = len(logSheet.col_values(1)[1:]) # Read length of date column
    timeListIndex = columnLength + 2 # Get new index of insertion into log
    newOccupancyCount = 0

    if columnLength > 0: # If a previous value exists, our new occupancy is based on the previous value.
        newOccupancyCount = int(logSheet.cell(timeListIndex - 1, 2).value) + 1
    else:                # Otherwise, our new occupancy is 1 because we assume that our initial occupancy is 0.
        newOccupancyCount = 1

    logSheet.update_cell(timeListIndex, 1, dateTimeFormat(dateTimeValue)) # Set new date in column 1
    logSheet.update_cell(timeListIndex, 2, newOccupancyCount) # Set new occupancy count in column 2


# ALL CODE THAT IS RUN FOR CERTAIN IS RUN HERE
