from dash import html, dcc, callback, Input, Output
from components.card import card
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

@callback(Output('bar-chart', 'figure'),Input('first', 'value'), Input('second', 'value'))
def display_output(first, second):
    if first == None or second == None: return go.Figure(data=[
go.Bar(name=f'Регион 1', y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h'),
go.Bar(name=f'Регион 2', y=["Признак 1", "Признак 2", 'Признак 3'], x=[12, 18, 29], orientation='h')
])
    print(f'Регион {first}')
    print(f'Регион {second}')
    fig = go.Figure(data=[
    go.Bar(name=f'Регион {first}', y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h'),
    go.Bar(name=f'Регион {second}', y=["Признак 1", "Признак 2", 'Признак 3'], x=[12, 18, 29], orientation='h')
])
    fig.update_layout(barmode='group')
    return fig


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
                id='first',
                style={"min-width": "200px"},
                placeholder="Регион 1"
            ),
            dcc.Dropdown(
                options=[
                    {'label': 'Регион 1', 'value': '1'},
                    {'label': 'Регион 2', 'value': '2'},
                    {'label': 'Регион 3', 'value': '3'}
                ],
                id='second',
                style={"min-width": "200px"},
                placeholder="Регион 2"
            )
        ],
            style={"display": "flex", "gap": "20px"}),
            html.Div([card(22,223,'Бюджет', True),
            card(223,150,'Волонтеры'),
            card(2222,13111,'СМИ расходы', True)], style={"display": "flex", "gap": "20px", "margin": "1rem 0" }),
            
            dcc.Graph(id='bar-chart')
    ]
)
