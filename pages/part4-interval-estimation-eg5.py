
import dash
from dash import html, dcc
import dash_mantine_components as dmc
from statsmodels.stats.proportion import proportions_ztest
from src.data_file import df


sample_size = 100
significance = 0.05
null_hypothesis = 0.5
df_sample = df.sample(n=sample_size)

sample_success = df_sample.query("`Type of Travel` == 'Business'").__len__()

proportion_results = proportions_ztest(count=sample_success,
                                       nobs=sample_size,
                                       value=null_hypothesis,
                                       alternative='two-sided'
                                       )
print(proportion_results)

def layout():
    return dmc.Container([

        html.H2('Hypothesis Testing Example 2.'),
        html.Li(html.H3(
            'Is the proportion of passengers who travel on business different from 50% (significance level of the test is 5%)?')),
        html.Li(
            html.H3('Null hypothesis: The proportion of passengers who travel on business is not different from 50%')),
        html.Li(html.H3(
            'Alternative hypothesis: The proportion of passengers who travel on business is different from 50%')),

        html.Img(src='https://vitalflux.com/wp-content/uploads/2022/01/one-sample-proportion-z-test-640x433.jpg'),

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
    """),

        html.Li(html.H3(f"{proportion_results}")),

        html.Li(html.H3(
            'Because significance level of the test is less than the p-value, we reject the null hypothesis at this significance level. We conclude that the proportion of passengers who travel on business is different from 50%.')),

        dmc.Space(h=60)

    ])


dash.register_page(__name__)


