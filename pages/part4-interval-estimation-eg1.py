

from dash import dcc, html
import dash_mantine_components as dmc
import scipy.stats as st
from src.data_file import df
import dash


flight_distance = df['Flight Distance']

n = 1000
flight_distance_sample_100 = flight_distance.sample(n=n)
x = flight_distance_sample_100.mean()
s = flight_distance_sample_100.std()
sem = st.sem(flight_distance_sample_100)
alpha = 0.05

interval_large_sample = st.norm.interval(
    alpha=alpha,
    loc=x,
    scale=sem
)


def layout():
    return dmc.Container([

        html.H2('Interval Estimation Example 1.'),
        html.Li(html.H3('Construct a 95% confidence interval for the average flight distance.')),
        html.Li(html.H3('Formula sutra ti saljem')),

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
            flight_distance_sample_100 = flight_distance.sample(n=n)
            x = flight_distance_sample_100.mean()
            s = flight_distance_sample_100.std()
            sem = st.sem(flight_distance_sample_20)
            alpha = 0.05


            interval_large_sample = st.norm.interval(
                alpha=alpha,
                loc=x,
                scale=sem
            )

        ```
        """
                     ),

        html.Li(html.H3(f"Confidence interval large sample: {interval_large_sample}")),
        html.Li(html.H3(
            'We are 95% confident that the average flight distance is between 820.6 and 1611.73 kilometers.'
        ))

    ])


dash.register_page(__name__)

