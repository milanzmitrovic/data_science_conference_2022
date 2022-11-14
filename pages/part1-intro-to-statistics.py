
import scipy.stats as st
import pandas as pd
import dash
import dash_mantine_components as dmc
from dash import html, dcc


def layout():

    return dmc.Container([

        html.H1('Intro to Statistics'),

        html.H2('What is statistics?'),
        html.Li(
            html.H3('Statistics refers to numerical facts')
        ),
        html.Li(
            html.H3('Statistics refers to the field of study')
        ),


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

        html.H2('Basic terms'),
        html.Li(
            html.H3('Primer sutra ti saljem..........')
        ),
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

        html.H2('Types of variables'),
        html.Li(
            html.H3('Quantitative variable ')
        ),
        html.Li(
            html.H3('Types of quantitative variable: discrete variable or continuous variable')
        ),
        html.Li(
            html.H3('DQualitative or categorical variable')
        ),

        dmc.Space(h=60)


    ])


dash.register_page(__name__)

