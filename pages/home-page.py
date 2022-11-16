
import dash
from dash import html
import dash_mantine_components as dmc


def layout():
    return dmc.Container([

        dmc.Space(h=60),

        dmc.SimpleGrid([

            html.Img(
                src='https://scontent.fbeg2-1.fna.fbcdn.net/v/t39.30808-6/275118980_3051200641862709_3706991297108316225_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=e3f864&_nc_ohc=0Gbhzj-KPGEAX-XS7r6&_nc_ht=scontent.fbeg2-1.fna&oh=00_AfD7G_HPA4eq6xln5gIiJizdXmmHim8Aq6Z8IlizjoTNzA&oe=6379CC12',
                style={'height': '450px', 'width': '1050px'}

            )
        ], cols=1),

        dmc.SimpleGrid([

            html.Img(
                src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png',
                style={'height': '450px', 'width': '1050px'}
            ),
        ], cols=1),

        dmc.SimpleGrid([
            html.Img(src='https://rapids.ai/assets/images/Plotly_Dash_logo.png',
                     style={'height': '450px', 'width': '650px'}
                     ),
        ], cols=1),

        dmc.SimpleGrid([

            html.Img(
                src='https://online.stat.psu.edu/statprogram/sites/statprogram/files/2018-08/statistics-review.jpg',
                style={'height': '450px', 'width': '1050px'}

            )
        ], cols=1),

        dmc.Space(h=20),

        html.H2('DataHangout meetup group from Belgrade:'),

        dmc.SimpleGrid([

            html.Img(
                src='assets/data_hangout.jpeg',
                style={'height': '450px', 'width': '800px'}

            )
        ], cols=1),

        dmc.Space(h=40),

        html.H1("""
        The views and opinions expressed in this workshop are those of the speakers and do not necessarily reflect the views or positions of any entity they represent.
        """),

        dmc.Space(h=60),

    ])


dash.register_page(__name__, path='/')

