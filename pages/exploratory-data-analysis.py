from dataclasses import fields

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio

from src.utils import Columns, create_scatter_plot, create_histogram
from src.data_file import df

pio.renderers.default = 'browser'


def create_simple_grid(
        input_list: list,
        number_of_columns_in_row: int
):
    return dmc.SimpleGrid(
        cols=number_of_columns_in_row,
        children=input_list
    )


def create_list_with_simple_scatter_plots():
    categorical_columns = [field.default for field in fields(Columns.CategoricalVariables)]
    numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

    list_with_scatter_charts = []

    for x in numerical_columns:
        for y in numerical_columns:
            if x == y:
                continue
            list_with_scatter_charts.append(
                dcc.Graph(
                    figure=create_scatter_plot(df_=df.sample(n=1000), x=x, y=y)
                )
            )

    return list_with_scatter_charts


def create_list_with_histograms():

    numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

    list_with_histograms = []

    for ii in numerical_columns:
        list_with_histograms.append(
            dcc.Graph(
                figure=create_histogram(
                    df_=df.sample(n=1000),
                    numerical_column=ii
                )
            )
        )

    return list_with_histograms


def create_list_with_histograms_color():

    categorical_columns = [field.default for field in fields(Columns.CategoricalVariables)]
    numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

    list_with_histograms_color = []

    for x in numerical_columns:
        for y in categorical_columns:
            list_with_histograms_color.append(
                dcc.Graph(
                    figure=create_histogram(
                        df_=df.sample(n=1000),
                        numerical_column=x,
                        color_=y
                    )
                )
            )

    return list_with_histograms_color


def eda():
    return dmc.Container([

        create_simple_grid(
            input_list=create_list_with_simple_scatter_plots(),
            number_of_columns_in_row=2
        ),

        html.Hr(),
        html.Hr(),
        html.Br(),
        html.Br(),

        create_simple_grid(
            input_list=create_list_with_histograms(),
            number_of_columns_in_row=2
        ),

        html.Hr(),
        html.Hr(),
        html.Br(),
        html.Br(),

        create_simple_grid(
            input_list=create_list_with_histograms_color(),
            number_of_columns_in_row=2
        ),

        html.Hr(),
        html.Hr(),
        html.Br(),
        html.Br(),


    ])


def layout():
    return eda()


dash.register_page(__name__)
