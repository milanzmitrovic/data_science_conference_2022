from dataclasses import fields

import scipy.stats as st
import pandas as pd
import dash
import dash_mantine_components as dmc
from dash import html, dcc, dash_table
from src.data_file import df
from src.utils import Columns


numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

numerical_columns.remove('ID')

dff = df[numerical_columns]

dff_ = dff.agg(func=['mean', 'std', 'median'])

dff_.reset_index(inplace=True)

dff_ = dff_.round(decimals=3)


def create_sample_data_table(df_: pd.DataFrame):

    return dmc.Container(
        dash_table.DataTable(
            data=df_.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df_.columns],
            page_size=30
        ),
        style={'overflow-x': 'auto'}
    )


def layout():

    return dmc.Container([

        html.H1('Measures of Central Tendency and Dispersion'),

        html.H2('Measures of Central Tendency'),
        html.Li(html.H3('Mean')),
        html.Li(html.H3('Formula sutra ti saljem')),
        html.Li(html.H3('Median')),
        html.Li(html.H3('Mode')),
        html.Li(html.H3('Primer sutra ti saljem')),

        html.H2('Measures of Dispersion'),
        html.Li(html.H3('Why do we calculate measures of dispersion?')),
        html.Li(html.H3('Variance')),
        html.Li(html.H3('Formula sutra ti saljem')),
        html.Li(html.H3('Standard deviation')),
        html.Li(html.H3('Kodovi')),
        html.Li(html.H3('Rezultati')),
        html.Li(html.H3('Interpretacija sutra ti saljem')),

        html.H1('Part II - Measures of Central Tendency and Dispersion'),

        html.H2('Measures of Central Tendency'),
        html.Li(html.H3('Mean')),
        html.Li(html.H3('Formula sutra ti saljem')),
        html.Li(html.H3('Median')),
        html.Li(html.H3('Mode')),
        html.Li(html.H3('Primer sutra ti saljem')),

        html.H2('Measures of Dispersion'),
        html.Li(html.H3('Why do we calculate measures of dispersion?')),
        html.Li(html.H3('Variance')),
        html.Li(html.H3('Formula sutra ti saljem')),
        html.Li(html.H3('Standard deviation')),

        dcc.Markdown("""

        ```python

        import pandas as pd

        df = pd.read_csv('path_to_csv_file')

        numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

        numerical_columns.remove('ID')

        dff = df[numerical_columns]

        dff_ = dff.agg(func=['mean', 'std', 'median'])

        ```
            """),

        create_sample_data_table(df_=dff_),

        html.Li(html.H3('Interpretacija sutra ti saljem')),

        dmc.Space(h=40),

    ])


dash.register_page(__name__)




