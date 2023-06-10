library(shiny)
ui <- fluidPage(
  div(
    style = "display: flex; justify-content: center; align-items: center; height: 100vh;",
    h1("Hello from Shiny App!!", style = "font-size: 72px; text-align: center;")
    )
)
server <- function(input, output) {
  
}
shinyApp(ui, server)