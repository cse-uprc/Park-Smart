// Number of milleseconds between updates
var INTERVAL = 2000;

// Function for updating the parking spaces
function updateParkingSpaces()
{
    $.getJSON("./getParkingSpaces", function(data) {
        for (var i = 0; i < data.parkingSpaceArray.length; i++)
        {
            console.log("boop!");
            $("#parking-spot-" + i + " > td").html(
                "<span class='"
              + (data.parkingSpaceArray[i].isOccupied ? "occupied" : "not-occupied")
              + "'>⬤</span>"
            );
        }
    }); 

}

// When document is loaded...
$(document).ready(function()
{
    // ... update the parking spaces
    updateParkingSpaces();

    // Keep updating the parking spaces every <INTERVAL> milliseconds
    setInterval(updateParkingSpaces, INTERVAL);
});