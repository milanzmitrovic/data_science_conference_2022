
import dash
from dash import html


def layout():
    return html.H2('Intro')


dash.register_page(__name__)

