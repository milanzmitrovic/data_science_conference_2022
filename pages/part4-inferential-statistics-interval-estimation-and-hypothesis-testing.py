import dash
import dash_mantine_components as dmc
from dash import html, dcc
from statsmodels.stats.proportion import proportion_confint, proportions_ztest

from src.data_file import df
import scipy.stats as st

import pandas as pd
import plotly.express as px
import dash
from scipy.stats import norm, t
import numpy as np
import plotly.io as pio
import scipy.stats as st
from dash import callback, Input, Output, dcc, html
import dash_mantine_components as dmc
pio.renderers.default = 'browser'


flight_distance = df['Flight Distance']

# Confidence Interval = x(+/-)t*(s/√n)
# x: sample mean
# t: t-value that corresponds to the confidence level
# s: sample standard deviation
# n: sample size


# # Case A - small sample (<30)
# n = 20
# flight_distance_sample_20 = flight_distance.sample(n=n)
# x = flight_distance_sample_20.mean()
# s = flight_distance_sample_20.std()
# n = 20
# sem = st.sem(flight_distance_sample_20)
#
# interval_small_sample = st.t.interval(alpha=0.95, df=n-1, loc=x, scale=sem)


# Case B - large sample (>30)
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

passenger_age = df['Age']

sample_size = 30
passenger_age_sample = passenger_age.sample(n=sample_size)

mean_age = passenger_age_sample.mean()
st_dev = passenger_age_sample.std()

st.sem(a=passenger_age_sample)

test_result = st.ttest_1samp(a=passenger_age_sample, popmean=42)


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
    return dmc.Container([

        html.H1('Inferential Statistics: Interval Estimation and Hypothesis Testing '),

        html.H2('Interval Estimation'),
        html.Li(html.H3('Why do we conduct interval estimation?')),
        html.Li(html.H3('Point estimate ')),
        html.Li(html.H3('Interval estimate')),
        html.Li(html.H3('Confidence level')),
        html.Li(html.H3('Formula sutra ti saljem')),








    ])




