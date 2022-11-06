
import pandas as pd
from scipy import stats as st
import numpy as np
from statsmodels.stats.proportion import proportion_confint
from dataclasses import dataclass
import plotly.express as px
import plotly.io as pio


pio.renderers.default = 'browser'

df = pd.read_csv('data/airline_passenger_satisfaction.csv')




# 1.
# create 95% confidence interval for population mean weight

n = 25
x_bar = 70
sigma = 16

st.t.interval(alpha=0.95, df=25-1, loc=70, scale=sigma/np.sqrt(25))
# (63.39552460279033, 76.60447539720967)

# With confidence of 95% we claim that average time for delivery of all goods is
# between (63.39552460279033, 76.60447539720967).


# 2.

data = [25.8, 7.6, 8.2, 9.3, 10.9, 10.6, 4.9, 9.6, 7.0, 3.7, 13.7, 7.4, 9.8, 7.4, 10.4, 12.7, 4.6, 9.0, 9.9, 6.0]

mean = np.mean(data)
sigma = np.std(data)

st.t.interval(alpha=0.95, df=len(data)-1, loc=mean, scale=st.sem(data))
# (7.252470800171901, 11.5975291998281)


# 3.

number_of_trials = 240
count_of_success_cases = 96

proportion_confint(count=count_of_success_cases, nobs=number_of_trials, alpha=0.05, method='normal')
# (0.3380204967695439, 0.46197950323045617)


# 4.

# define data
data = [300, 315, 320, 311, 314, 309, 300, 308, 305, 303, 305, 301, 303]

# perform one sample t-test
st.ttest_1samp(a=data, popmean=310)
# Ttest_1sampResult(statistic=-1.5848116313861254, pvalue=0.1389944275158753)


#
st.uniform.rvs(size=1000, loc=10, scale=20)
st.norm.rvs(size=1000, loc=0, scale=1)
st.t.rvs(size=1000, loc=0, scale=1, df=99)
st.gamma.rvs(a=5, size=1000)
st.expon.rvs(scale=1, loc=0, size=1000)
st.poisson.rvs(mu=3, size=1000)
st.binom.rvs(n=10, p=0.8, size=1000)
st.bernoulli.rvs(size=1000, p=0.6)
st.lognorm.rvs(size=1000, loc=0, scale=1, s=22)
st.beta.rvs(size=1000, a=33, b=33)


distributions = {

    'Uniform': 'st.uniform.rvs(size=1000, loc=10, scale=20)',
    'Normal': 'st.norm.rvs(size=1000, loc=0, scale=1)',
    'T distribution': 'st.t.rvs(size=1000, loc=0, scale=1, df=99)',
    'Gamma': 'st.gamma.rvs(a=5, size=1000)',
    'Exponential': 'st.expon.rvs(scale=1, loc=0, size=1000)',
    'Poisson': 'st.poisson.rvs(mu=3, size=1000)',
    'Binomial': 'st.binom.rvs(n=10, p=0.8, size=1000)',
    'Bernoulli': 'st.bernoulli.rvs(size=1000, p=0.6)',
    'Lognormal': 'st.lognorm.rvs(size=1000, loc=0, scale=1, s=22)',
    'Beta': 'st.beta.rvs(size=1000, a=33, b=33)'

}

[{'label': k, 'value': v} for k, v in distributions.items()]


distributions['uniform']


# normal, uniform, binomial, poisson, t-distribution
# exponential, gamma, lognormal, beta, double exponential.



df.sample(n=3)['a'].mean()

for i in range(200):
    df.sample(n=30);



px.histogram([1,2,3,4,5,5,5,5]).show()



def create_histogram(
        df_: pd.DataFrame,
        numerical_column: str,
        number_of_bins: int = None,
        color_=None
):
    fig = px.histogram(
        data_frame=df_,
        color=color_,
        barmode='overlay',
        x=numerical_column,
        template='simple_white',
    )

    fig.update_traces(xbins=dict(
        size=number_of_bins
    ))

    return fig



df = pd.DataFrame({'a': [1,2,3,4,5,6,7]})


create_histogram(df_=df, numerical_column='a').show()



import plotly.graph_objects as go


