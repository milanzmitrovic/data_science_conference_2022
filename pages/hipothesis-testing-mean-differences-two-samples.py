
import scipy.stats as st
import pandas as pd
import dash
from dash import html, dcc
import dash_mantine_components as dmc
from src.data_file import df


sample_size = 300

df_sampled = df.sample(n=sample_size)

df_sampled[['Customer Type', 'Flight Distance']].groupby(by='Customer Type', as_index=False).agg(['mean', st.sem])

flight_distance__first_time_customers = df_sampled.query("`Customer Type` == 'First-time'")['Flight Distance']
flight_distance__returning_customers = df_sampled.query("`Customer Type` == 'Returning'")['Flight Distance']


test_result = st.ttest_ind(a=flight_distance__first_time_customers, b=flight_distance__returning_customers)


def layout():
    return html.Div([
        dmc.Space(h=40),

        html.H2(f"{test_result}"),

        dmc.Space(h=40),

        dcc.Markdown("""

            ```python

                import scipy.stats as st
                import pandas as pd
                
                
                df = pd.read_csv('data/airline_passenger_satisfaction.csv')
                
                sample_size = 300
                
                df_sampled = df.sample(n=sample_size)
                
                
                df_sampled[['Customer Type', 'Flight Distance']].groupby(by='Customer Type', as_index=False).agg(['mean', st.sem])
                
                flight_distance__first_time_customers = df_sampled.query("`Customer Type` == 'First-time'")['Flight Distance']
                flight_distance__returning_customers = df_sampled.query("`Customer Type` == 'Returning'")['Flight Distance']
                
                
                st.ttest_ind(a=flight_distance__first_time_customers, b=flight_distance__returning_customers)



            ```
        """)

    ])


dash.register_page(__name__)


