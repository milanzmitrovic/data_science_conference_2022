
import dash
from dash import dcc, html
import dash_mantine_components as dmc
import pandas as pd
from statsmodels.stats.proportion import proportion_confint

from src.data_file import df


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

        html.H2(f"Confidence interval for proportion: {round(proportion_confidence_interval[0][0],3)} - {round(proportion_confidence_interval[1][0],3)}"),


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
        """)

    ])


dash.register_page(__name__)


