
from statsmodels.stats.proportion import proportion_confint
import pandas as pd


# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
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


if __name__ == '__main__':
    pass


