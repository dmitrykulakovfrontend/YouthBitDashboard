# package imports
import dash
from dash import html, dcc, callback, Input, Output
# -*- coding: utf-8 -*-
import dash
from dash import Input, Output, dcc, html


def card(value, value2, name,  dollar=False):
    percentage_difference = ((value - value2) / value2) * 100
    if percentage_difference >= 0:
        percentage_difference = "+" + "{:.2f}".format(percentage_difference) + "%"
    else:
        percentage_difference = "{:.2f}".format(percentage_difference) + "%"
    print()
    return html.Div([
        html.Span(name, style={"color": "#809FB8"}),
        html.Div([
            html.Span("{:.2f}".format(value) + " $" if dollar == True else value, style={
                      "font-size": "1.5rem", "font-weight": "bold", }),
            html.Span("{:.2f}".format(value2) + " $" if dollar == True else value2, style={"font-size": "1.5rem",
                      "font-weight": "bold", "color": "#A1A7B1"}),
        ], style={"display": "flex", "gap": "20px", }),
        html.P(
[html.Span(percentage_difference, style={"color": "#34B53A" if value > value2 else "#FF3A29", "font-size": "1.5rem", "font-weight": "500"}), " Относительно сравниваемого"], style={"margin": "0", "display": "flex", "flex-direction": "column" })

    ], style={"border": "1px solid #E0E0E0", "padding": "0.5rem", "width": "fit-content", "min-width": "240px", "border-radius": "16px", })
