


import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


app = Dash(__name__)

app.layout = html.Div([
    html.H1('Welcome to Dash!'),

    dcc.Input(id='input_id'),

    html.H4(id='output_id')
])


@callback(
    Output(component_id='output_id', component_property='children'),
    Input(component_id='input_id', component_property='value')
)
def my_fun(input_):
    return f"You have just selected: {input_}"


if __name__ == '__main__':
    app.run_server(debug=True)

