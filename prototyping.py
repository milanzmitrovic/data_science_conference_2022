import plotly.io as pio
import plotly.express as px
import pandas as pd
from dataclasses import fields
from src.utils import Columns
from src.utils import create_histogram

pio.renderers.default = 'browser'

fields(Columns.CategoricalVariables)

categorical_columns = [field.default for field in fields(Columns.CategoricalVariables)]
numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

for x in [field.default for field in fields(Columns.CategoricalVariables)]:
    for y in [field.default for field in fields(Columns.NumericalVariables)]:
        print(x, ' - ', y)

df = pd.read_csv('data/airline_passenger_satisfaction.csv')

# Numerical variables
#       - Scatter plot
#       - Histogram
#           - Simple hist
#           - With color for category


# Categorical variables
#       - Bar chart for count


for i in numerical_columns:
    create_histogram(
        df_=df,
        numerical_column=i
    ).show()








