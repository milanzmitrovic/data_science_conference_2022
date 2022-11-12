
# Further information https://www.geeksforgeeks.org/how-to-calculate-confidence-intervals-in-python/

import scipy.stats as st
import pandas as pd


# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
df = pd.read_csv('data/airline_passenger_satisfaction.csv')

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

st.norm.interval(
    alpha=0.95,
    loc=x,
    scale=sem
)


if __name__ == '__main__':
    pass

