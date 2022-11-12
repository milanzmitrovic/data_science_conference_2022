import dash_mantine_components as dmc
from dash import html, Output, Input, callback, dcc
import dash


def create_content():

    return [
        html.Hr(),
        html.Br(),
        html.Br(),
        dcc.Link('Home Page', href='/home-page'),
        dmc.Space(h=20),
        dcc.Link('About Us', href='/about_us'),
        dmc.Space(h=20),
        dcc.Link('Intro', href='/intro'),
        dmc.Space(h=20),
        dcc.Link('Exploratory Data Analysis', href='/exploratory-data-analysis'),
        dmc.Space(h=20),
        dcc.Link('Show Dataset Sample', href='/data-sample'),
        dmc.Space(h=20),
        dcc.Link('Categorical Variables', href='/categorical-variables-bar-charts'),
        dmc.Space(h=20),
        dcc.Link('Interactive Distributions', href='/interactive-distributions'),
        dmc.Space(h=20),
        dcc.Link('Central Limit Theorem', href='/central-limit-theorem'),
        dmc.Space(h=20),
        dcc.Link('Bin Sizes', href='/bin-sizes'),
        dmc.Space(h=20),
        dcc.Link('Distributions', href='/distributions'),
        dmc.Space(h=20),
        dcc.Link('Conclusions', href='/conclusions'),
        dmc.Space(h=20)
    ]


def nav_drawer():
    return html.Div(
        [
            dmc.Button("Table of Content", id="drawer-demo-button"),
            dmc.Drawer(
                title="Table of Content",
                id="drawer",
                padding="md",
                children=create_content()
            ),

        ]
    )


@callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
