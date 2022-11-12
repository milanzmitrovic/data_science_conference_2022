
# Further information: https://www.statology.org/hypothesis-test-python/

import scipy.stats as st
import pandas as pd


# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
df = pd.read_csv('data/airline_passenger_satisfaction.csv')

sample_size = 300

df_sampled = df.sample(n=sample_size)


df_sampled[['Customer Type', 'Flight Distance']].groupby(by='Customer Type', as_index=False).agg(['mean', st.sem])

flight_distance__first_time_customers = df_sampled.query("`Customer Type` == 'First-time'")['Flight Distance']
flight_distance__returning_customers = df_sampled.query("`Customer Type` == 'Returning'")['Flight Distance']


st.ttest_ind(a=flight_distance__first_time_customers, b=flight_distance__returning_customers)


