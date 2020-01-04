ui <- bootstrapPage(
  
  fluidRow(
    column(12,
           titlePanel("Generic Parking Garage Data"),
    ),
  ),
  
  fluidRow(
    column(12,
           titlePanel("")
    ),
  ),
  
  fluidRow(
    column(4,
        plotlyOutput(outputId = "occupied_gauge",inline = "False")
    ),
    column(8,
           selectInput(inputId = "view_by", label = "View Parking Usage By: ", c("Day", "Week", "3 Weeks")),
           plotlyOutput(outputId = "main_plot", width =  "90%", height = "90%")
       
    )
  )
)