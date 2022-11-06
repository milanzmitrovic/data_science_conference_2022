

import dash
import dash_mantine_components as dmc
from dash import Input, Output, dcc, callback
import pandas as pd
import scipy.stats as st

from src.utils import IDs, create_histogram, distributions


def bar_chart_with_population_and_sample_data():

    return dmc.Container([

        dmc.Space(h=30),

        dcc.Dropdown(
            options=[{'label': k, 'value': v} for k, v in distributions.items()],
            id=IDs.bar_chart_with_population_and_sample_data_dropdown,
            value=distributions['Normal']
        ),

        dcc.Graph(
            id=IDs.bar_chart_with_population_and_sample_data_distribution
        ),

        dmc.Text('Sample size'),
        dcc.Slider(
            id=IDs.bar_chart_with_population_and_sample_data_slider,
            min=1,
            max=100,
            value=5
        ),

        dcc.Graph(
            id=IDs.bar_chart_with_population_and_sample_data_sample_distribution
        )

    ])


@callback(
    Output(component_id=IDs.bar_chart_with_population_and_sample_data_distribution, component_property='figure'),
    Output(component_id=IDs.bar_chart_with_population_and_sample_data_sample_distribution,
           component_property='figure'),

    Input(component_id=IDs.bar_chart_with_population_and_sample_data_slider, component_property='value'),
    Input(component_id=IDs.bar_chart_with_population_and_sample_data_dropdown, component_property='value')
)
def callback_update_two_charts(
        sample_size: int,
        distribution_: str
):
    data = eval(distribution_)

    dff = pd.DataFrame({'distribution_data': data})

    fig_distributions = create_histogram(
        df_=dff,
        numerical_column='distribution_data'
    )

    sample_means = []

    for i in range(200):
        mean_ = dff.sample(n=int(sample_size))['distribution_data'].mean()
        sample_means.append(mean_)

    dff = pd.DataFrame({'sample_means': sample_means})

    fig_sample_means = create_histogram(df_=dff, numerical_column='sample_means')

    return fig_distributions, fig_sample_means


def layout():
    return bar_chart_with_population_and_sample_data()


dash.register_page(__name__)

