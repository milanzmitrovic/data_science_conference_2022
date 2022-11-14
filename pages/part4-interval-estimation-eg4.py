
import dash
import dash_mantine_components as dmc
from dash import dcc, html
import scipy.stats as st
from src.data_file import df


passenger_age = df['Age']

sample_size = 30
passenger_age_sample = passenger_age.sample(n=sample_size)

mean_age = passenger_age_sample.mean()
st_dev = passenger_age_sample.std()

st.sem(a=passenger_age_sample)

test_result = st.ttest_1samp(a=passenger_age_sample, popmean=42)


def layout():

    return dmc.Container([

        html.H2('Hypothesis Testing Example 1.'),
        html.Li(html.H3(
            'Is the average age of passengers different from 42 years (significance level of the test is 5%)?')),
        html.Li(html.H3('Null hypothesis: The average age of passengers is not different from 42 years.')),
        html.Li(html.H3('Alternative hypothesis: The average age of passengers is different from 42 years.')),
        html.Li(html.H3('Formula sutra ti saljem')),
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
    """),
        html.Li(html.H3(f"{test_result}")),
        html.Li(html.H3(
            'Interpratacija: Because significance level of the test is greater than the p-value, we reject the null hypothesis at this significance level. We conclude that the average age of passengers is different from 42 years.')),

    ])


dash.register_page(__name__)

