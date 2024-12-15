"""Entry point for the dash_project_name."""


from dash_project_name.layouts.homepage import homepage_layout
from dash_project_name.server import app

app.layout = homepage_layout

if __name__ == "__main__":
    app.run(debug=True)
