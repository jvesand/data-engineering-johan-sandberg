import plotly_express as px
import numpy as np
from dash import Dash, dcc, Output, Input
from dash.html import H1, Div, P, H2

app = Dash(__name__)

dropdown_options = [{"label": rolls, "value": rolls} for rolls in [10,100,1000,10000]]

app.layout = Div([
    H1("Dice simulator"),
    P("Chooce number of dice and number of rolls"),
    dcc.Graph(id = "dice-graph"),
    H2("Number of rolls"),
    dcc.Dropdown(id = "number-rolls", options = dropdown_options, value = 10),
    H2("Number of dice"),
    dcc.Slider(id = "number-dice", min=1, max=6, step=1, value=2)
])

@app.callback(Output("dice-graph", "figure"), Input("number-rolls", "value"), Input("number-dice", "value"))
def _dice_simulator_histogram(rolls, number_dice):
    dice = np.random.randint(1,7, size = (rolls, number_dice))
    return px.histogram(dice.sum(axis = 1))

if __name__ == "__main__":
    print("Hello from the docker side")
    app.run_server(debug = True)
