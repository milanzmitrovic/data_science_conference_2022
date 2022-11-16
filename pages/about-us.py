import dash
from dash import html
import dash_mantine_components as dmc


def layout():
    return dmc.Container([

        html.H2('About instructors', style={'textAlign': 'center'}),
        dmc.Space(h=40),

        dmc.SimpleGrid([

            html.Div([
                html.P("""

                    Ivana Ivković graduated from the Faculty of Economics, University of Belgrade (study program Statistics). 
                    She completed a master studies at the Faculty of Economics, University of Belgrade (study program Econometrics), defending master thesis titled "Application of log-linear and logit models in the analysis of contingency tables". 
                    
                    """),
                html.P("""
                    At the same Faculty, she completed a doctoral studies (study program Statistics), defending doctoral dissertation titled "Non-parametric statistical techniques for estimation of regression coefficients and coefficient of variation in corporate finance". 
                    Ivana Ivković has been an assistant professor at the Faculty of Economics and Business, University of Belgrade (course Introduction to Statistics) since June 2022. 


                    """),

            ]),

            html.Img(src='../assets/ivana.jpg')

        ], cols=2),

        dmc.Space(h=40),
        html.Hr(),
        dmc.Space(h=40),

        dmc.SimpleGrid([

            html.Img(src='../assets/milan.jpg', style={'height': '450px', 'width': '450px'}),

            html.Div([
                html.P("""

                Besides skiing, riding bicycles, wild nature, trams and trains, two of my biggest passions are programming and teaching. When I write programs and show others what I made, I put myself into happy child mode. Beside that, I enjoy long walks and like to play with animals outside.
            
            
                """),

                html.P(

                    """
            
                Although I am economist by vocation, I find fun in writing programs and see computer science as really impactful discipline. 
                The world needs more computer scientists who understand economics, and more business leaders who understand principles of scientific computing. 
                Understanding ways how businesses operate and ways how economy works, makes me ready to help organisations strengthen their impact in todays world.
            
            
                """
                ),

            ])

        ], cols=2),

        dmc.Space(h=40),

    ])


dash.register_page(__name__)
