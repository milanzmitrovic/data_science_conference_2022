
# Further information: https://sonalake.com/latest/hypothesis-testing-of-proportion-based-samples/
# Also https://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportions_ztest.html

from statsmodels.stats.proportion import proportions_ztest
import scipy.stats as st
import pandas as pd

# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
df = pd.read_csv('data/airline_passenger_satisfaction.csv')

sample_size = 100



