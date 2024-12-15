""" aaa """

# Import packages
import plotly.express as px
from dash import Input, Output, callback

from dash_project_name.dao.csv_reader import sample_data_df


# Add controls to build the interaction
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(col_chosen):
    """aaa"""
    fig = px.histogram(sample_data_df, x="continent", y=col_chosen, histfunc="avg")
    return fig
