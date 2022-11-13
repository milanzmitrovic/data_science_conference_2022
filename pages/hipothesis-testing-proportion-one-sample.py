from statsmodels.stats.proportion import proportions_ztest
import scipy.stats as st
import pandas as pd
import dash
import dash_mantine_components as dmc
from dash import html, dcc

# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
df = pd.read_csv('data/airline_passenger_satisfaction.csv')

sample_size = 100
significance = 0.95
null_hypothesis = 0.5
df_sample = df.sample(n=sample_size)

sample_success = df_sample.query("`Type of Travel` == 'Business'").__len__()

proportion_results = proportions_ztest(count=sample_success,
                                       nobs=sample_size,
                                       value=null_hypothesis,
                                       alternative='two-sided'
                                       )


def layout():
    return html.Div([
        dmc.Space(h=40),

        html.H2(f"{proportion_results}"),

        dmc.Space(h=40),

        dcc.Markdown("""

            ```python
                from statsmodels.stats.proportion import proportions_ztest
                import scipy.stats as st
                import pandas as pd
                
                # df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
                df = pd.read_csv('data/airline_passenger_satisfaction.csv')
                
                sample_size = 100
                significance = 0.95
                null_hypothesis = 0.5
                df_sample = df.sample(n=sample_size)
                
                sample_success = df_sample.query("`Type of Travel` == 'Business'").__len__()
                
                proportions_ztest(count=sample_success,
                                  nobs=sample_size,
                                  value=null_hypothesis,
                                  alternative='two-sided'
                                  )
            ```
        """)

    ])


dash.register_page(__name__)
