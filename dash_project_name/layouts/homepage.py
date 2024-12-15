""" aaa """

from dash import dash_table, dcc, html

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
