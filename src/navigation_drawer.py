import dash_mantine_components as dmc
from dash import html, Output, Input, callback, dcc
import dash


def create_content():
    return [
        html.Hr(),

        dcc.Link('Home Page', href='/'),
        dmc.Space(h=20),
        dcc.Link('About Us', href='/about-us'),
        dmc.Space(h=20),

        html.H3('Part I - Intro to Statistics'),
        dcc.Link('Intro to Statistics',
                 href='/part1-intro-to-statistics'),
        dmc.Space(h=20),

        html.H3('Part II - Measures of Central Tendency and Dispersion'),
        html.Li(dcc.Link('Show Dataset Sample', href='/data-sample')),
        html.Li(dcc.Link('Exploratory Data Analysis', href='/exploratory-data-analysis')),
        html.Li(dcc.Link('Categorical Variables', href='/categorical-variables-bar-charts')),

        html.Li(dcc.Link('Intro to statistical metrics',
                         href='/part2-measure-of-central-tendency-and-dispersion')),
        dmc.Space(h=20),

        html.H3('Part III – Various Distributions and Central Limit Theorem '),
        html.Li(dcc.Link('Bin Sizes', href='/bin-sizes')),
        html.Li(dcc.Link('Interactive Distributions', href='/interactive-distributions')),
        html.Li(dcc.Link('Distributions', href='/distributions')),
        html.Li(dcc.Link('Central Limit Theorem', href='/central-limit-theorem')),
        dmc.Space(h=20),

        html.H3('Part IV - Inferential Statistics: Interval Estimation and Hypothesis Testing'),
        html.Li(dcc.Link('Interval estimation', href='/part4-interval-estimation')),
        html.Li(dcc.Link('Interval estimation eg. 1', href='/part4-interval-estimation-eg1')),
        html.Li(dcc.Link('Interval Estimation eg. 2.', href='/part4-interval-estimation-eg2')),
        html.Li(dcc.Link('Width of a confidence interval', href='/part4-interval-estimation-eg3')),
        html.Li(dcc.Link('Hypothesis Testing', href='/part4-hipothesys-testing')),
        html.Li(dcc.Link('Hypothesis Testing eg 1.', href='/part4-interval-estimation-eg4')),
        html.Li(dcc.Link('Hypothesis Testing eg 2.', href='/part4-interval-estimation-eg5')),

        dmc.Space(h=20),
        dcc.Link('Conclusions', href='/conclusions'),
        dmc.Space(h=20),
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

        ], style={'overflow-y': 'scroll'}
    )


@callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
