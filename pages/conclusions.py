
import dash_mantine_components as dmc
from dash import html
import dash


def layout():

    return dmc.Container([

        html.Img(src='https://media.istockphoto.com/id/500445793/photo/hand-writing-thank-you-on-chalkboard.jpg?s=612x612&w=0&k=20&c=OQbeo_sWVw0b7umUZYIzpNqhWJ8Dejur1dLAwBiqpeE=',
                 style={'height': '550px', 'width': '950px'}
                 )

    ])


dash.register_page(__name__)
