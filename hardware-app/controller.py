import space_checker as checker
import requests
import sheets

API_ENDPOINT = "http://parksmart2020.pythonanywhere.com/updateParkingSpace"

def updateRow(value):
    if checker.isOccupied():
        sheets.setOccupied(value)
        
        data = {
                'id':value,
                'isOccupied':1}
    else:
        sheets.setVacant(value)
        
        data = {
                'id':value,
                'isOccupied':0}
    r = requests.get(url = API_ENDPOINT, params = data)
    service_url = r.text
    print("The service URL is:%s"%service_url)
    
def calibrate():
    checker.calibrate()
