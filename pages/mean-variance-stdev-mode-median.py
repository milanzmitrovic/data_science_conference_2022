
import pandas as pd
from dataclasses import fields
from src.utils import Columns
from src.data_file import df
from dash import html, dcc
import dash_mantine_components as dmc
from dash import dash_table
import dash


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
    return html.Div([
        dmc.Space(h=40),
        create_sample_data_table(df_=dff_),

        dmc.Space(h=40),

        dcc.Markdown("""
        
            ```python
            
            import pandas as pd
            
            df = pd.read_csv('path_to_csv_file')

            numerical_columns = [field.default for field in fields(Columns.NumericalVariables)]

            numerical_columns.remove('ID')

            dff = df[numerical_columns]

            dff_ = dff.agg(func=['mean', 'std', 'median'])

            ```
        """)

        ])


dash.register_page(__name__)

