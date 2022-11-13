
import dash
from dash import html, dcc
import dash_mantine_components as dmc


def layout():
    return dmc.Container([

        html.H1('Part I - Intro to Statistics'),

        html.H1('Part II - Intro to Airline Passengers Dataset'),

        html.H2(),

        html.H2('Overview'),

        dcc.Markdown('''
        
        

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
        
        
        # Case A - small sample (<30)
        n = 20
        flight_distance_sample_20 = flight_distance.sample(n=n)
        x = flight_distance_sample_20.mean()
        s = flight_distance_sample_20.std()
        n = 20
        sem = st.sem(flight_distance_sample_20)
        
        st.t.interval(alpha=0.95, df=n-1, loc=x, scale=sem)
        
        
        # Case B - large sample (>30)
        n = 1000
        flight_distance_sample_100 = flight_distance.sample(n=n)
        x = flight_distance_sample_100.mean()
        s = flight_distance_sample_100.std()
        sem = st.sem(flight_distance_sample_20)
        level_of_significance = 0.95
        
        
        interval = st.norm.interval(
            alpha=level_of_significance,
            loc=x,
            scale=sem
        )
        
        
        if __name__ == '__main__':
            print(f"Confidence interval {interval}")

       ```'''),

        dmc.Space(h=40)

        ])


dash.register_page(__name__)

