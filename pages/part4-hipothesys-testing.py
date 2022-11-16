

import dash
import dash_mantine_components as dmc
from dash import dcc, html


def layout():

    return dmc.Container([

        html.H2('Hypothesis Testing'),

        dmc.Space(h=5),

        html.Li(html.H3('Why do we perform a test of hypothesis? ')),
        html.Li(html.H3('Null hypothesis')),
        html.Li(html.H3('Alternative hypothesis')),
        html.Li(html.H3('Significance level of the test')),

    ])


dash.register_page(__name__)


