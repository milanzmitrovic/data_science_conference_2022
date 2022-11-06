
import dash
import dash_mantine_components as dmc
from dash import Input, Output, dcc, callback
import pandas as pd
import numpy as np

from src.utils import IDs, create_histogram


def bar_chart_with_varying_bin_size():

    return dmc.Container([
        dmc.Space(h=30),
        dmc.Text('Select bin size'),
        dcc.Slider(
            id=IDs.bar_chart_with_varying_bin_size_slider,
            min=1,
            max=100,
            value=5
        ),

        dcc.Graph(id=IDs.bar_chart_with_varying_bin_size)
    ])


# This way of writing code does not work within Dash.Tabs
# Report bug!!!
@callback(
    Output(
        component_id=IDs.bar_chart_with_varying_bin_size,
        component_property='figure'
    ),

    Input(
        component_id=IDs.bar_chart_with_varying_bin_size_slider,
        component_property='value'
    )
)
def callback_update_bin_size(bin_size):

    data = np.random.normal(loc=0, scale=30, size=10000)

    dff = pd.DataFrame({'random_data': data})

    fig = create_histogram(
        df_=dff,
        numerical_column='random_data',
        number_of_bins=int(bin_size)
    )

    return fig


def layout():
    return bar_chart_with_varying_bin_size()


dash.register_page(__name__)



