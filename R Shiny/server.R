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

getOccupiedTimeRange <- function(timeRange){
  # timeRange is a string that determines the amount of time
  # ex - "day", "week", "month"
  sampleTibble <- read_sheet(url, sheet=2)  # Get data from google sheets 

  # note the sheet param lets you access different sheets within the url
  dateTimes <- as.data.frame(sampleTibble)  # and convert it to a standard dataframe
  
  # To select the time range simply grab rows with time markers greater than the current time - interval
  if(timeRange == "Day"){
    dateTimes <- dateTimes[which(dateTimes$DateTime > (now()-ddays(1))),]
  }
  else if(timeRange == "Week"){
    dateTimes <- dateTimes[which(dateTimes$DateTime > (now()-dweeks(1))),]
  }
  else if(timeRange == "3 Weeks"){
    dateTimes <- dateTimes[which(dateTimes$DateTime > (now()-dweeks(3))),]
  }
  
  dateTimes   # Return dataframe with data
}

server <- function(input, output) {
  
  output$main_plot <- renderPlotly({
  
  # get and plot data from getOccupiedTimeRange()
  occupiedData <- getOccupiedTimeRange(input$view_by)
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
    
    p_gauge <- plot_ly(
      domain = list(x = c(0, 1), y = c(0, 1)),
      value = getAvailable(),
      title = list(text = "Available Spaces", font = list(size = 24)),
      gauge = list(
        axis = list(tickwidth = 1, tickcolor = "darkblue"),
        bar = list(color = "darkblue"),
        bgcolor = "white",
        borderwidth = 2,
        bordercolor = "gray",
        steps = list(
          list(range = c(0, 6), color = "cyan"),
          list(range = c(6, 10), color = "royalblue")
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

    #hist(faithful$eruptions,
    #     probability = TRUE,
    #     breaks = as.numeric(input$n_breaks),
    #     xlab = "Duration (minutes)",
    #     main = "Geyser eruption duration")
    
    # Pie Chart from data frame with Appended Sample Sizes
    
    
    #if (input$individual_obs) {
    #  rug(faithful$eruptions)
    #}
    
    #if (input$density) {
    #  dens <- density(faithful$eruptions,
    #                  adjust = input$bw_adjust)
    #  lines(dens, col = "blue")
    #}
 