from dash import html, dcc, callback, Input, Output
import numpy as np
from components.card import card
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/dmitrykulakovfrontend/YouthBitDashboard/main/out.csv')


@callback(Output("charts", "style"),  Input("region", "value"), Input("type", "value"))
def toggle_menu(val1, val2):
    if val1 == None or val2 == None: return {"display": "none"}
    return {"display": "block", "position": "relative", "right": "50px"}

@callback(Output("cards", "children"),Output('histogram', "figure"),Output('histogram2', "figure"), Input("region", "value"), Input("type", "value"))
def display_region_info(region_name, type):
    default_fig = go.Figure(data=[
            go.Bar(name='test', y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h')
    ])
    default_fig2 = go.Figure(data=[
            go.Bar(name='test', y=["Признак 1", "Признак 2", 'Признак 3'], x=[20, 14, 23], orientation='h')
    ])
    if region_name == None or type == None: return '', default_fig, default_fig2

    filtered_df = df.loc[df['Регион'] == region_name]

    population_involvement = filtered_df['Уровень вовлеченности населения'].iloc[0]
    youth_involvement = filtered_df['Общее количество вовлеченной молодежи'].iloc[0]
    budget = filtered_df['Бюджет'].iloc[0]
    budget_per_person = filtered_df['Бюджет на человек'].iloc[0]
    
    x1 = filtered_df["Бюджет МиММ"].iloc[0]
    x2 = filtered_df['Бюджет ПВ'].iloc[0]
    x3 = filtered_df['Бюджет ВД'].iloc[0]
    x4 = filtered_df['Бюджет ПиП'].iloc[0]
    x5 = filtered_df['Бюджет других расходов'].iloc[0]

    y1 = filtered_df['Численность МиММ'].iloc[0]
    y2 = filtered_df['Численность ПВ'].iloc[0]
    y3 = filtered_df['Численность ВД'].iloc[0]
    y4 = filtered_df['Численность ПиП'].iloc[0]
    y5 = filtered_df['Численность других отделений'].iloc[0]

    color = "green" if population_involvement == "Высокий" else "red" if population_involvement == "Низкий" else "orange"

    fig = go.Figure(data=[
            go.Bar( y=['Бюджет Развития международного <br>и межрегионального молодeжного<br> сотрудничества', 'Бюджет Патриотического <br>воспитание молодeжи', 'Бюджет Волонтёрской<br>деятельности', 'Бюджет Содействия<br> в подготовке и переподготовке <br>специалистов', 'Бюджет других<br> отделений'], x=[x1,x2,x3,x4,x5], orientation='h')
    ])
    fig2 = go.Figure(data=[
            go.Bar( y=['Численность Развития<br> международного и межрегионального<br> молодeжного сотрудничества', 'Численность Патриотического <br>воспитание молодeжи', 'Численность Волонтёрской<br> деятельности', 'Численность Содействия<br> в подготовке и переподготовке<br> специалистов', 'Численность других<br> расходов'], x=[y1,y2,y3,y4,y5], orientation='h')
    ])
    fig.update_layout( bargap=0.30)
    fig2.update_layout( bargap=1)

    return [card(budget,budget_per_person,'Бюджет на человека','Бюджет', True),
            card(youth_involvement,population_involvement,'Уровень вовлеченности населения','Количество вовлеченной молодежи', color=color)], fig, fig2
print(df)


regions = html.Div(
    [
        html.H1('Информация о регионах',
                style={'color': "#897AD6"}),
        html.Label('Выберите регион и тип данных для подробной информации', style={"text-align": "left", "width": "100%", "font-weight": "bold", "margin": "1rem 0", "font-size": "1.5rem"}),
        html.Div([
            dcc.Dropdown(
                options=[
    {'label': '{}'.format(name), 'value': '{}'.format(name)} for name in df['Регион']
                ],
                id='region',
                style={"min-width": "300px"},
                placeholder="Выберите регион"
            ),
            dcc.Dropdown(
                options=[
    # {'label': '{}'.format(name), 'value': '{}'.format(name)} for name in df.columns[1:]
    "Основное"
                ],
                id='type',
                style={"min-width": "300px"},
                placeholder="Выберите данные"
            )
        ],
            style={"display": "flex", "gap": "20px", "justify-content": "flex-start"}),
            html.Div(id="cards", style={"display": "flex", "gap": "20px", "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "flex-start" }),
            html.Div([dcc.Graph(id="histogram",),
            dcc.Graph(id="histogram2",)], style={"display": "flex"}, id="charts")
            
    ]
)
