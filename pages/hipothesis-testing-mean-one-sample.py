

import scipy.stats as st
import pandas as pd
import dash
from dash import html, dcc
import dash_mantine_components as dmc
from src.data_file import df


passenger_age = df['Age']

sample_size = 30
passenger_age_sample = passenger_age.sample(n=sample_size)

mean_age = passenger_age_sample.mean()
st_dev = passenger_age_sample.std()

st.sem(a=passenger_age_sample)

test_result = st.ttest_1samp(a=passenger_age_sample, popmean=42)


def layout():
    return html.Div([
        dmc.Space(h=40),

        html.H2(f"{test_result}"),

        dmc.Space(h=40),

        dcc.Markdown("""

            ```python

                import scipy.stats as st
                import pandas as pd
                
                
                # df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
                df = pd.read_csv('data/airline_passenger_satisfaction.csv')
                
                passenger_age = df['Age']
                
                sample_size = 30
                passenger_age_sample = passenger_age.sample(n=sample_size)
                
                mean_age = passenger_age_sample.mean()
                st_dev = passenger_age_sample.std()
                
                st.sem(a=passenger_age_sample)
                
                st.ttest_1samp(a=passenger_age_sample, popmean=42)

            ```
        """)

    ])


dash.register_page(__name__)


