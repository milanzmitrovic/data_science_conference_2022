
import dash_mantine_components as dmc
from dash import dcc, html
import dash
import numpy as np
import plotly.express as px
from dash import Input, Output, callback
from scipy.stats import norm, t


def layout():

    return dmc.Container([

        html.H2('Width of a confidence interval'),

        dmc.Space(h=20),

        dcc.Input(
            id='level_of_confidence',
            value=0.95,
            min=0.1,
            max=0.99
        ),

        dcc.Input(
            id='sample_size',
            value=30,
            min=10,
            max=1000
        ),

        dcc.Graph(id='interactive-confidence-interval'),

        html.H3('If we want to decrease the width of a confidence interval, we have two options:'),
        html.Li(html.H4('Lower the confidence level')),
        html.Li(html.H4('Increase the sample size')),


    ])


@callback(
    Output(component_id='interactive-confidence-interval', component_property='figure'),
    Input(component_id='level_of_confidence', component_property='value'),
    Input(component_id='sample_size', component_property='value')
)
def interactive_chart(level_of_confidence, sample_size):

    sample_size = int(sample_size)
    level_of_confidence = float(level_of_confidence)

    #

    m = 0
    s = 5

    dof = sample_size - 1
    t_crit = np.abs(t.ppf((1 - level_of_confidence) / 2, dof))
    min_, max_ = (m - s * t_crit / np.sqrt(sample_size), m + s * t_crit / np.sqrt(sample_size))

    #
    x = np.linspace(t.ppf(0.0001, df=dof), t.ppf(0.9999, df=dof), 100)
    y = t.pdf(x, df=dof)

    fig = px.scatter(x=x, y=y, template='simple_white')
    fig.add_vline(x=min_, line_color="green", line_width=4)
    fig.add_vline(x=max_, line_color="green", line_width=4)

    return fig


dash.register_page(__name__)


