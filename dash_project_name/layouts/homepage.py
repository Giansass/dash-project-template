""" aaa """

import plotly.express as px
from dash import Input, Output, callback, dash_table, dcc, html

from dash_project_name.dao.csv_reader import sample_data_df

# Homepage layout
homepage_layout = [
    html.Div(children="My First App with Data, Graph, and Controls"),
    html.Hr(),
    dcc.RadioItems(
        options=["pop", "lifeExp", "gdpPercap"],
        value="lifeExp",
        id="controls-and-radio-item",
    ),
    dash_table.DataTable(data=sample_data_df.to_dict("records"), page_size=10),
    dcc.Graph(figure={}, id="controls-and-graph"),
]


# Add controls to build the interaction
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    """aaa"""
    fig = px.histogram(sample_data_df, x="continent", y=col_chosen, histfunc="avg")
    return fig
