# Using sheets.py
Note: Deprecated.
## Getters
* isThereParking()
    - Is there at least one vacant parking space in the lot? Returns boolean as appropriate.
* spacesAvailable()
    - How many spaces are vacant in the lot? Returns an int as appropriate.
* isOccupied(int zeroIndexValue)
    - Is parking space number $zeroIndexValue occupied? Returns boolean as appropriate.
* occupiedStatusList()
    - Returns a list of unicode value strings containing "TRUE" and "FALSE" representing status of being occupied by a car.
* getParkingSpaceCount()
    - Returns the number of parking spaces allocated in the Google Sheets spreadsheet being accessed.

## Setters
* setOccupied(int zeroIndexValue)
    - Declares space number $zeroIndexValue to be occupied (set to TRUE)
* setVacant(int zeroIndexValue)
    - Declares space number $zeroIndexValue to be vacant (set to FALSE)
* setParkingSpaceCount(int oneIndexValue)
    - Sets the number of parking spaces described in the spreadsheet and either erases values or inserts vacant parking spaces as appropriate

## Backend stuff
these **do not** need to be called. They are used entirely by the other methods in this file.
* connectSheet()
    - If no connection has been made, make a connection to the spreadsheet.
* isUninitialized()
    - Return whether or not the sheet has been initialized in the first place.
* makeConnection()
    - Make outgoing connection to Google Sheets spreadsheet.
.
