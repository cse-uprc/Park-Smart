# Name: server.py
# Authors: Jacob Hunt, Joey Kilgore, Jared Makai, Jonathan Bender
# Python version: 3
#
# Description:
# The server for the web app

import os
from flask import Flask, render_template, request

app = Flask(__name__)

# root page
@app.route("/")
def index():
    return render_template("index.html")

# configure server
server_address = "0.0.0.0"
port_number = 8080

# run server
if __name__ == "__main__":
    app.run(host = os.getenv('IP', server_address), 
            port = int(os.getenv('PORT', port_number)))