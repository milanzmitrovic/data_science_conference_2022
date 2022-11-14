
import dash_mantine_components as dmc
from dash import html, dcc
from statsmodels.stats.proportion import proportion_confint
from src.data_file import df
import dash


df_sample = df.sample(n=100)

passenders_class = df_sample[['Type of Travel']]

count_of_business_class_passengers = passenders_class.query("`Type of Travel` == 'Business'").count()
total_passengers = len(df_sample)
proportion_of_business_class_passengers = count_of_business_class_passengers / total_passengers

proportion_confidence_interval = proportion_confint(count=count_of_business_class_passengers,
                                                    nobs=total_passengers,
                                                    alpha=0.05,
                                                    method='normal'
                                                    )


def layout():

    return dmc.Container([

        html.H2('Interval Estimation Example 2.'),
        html.Li
        (html.H3('Construct a 95% confidence interval for the proportion of passengers who used business class.')),
        html.Li(html.H3('Formula sutra ti saljem')),

        dcc.Markdown("""

        ```python

            import pandas as pd
            from statsmodels.stats.proportion import proportion_confint            

            df = pd.read_csv('data/airline_passenger_satisfaction.csv')

            df_sample = df.sample(n=100)

            passenders_class = df_sample[['Type of Travel']]

            count_of_business_class_passengers = passenders_class.query("`Type of Travel` == 'Business'").count()
            total_passengers = len(df_sample)
            proportion_of_business_class_passengers = count_of_business_class_passengers / total_passengers


            proportion_confint(count=count_of_business_class_passengers,
                               nobs=total_passengers,
                               alpha=0.05,
                               method='normal'
                               )

        ```
        """
                     ),

        html.Li(html.H3(f"{proportion_confidence_interval}")),
        html.Li(html.H3(
            'We are 95% confident that the proportion of passengers who used business class is between 0.632 and 0.808.'
        )),

    ])


dash.register_page(__name__)

