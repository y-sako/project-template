
# pip install shiny

from shiny import App, ui

# Part 1: ui ----
app_ui = ui.page_fluid(
    "Hello from PyShiny!",
)

# Part 2: server ----
def server(input, output, session):
    ...

# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)
