from dash import Dash, Input, Output, dcc, html, callback

from src.bar_chart_with_distributions import bar_chart_with_distributions
from src.bar_chart_with_population_and_sample_mean import bar_chart_with_population_and_sample_data
from src.bar_chart_with_varying_bin_size import bar_chart_with_varying_bin_size
from src.utils import IDs, TabNames


def create_tabs_content():
    @callback(
        Output(
            component_id=IDs.tab_output,
            component_property='children'
        ),

        Input(
            component_id=IDs.tab_input,
            component_property='value'
        )
    )
    def render_content(tab):
        if tab == TabNames.tab_1:
            return bar_chart_with_varying_bin_size()
            # return ''
        elif tab == TabNames.tab_2:
            return bar_chart_with_distributions()
        elif tab == TabNames.tab_3:
            return bar_chart_with_population_and_sample_data()

    return html.Div([
        dcc.Tabs(
            id=IDs.tab_input,
            value=TabNames.tab_1,
            children=[
                dcc.Tab(label='Tab One (bin size)', value=TabNames.tab_1),
                dcc.Tab(label='Tab Two (distributions)', value=TabNames.tab_2),
                dcc.Tab(label='Tab Three (central limit theorem)', value=TabNames.tab_3),

            ]),

        html.Div(id=IDs.tab_output),

    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H1('Welcome to Statistics with Python workshop!'),

    create_tabs_content(),

])

if __name__ == '__main__':
    app.run_server(debug=True)
