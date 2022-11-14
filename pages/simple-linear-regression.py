
from src.data_file import df
import pandas as pd
from src.utils import Columns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.io as pio
import numpy as np
import statsmodels.api as sm
pio.renderers.default = 'browser'

df = df[[Columns.NumericalVariables.departure_delay, Columns.NumericalVariables.arrival_delay]].dropna()

df.corr()

df_sample = df.sample(n=10000)

X = df_sample[Columns.NumericalVariables.arrival_delay].values
y = df_sample[Columns.NumericalVariables.departure_delay].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

reg = LinearRegression()

X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)

X_test = X_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

reg.fit(X_train, y_train)

reg.predict(X_test)


px.scatter(x=X_test.flatten(), y=reg.predict(X_test).flatten()).show()

reg.coef_

reg.intercept_


# ------- # ------- # ------- # ------- #


lr = sm.OLS(y_train, X_train).fit()

print(lr.summary())

lr.summary()

y_train

len(y_train)

llr = sm.Logit(np.random.randint(0,2, 6700), X_train).fit()


llr.summary()


# ------- # ------- # ------- # ------- #


