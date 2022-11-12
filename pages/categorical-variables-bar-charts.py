

import dash
from dash import html, dcc
from src.data_file import df
from src.utils import create_bar_chart, create_simple_grid
import dash_mantine_components as dmc
from dataclasses import fields
from src.utils import Columns


def create_list_with_bar_charts():
    categorical_columns = [field.default for field in fields(Columns.CategoricalVariables)]

    list_with_bar_charts = []

    for x in categorical_columns:
        list_with_bar_charts.append(
            dcc.Graph(
                figure=create_bar_chart(
                    df_=df, x_variable=x)
            )
        )

    return list_with_bar_charts


def test():
    return dmc.Container([

        create_simple_grid(
            input_list=create_list_with_bar_charts(),
            number_of_columns_in_row=2
        ),

        html.Hr(),
        html.Hr(),
        html.Br(),
        html.Br()

    ])


def layout():
    return test()


dash.register_page(__name__)


