import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio
import numpy as np


def layout():
    @callback(
        Output("graph", "figure"),
        Input("mean", "value"),
        Input("std", "value"))
    def callback_display_color(mean, std):
        data = np.random.normal(mean, std, size=500)  # replace with your own data source
        fig = px.histogram(data, range_x=[-20, 20], range_y=[0, 100], template='simple_white')
        return fig

    return dmc.Container([
        html.H4('Interactive normal distribution'),

        html.P("Mean:"),
        dcc.Slider(id="mean", min=-15, max=15, value=0,
                   ),
        html.P("Standard Deviation:"),
        dcc.Slider(id="std", min=1, max=10, value=1,
                   ),

        dcc.Graph(id="graph"),

    ])


layout()


dash.register_page(__name__)



