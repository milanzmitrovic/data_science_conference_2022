
import dash
from dash import html


def layout():
    return html.H2('Home page')


dash.register_page(__name__, path='/')

