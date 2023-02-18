from dash import html, dcc, callback, Input, Output
from components.card import card
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

@callback(Output('bar-chart', 'figure'),Input('dropdown', 'value'))
def display_output(values):
    if len(values) < 2: return go.Figure(data=[
go.Bar(name=f'Регион 1', y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h'),
go.Bar(name=f'Регион 2', y=["Признак 1", "Признак 2", 'Признак 3'], x=[12, 18, 29], orientation='h')
])
    data = [
        go.Bar(name='Регион {}'.format(name), y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h') for name in values
]
    fig = go.Figure(data=data)
    
    fig.update_layout(barmode='group')
    return fig


compare = html.Div(
    [
        html.H1('Сравнение регионов и округов',
                style={'color': "#897AD6"}),
        html.Label('Выберите регионы/округи для сравнения', style={"text-align": "center", "width": "100%", "font-weight": "bold", "margin": "1rem 0", "font-size": "1.5rem"}),
        html.Div([
            dcc.Dropdown(
                options=[
                    {'label': 'Регион 1', 'value': '1'},
                    {'label': 'Регион 2', 'value': '2'},
                    {'label': 'Регион 3', 'value': '3'},
                    {'label': 'Регион 4', 'value': '4'},
                    {'label': 'Регион 5', 'value': '5'}
                ],
                value=[],
                id='dropdown',
                style={"min-width": "200px", "font-weight": "bold", "padding": "1rem 0", "max-width": "400px"},
                placeholder="Выберите регионы",
                multi=True,
                maxHeight=300,
            )
        ],
            style={"display": "flex", "gap": "20px", "justify-content": "center"}),
            # html.Div([card(22,223,'Бюджет', True),
            # card(223,150,'Волонтеры'),
            # card(2222,13111,'СМИ расходы', True)], style={"display": "flex", "gap": "20px", "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "center" }),
            
            dcc.Graph(id='bar-chart')
    ]
)
