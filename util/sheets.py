import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []
sheet1 = None
sheet2 = None
idnum = 0
sheet = None
client = None
rowCount = None

OCCUPIED_STRING = "OCCUPIED"

def isThereParking():
    return (spacesAvailable() > 0)
    
def spacesAvailable():
    
    sheetData = [] # Get CSV from Google Sheets to parse
    
    parkingSpaceCount = 0

    for str in sheetData:
        if (str != OCCUPIED_STRING):
            parkingSpaceCount = parkingSpaceCount + 1
    
    return parkingSpaceCount
   
def makeConnection():
    # Make the connection to the Google Spreadsheet
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    global client
    client = gspread.authorize(creds)
    global sheet1
    sheet1 = client.open('park-smart-264104').get_worksheet(0)
