# Load google apis
library(googlesheets4)
library(googledrive)
library(lubridate)
library(plotly)
sheets_auth(scope = "https://www.googleapis.com/auth/drive")
drive_auth(token = sheets_token())
url <- "https://docs.google.com/spreadsheets/d/1tfKdmx19QHB5thPQbzXjL8ze-jA0TPOM1Zyx3eGRkP4/edit?folder=0APHNUN_jVyb8Uk9PVA#gid=0"

getAvailable <- function(){
  sampleTibble <- read_sheet(url)
  sample <- as.data.frame(sampleTibble)
  numAvailable <- length(sample$Occupied[sample$Occupied == "FALSE"])
  numAvailable
}

getOccupiedTimeRange <- function(num_days){
  # timeRange is a string that determines the amount of time
  # ex - "day", "week", "month"
  sampleTibble <- read_sheet(url, sheet=2)  # Get data from google sheets 
  # note the sheet param lets you access different sheets within the url
  dateTimes <- as.data.frame(sampleTibble)  # and convert it to a standard dataframe
  # To select the time range simply grab rows with time markers greater than the current time - number of past days
  dateTimes <- dateTimes[which(dateTimes$DateTime > (now()-ddays(num_days))),]
  dateTimes   # Return dataframe with data
}

server <- function(input, output, session) {
  autoInvalidate <- reactiveTimer(1000)
  output$main_plot <- renderPlotly({
  # get and plot data from getOccupiedTimeRange()
  occupiedData <- getOccupiedTimeRange(input$numeric_date_range)
  p <- plot_ly(x=ymd_hms(occupiedData$DateTime),y=occupiedData$Occupied, type = 'scatter', mode='lines+markers')%>%
    layout(
      xaxis = list(
        tick = 'datetime',
        tickmode = 'linear'
      )
    )
  head(occupiedData)
  p   # display the plot
  })
  
  output$occupied_gauge <- renderPlotly({
    autoInvalidate()
    p_gauge <- plot_ly(
      domain = list(x = c(0, 1), y = c(0, 1)),
      value = getAvailable(),
      title = list(text = "Available Spaces", font = list(size = 24)),
      gauge = list(
        axis = list(range = list(0, 10), tickwidth = 1, tickcolor = "darkblue"),
        bar = list(color = "darkblue"),
        bgcolor = "white",
        borderwidth = 2,
        bordercolor = "gray",
        steps = list(
          list(range = c(0, 5), color = "green"),
          list(range = c(5, 7), color = "yellow"),
          list(range = c(7, 10), color = "red")
        ),
        threshold = list(
          line = list(color = "red", width = 4),
          thickness = 0.75,
          value = 490
        )
      ),
      type = "indicator",
      mode = "gauge+number") %>%
      layout(margin = list(l=20,r=30),
             font = list(color = "darkblue", family = "Arial"))
    p_gauge
  })
}