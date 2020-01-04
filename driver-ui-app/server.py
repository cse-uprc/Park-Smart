# Name: server.py
# Authors: Jacob Hunt, Joey Kilgore, Jared Makai, Jonathan Bender
# Python version: 3
#
# Description:
# The server for the web app

import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

NUMBER_OF_PARKING_SPACES = 10

# class to represent a parking space
class ParkingSpace:
    def __init__(self, id, isOccupied):
        self.id = int(id)
        self.isOccupied = bool(isOccupied)

    def serialize(self):
        return {
            'id': self.id,
            'isOccupied': self.isOccupied
        }

# array to represent the ten parking spaces
parkingSpaces = []

# root page
@app.route("/")
def index():
    return render_template("index.html")

# get current status for parking spaces
@app.route("/getParkingSpaces")
def getParkingSpace():
    return jsonify(
        # return a json of the parking space data
        parkingSpaceArray = [pSpace.serialize() for pSpace in parkingSpaces]
    );

# update the status for a parking space
@app.route("/updateParkingSpace")
def updateParkingSpace():

    # get remote input from an HTTP "post" request
    if request.method == "POST":
        requestData = request.form
        req_id = int(request.form.get("id"))
        req_isOccupied = request.form.get("isOccupied")
    
    # get remote input from an HTTP "get" request
    if request.method == "GET":
        requestData = request.args
        req_id = int(request.args.get("id"))
        req_isOccupied = request.args.get("isOccupied")
    
    try:
        if int(req_isOccupied) == 0:
            req_isOccupied = False
            parkingSpaces[req_id].isOccupied = req_isOccupied
        elif int(req_isOccupied) == 1:
            req_isOccupied = True
            parkingSpaces[req_id].isOccupied = req_isOccupied
        else:
            return jsonify(
                success = False,
                returnMessage = "Invalid input in HTTP request",
            )
    except:
        return jsonify(
            success = False,
            returnMessage = "A serverside exception occurred",
        )

    return jsonify(
        success = True,
        returnMessage = "Parking Space #" + str(req_id) + " Successfully Updated"
    );

# configure server
server_address = "0.0.0.0"
port_number = 8080

# start of program
if __name__ == "__main__":
    
    # put the ten parking spaces in the array
    for i in range (10):
        parkingSpaces.append(ParkingSpace(i, False))

    # run server
    app.run(host = os.getenv('IP', server_address), 
            port = int(os.getenv('PORT', port_number)))