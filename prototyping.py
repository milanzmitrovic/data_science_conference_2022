from dataclasses import fields
from src.data_file import df
from src.utils import Columns
import pandas as pd

categorical_columns = [field.default for field in fields(Columns.CategoricalVariables)]

categorical_columns

neutral_or_dissatisfied = 'Neutral or Dissatisfied'
satisfied = 'Satisfied'

df.iloc[1]['Satisfaction']


def satisfied_(row_series: pd.Series):
    if row_series['Satisfaction'] == satisfied:
        return 1


def dis_satisfied_(row_series: pd.Series):
    if row_series['Satisfaction'] != satisfied:
        return 1


df['satisfied'] = df.apply(func=satisfied_, axis=1)
df['dis_satisfied'] = df.apply(func=dis_satisfied_, axis=1)


categorical_columns.remove('Satisfaction')

dff = df[categorical_columns + ['satisfied', 'dis_satisfied']]


interesting_df = dff[[
    Columns.CategoricalVariables.baggage_handling,
    Columns.CategoricalVariables.check_in_service,
    Columns.CategoricalVariables.cleanliness,
    Columns.CategoricalVariables.departure_and_arrival_time_convenience,
    Columns.CategoricalVariables.ease_of_online_booking,
    Columns.CategoricalVariables.food_and_drink,
    'satisfied',
    'dis_satisfied'
]].groupby(
    by=[Columns.CategoricalVariables.baggage_handling,
        Columns.CategoricalVariables.check_in_service,
        Columns.CategoricalVariables.cleanliness,
        Columns.CategoricalVariables.departure_and_arrival_time_convenience,
        Columns.CategoricalVariables.ease_of_online_booking,
        Columns.CategoricalVariables.food_and_drink
        ],
    as_index=False
).sum()


interesting_df['satisfied'] / interesting_df['dis_satisfied']


import pandas as pd

pd.read_table('data/rrr.tsv')
