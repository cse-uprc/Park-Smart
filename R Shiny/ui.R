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
           numericInput(inputId = "numeric_date_range", label = "Past Days: ", 1),
           plotlyOutput(outputId = "main_plot", width =  "90%", height = "90%")
    )
  )
)