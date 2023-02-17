'''
# This app creates a simple sidebar layout using inline style arguments and the
# dbc.Nav component.
# dcc.Location is used to track the current location, and a callback uses the
# current location to render the appropriate page content. The active prop of
# each NavLink is set automatically according to the current pathname. To use
# this feature you must install dash-bootstrap-components >= 0.11.0.
# For more details on building multi-page Dash applications, check out the Dash
# documentation: https://dash.plot.ly/urls
# Source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
# @ Create Time: 2023-02-15 20:34:03.153109
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
'''
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, dcc, html
from pages.compare import compare
roboto_flex = "https://fonts.cdnfonts.com/css/roboto-flex"
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                title="youthbit_dashboard",
                external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      dbc.icons.BOOTSTRAP, roboto_flex],
                )
# app.config.supress_callback_exceptions=True
# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#897AD6",
    "color": "#FFFFFF",
    "boxShadow": "0px 0px 10px 0px black",
    "transition": "all 0.4s ease-in",
    "z-index": "2"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Img(className="pb-2 mb-4", src=dash.get_asset_url('logo.png'), style={
                 "borderBottom": "2px solid #B3E427"}, alt="YouthBit Logo", width=220, height=63),
        dbc.Nav(
            [
                dbc.NavLink([
                    html.I(className="bi bi-house-door-fill me-2"),
                    "Dashboard",
                ], href="/", active="exact"),
                dbc.NavLink([
                    html.I(className="bi bi-house-door-fill me-2"),
                    "Сравнение",
                ], href="/compare", active="exact"),
                dbc.NavLink([
                    html.I(className="bi bi-house-door-fill me-2"),
                    "Page 2",
                ], href="/page-2", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
    className="sidebar"
)
# russia_geoJSON = 'https://raw.githubusercontent.com/timurkanaz/Russia_geojson_OSM/master/GeoJson\'s/Countries/Russia_regions.geojson'


content = html.Div(id="page-content", style=CONTENT_STYLE,
                   className="page-content")

small_screens_button = html.Button(
    html.I(className="bi bi-list"), className="menu-button", n_clicks=0)


@app.callback(Output(sidebar, "className"), Input(small_screens_button, "n_clicks"))
def toggle_menu(clicks_amount):
    if clicks_amount % 2 != 0:
        return 'sidebar active'
    return 'sidebar'


app.layout = html.Div([dcc.Location(id="url"), sidebar,
                      content, small_screens_button])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [html.P("This is the content of the home page!"), dcc.Graph(
            id='life-exp-vs-gdp',
            figure=fig
        )]
    elif pathname == "/compare":
        return compare,
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
