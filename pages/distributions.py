

import dash
import dash_mantine_components as dmc
from dash import Input, Output, dcc, callback
import pandas as pd
import scipy.stats as st


from src.utils import IDs, create_histogram, distributions


def bar_chart_with_distributions():
    @callback(
        Output(
            component_id=IDs.bar_chart_with_distributions_graph,
            component_property='figure'
        ),

        Input(
            component_id=IDs.bar_chart_with_distributions,
            component_property='value'
        )
    )
    def callback_update_distribution_graph(input_):
        data = eval(input_)

        dff = pd.DataFrame({'distribution_data': data})

        fig = create_histogram(
            df_=dff,
            numerical_column='distribution_data'
        )

        return fig

    return dmc.Container([

        dmc.Space(h=30),

        dcc.Dropdown(
            options=[{'label': k, 'value': v} for k, v in distributions.items()],
            id=IDs.bar_chart_with_distributions,
            value=distributions['Normal']
        ),

        dcc.Graph(id=IDs.bar_chart_with_distributions_graph)
    ])


def layout():
    return bar_chart_with_distributions()


layout()


dash.register_page(__name__)

