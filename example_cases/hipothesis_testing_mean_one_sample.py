
# Further information: https://www.statology.org/hypothesis-test-python/

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


if __name__ == '__main__':
    pass


