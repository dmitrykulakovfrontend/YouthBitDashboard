from dash import html, dcc, callback, Input, Output
from components.card import card
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

@callback(Output('bar-chart', 'children'),Input('first', 'value'), Input('second', 'value'))
def display_output(first, second):
    if len(first) == 0 or len(second) == 0: return ''
    print(f'Регион {first}')
    print(f'Регион {second}')
    fig = go.Figure(data=[
    go.Bar(name=f'Регион {first}', y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h'),
    go.Bar(name=f'Регион {second}', y=["Признак 1", "Признак 2", 'Признак 3'], x=[12, 18, 29], orientation='h')
])
    fig.update_layout(barmode='group')
    return dcc.Graph(id='bar-chart', figure=fig)

compare = html.Div(
    [
        html.H1('Сравнение регионов и округов',
                style={'color': "#897AD6"}),
        html.Label('Выберите 2 региона/округа для сравнения'),
        html.Div([
            dcc.Dropdown(
                options=[
                    {'label': 'Регион 1', 'value': '1'},
                    {'label': 'Регион 2', 'value': '2'},
                    {'label': 'Регион 3', 'value': '3'}
                ],
                value=[],
                id='first',
                style={"min-width": "200px"}
            ),
            dcc.Dropdown(
                options=[
                    {'label': 'Регион 1', 'value': '1'},
                    {'label': 'Регион 2', 'value': '2'},
                    {'label': 'Регион 3', 'value': '3'}
                ],
                value=[],
                id='second',
                style={"min-width": "200px"}
            )
        ],
            style={"display": "flex", "justify-content": "space-around"}),
            html.Div([card(22,223,'Бюджет', True),
            card(223,150,'Волонтеры'),
            card(2222,13111,'СМИ расходы', True)], style={"display": "flex", "gap": "20px", "margin": "1rem" }),
            
            html.Div(id='bar-chart')
    ]
)
