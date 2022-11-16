
from dash import dash_table
import scipy.stats as st
import pandas as pd
import dash
import dash_mantine_components as dmc
from dash import html, dcc


df = pd.read_table('data/rrr.tsv')


def data_table():

    return dmc.Container(
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            page_size=30
        )
    )


def layout():

    return dmc.Container([

        html.H1('Intro to Statistics'),

        dmc.Space(h=40),

        html.H2('What is statistics?'),
        html.Li(
            html.H3('Statistics refers to numerical facts')
        ),
        html.Li(
            html.H3('Statistics refers to the field of study')
        ),

        dmc.Space(h=40),

        html.H2('Importance of statistics'),
        html.Li(
            html.H3('Population')
        ),
        html.Li(
            html.H3('Census')
        ),
        html.Li(
            html.H3('A lack of census')
        ),
        html.Li(
            html.H3('Sample ')
        ),
        html.Li(
            html.H3('Inferential statistics')
        ),

        dmc.Space(h=40),

        html.H2('Basic terms'),

        dmc.Space(h=10),

        data_table(),

        dmc.Space(h=10),

        html.Li(
            html.H3('Element of a sample or population')
        ),
        html.Li(
            html.H3('Variable')
        ),
        html.Li(
            html.H3('Observation')
        ),
        html.Li(
            html.H3('Data set')
        ),

        dmc.Space(h=40),

        html.H2('Types of variables'),
        html.Li(
            html.H3('Quantitative variable ')
        ),
        html.Li(
            html.H3('Types of quantitative variable: discrete variable or continuous variable')
        ),
        html.Li(
            html.H3('Qualitative or categorical variable')
        ),

        dmc.Space(h=60)


    ])


dash.register_page(__name__)

