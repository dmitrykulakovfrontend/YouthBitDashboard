from dash import html
import dash_bootstrap_components as dbc
import uuid

colors = {
    "red": "#FF3A29",
    "green": "#34B53A",
    "orange": "#F2994A"
}


def card(value, secondaryValue, secondaryName, name, money=False, color="green"):
    id = str(uuid.uuid4())
    color = colors[color]
    return html.Div([
        html.Span(name, style={"color": "#809FB8"}),
        html.Div([
            html.Span(
                children=('{:,.2f} ₽'.format(value) if money == True else value), style={"font-size": "1.5rem", "font-weight": "500"})
        ], style={"display": "flex", "gap": "20px"}),
        html.P(
            [html.Span('{:,.2f} ₽'.format(secondaryValue) if money == True and not isinstance(secondaryValue, str) else secondaryValue, style={"color": color, "font-size": "1rem", "font-weight": "500"}), secondaryName], style={"margin": "0", "display": "flex", "flex-direction": "column"}),
        dbc.Tooltip(
            [html.P("Список действий для улучшения ситуации:"), html.P(
                "1. Действие 1"), html.P(
                "2. Действие 2")],
            target=id,
            placement="right",
            style={"backgroundColor": "red !important"}
        )

    ], id=id, style={"border": "1px solid #E0E0E0", "padding": "0.5rem", "width": "fit-content", "min-width": "240px", "border-radius": "16px", })
