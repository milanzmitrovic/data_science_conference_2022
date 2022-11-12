
# Further information: https://sonalake.com/latest/hypothesis-testing-of-proportion-based-samples/
# Also https://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportions_ztest.html

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


if __name__ == '__main__':
    pass


