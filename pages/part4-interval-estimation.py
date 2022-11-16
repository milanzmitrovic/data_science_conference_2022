
from dash import dcc, html
import dash_mantine_components as dmc
import dash
from statsmodels.stats.proportion import proportion_confint
import scipy.stats as st
from example_cases.confidence_interval_mean import flight_distance
from src.data_file import df


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

        html.H1('Inferential Statistics: Interval Estimation and Hypothesis Testing '),

        dmc.Space(h=10),

        html.H2('Interval Estimation'),
        html.Li(html.H3('Why do we conduct interval estimation?')),
        html.Li(html.H3('Point estimate ')),
        html.Li(html.H3('Interval estimate')),
        html.Li(html.H3('Confidence level - (Point estimate +/- Margin of error)')),

        ])


dash.register_page(__name__)


