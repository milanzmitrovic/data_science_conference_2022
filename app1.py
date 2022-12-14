
from dash import Dash, html, dcc
import dash
from dash import Dash, Input, Output, dcc, html, callback
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

from src.navigation_drawer import nav_drawer


app = Dash(
    __name__,
    use_pages=True
)

app.layout = html.Div([
    html.H1('Introduction to Statistical Methods with Examples in Python!'),

    nav_drawer(),

    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)


