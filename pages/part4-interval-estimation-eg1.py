

from dash import dcc, html
import dash_mantine_components as dmc
import scipy.stats as st
from src.data_file import df
import dash


flight_distance = df['Flight Distance']

n = 100
flight_distance_sample = flight_distance.sample(n=n)
x = flight_distance_sample.mean()
s = flight_distance_sample.std()
sem = st.sem(flight_distance_sample)
alpha = 0.95

interval_large_sample = st.norm.interval(
    alpha=alpha,
    loc=x,
    scale=sem
)


def layout():
    return dmc.Container([

        html.H2('Interval Estimation Example 1.'),
        html.Li(html.H3('Construct a 95% confidence interval for the average flight distance.')),

        html.Img(src='assets/ie1.png', style={'height': '450px', 'width': '800px'}),

        dcc.Markdown("""

        ```python

            import scipy.stats as st
            import pandas as pd

            df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
            # df = pd.read_csv('data/airline_passenger_satisfaction.csv')

            flight_distance = df['Flight Distance']


            # Confidence Interval = x(+/-)t*(s/√n)
            # x: sample mean
            # t: t-value that corresponds to the confidence level
            # s: sample standard deviation
            # n: sample size

            # Case B - large sample (>30)
            n = 1000
            flight_distance_sample = flight_distance.sample(n=n)
            x = flight_distance_sample.mean()
            s = flight_distance_sample.std()
            sem = st.sem(flight_distance_sample)
            alpha = 0.05


            interval_large_sample = st.norm.interval(
                alpha=alpha,
                loc=x,
                scale=sem
            )

        ```
        """
                     ),

        html.Li(html.H3(f"Confidence interval large sample: {(1034.353, 1446.966)}")),
        html.Li(html.H3(
            'We are 95% confident that the average flight distance is between 1034.353 and 1446.966 kilometers.'
        ))

    ])


dash.register_page(__name__)

