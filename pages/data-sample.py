
from dataclasses import fields

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback, dash_table
import plotly.express as px
import pandas as pd
import plotly.io as pio

from src.utils import Columns, create_scatter_plot, create_histogram
from src.data_file import df

pio.renderers.default = 'browser'


def create_sample_data_table(df_: pd.DataFrame):

    return dmc.Container(
        dash_table.DataTable(
            data=df_.sample(n=100).to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            page_size=30
        ),
        style={'overflow-x': 'auto'}
    )


def layout():
    return html.Div([
        dmc.Space(h=40),
        create_sample_data_table(df_=df)
        ])


dash.register_page(__name__)

