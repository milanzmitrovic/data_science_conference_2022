
import dash
from dash import html


def layout():
    return html.H2('About us')


dash.register_page(__name__)
