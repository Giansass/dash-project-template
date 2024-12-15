"""Entry point for the dash_project_name."""

from dash import html

from dash_project_name.server import app

app.layout = [html.Div(children="Hello World")]

if __name__ == "__main__":
    app.run(debug=True)
