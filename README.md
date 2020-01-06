# Park-Smart
Smart Parking

This project has multiple different pieces of software that combine to make ParkSmart!  

## Hardware-app  
This is the python application running on a raspberry pi that uses an [ultrasonic distance sensor](https://www.mouser.com/ProductDetail/Adafruit/3942?qs=byeeYqUIh0OD1hDPcrj%252BAQ%3D%3D&gclid=CjwKCAiA0svwBRBhEiwAHqKjFramVFJ-Ogx7izE9Igy5VTHyQoUAqEf5A3om5ZR8cm1drt1z759IUBoCrtoQAvD_BwE) to detect distance. The button.py script runs our demo script built for going through a row of 10 parking spaces.  
The demo script does the following  
1. Has a calibration step on an empty parking space  
2. Gives an LED light for showing when the pi is ready to read the next parking spot
3. The user clicks a button while holding the sensor over the parking spot, and this will then update the connected google sheet and web interface.  
4. Repeat steps 2 and 3 for all 10 parking spaces.  

## Driver-ui-app  
This python web application uses a database to keep track of which parking spaces are available or empty. The pi sends http requests to update the server, and the UI displays (in this demo) the 10 parking spaces with green markings to designate empty spots, and red markings to designate taken spots.  

## R Shiny  
This R shiny application reads the google sheet that the pi updates, and displays graphs showing the total available parking spaces in the demo parking garage, and shows the usage over a period of time.
