import dash_mantine_components as dmc
from dash import html, Output, Input, callback, dcc
import dash


def nav_drawer():
    return html.Div(
        [
            dmc.Button("Open Drawer", id="drawer-demo-button"),
            dmc.Drawer(
                title="Drawer Example",
                id="drawer",
                padding="md",
                children=[
                    html.Div([
                        dcc.Link(
                            f"{page['name']} - {page['path']}", href=page["relative_path"]
                        ),
                        dmc.Space(h=20)
                        ]
                    )
                    for page in dash.page_registry.values()
                ]
            ),

        ]
    )


@callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
