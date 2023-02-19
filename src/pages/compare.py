from dash import html, dcc, callback, Input, Output
from components.card import card
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/dmitrykulakovfrontend/YouthBitDashboard/main/out.csv')


@callback(Output("regionsData", "style"),  Input('dropdown', 'value'))
def toggle_menu(val):
    if len(val) < 2:
        return {"display": "none"}
    return {"display": "flex"}


@callback(Output("regions_cards_budget", "children"), Output("regions_cards_involvement", "children"), Output('regionsData', 'children'), Input('dropdown', 'value'))
def display_info(regions):
    if len(regions) < 2:
        return [], [], []
    filtered_df = df.loc[df['Регион'].isin(regions)]
    population_involvement = filtered_df['Уровень вовлеченности населения']
    youth_involvement = filtered_df['Общее количество вовлеченной молодежи']
    budget = filtered_df['Бюджет']
    budget_per_person = filtered_df['Бюджет на человек']
    colors = ["green" if value == "Высокий" else "red" if value ==
              "Низкий" else "orange" for value in population_involvement]

    # y1 = filtered_df['Численность МиММ']
    # y2 = filtered_df['Численность ПВ']
    # y3 = filtered_df['Численность ВД']
    # y4 = filtered_df['Численность ПиП']
    # y5 = filtered_df['Численность других отделений']

    titles = ['Развитие международного <br>и межрегионального<br> молодeжного сотрудничества', 'Патриотическое <br>воспитание молодeжи',
              'Волонтёрская<br>деятельность', 'Содействие в подготовке<br> и переподготовке специалистов', 'Другие<br> отделения']
    # budget_values = [x1, x2, x3, x4, x5]
    # amount_values = [y1, y2, y3, y4, y5]

    # budget_objects = [{'value': val, 'title': title}
    #                   for val, title in zip(budget_values, titles)]
    # amount_objects = [{'value': val, 'title': title}
    #                   for val, title in zip(amount_values, titles)]

    # sorted_budget_objects = sorted(
    #     budget_objects, key=lambda obj: obj['value'])
    # sorted_amount_objects = sorted(
    #     amount_objects, key=lambda obj: obj['value'])

    # budget_values = [object["value"] for object in sorted_budget_objects]
    # amount_values = [object["value"] for object in sorted_amount_objects]

    # budget_titles = [object["title"] for object in sorted_budget_objects]
    # amount_titles = [object["title"] for object in sorted_amount_objects]

    # fig = go.Figure(data=[
    #     go.Bar(y=budget_titles, x=budget_values, orientation='h',
    #                 marker_color='#b3e427', name="В рублях", showlegend=True)
    # ])
    # fig2 = go.Figure(data=[
    #     go.Bar(y=amount_titles, x=amount_values, orientation='h',
    #            marker_color='#897AD6', name="Кол-во людей", showlegend=True)
    # ])
    # fig.update_traces(
    #     hoverlabel_font_color='white'
    # )
    # fig2.update_traces(
    #     hoverlabel_font_color='white'
    # )
    # fig.update_layout(legend={
    #     "title": '<b>Бюджет</b>',
    #     "font": {
    #         "family": 'Arial, sans-serif',
    #         "size": 14,
    #         "color": 'black'
    #     },
    #     "traceorder": 'normal',
    #     "y": 1,
    #     "x": 0.5,
    #     "orientation": "h",
    #     "yanchor": 'bottom',
    #     "xanchor": 'center',
    # }, margin=dict(l=0, r=0, t=50, b=0))
    # fig2.update_layout(legend={
    #     "title": '<b>Численность</b>',
    #     "font": {
    #         "family": 'Arial, sans-serif',
    #         "size": 14,
    #         "color": 'black'
    #     },
    #     "traceorder": 'normal',
    #     "y": 1,
    #     "x": 0.5,
    #     "orientation": "h",
    #     "yanchor": 'bottom',
    #     "xanchor": 'center',
    # }, margin=dict(l=0, r=0, t=50, b=0))
    budget_cards = [card(data['Бюджет'], data['Бюджет на человек'],
                         'Бюджет на человека', f'Бюджет {df.iloc[i]["Регион"]}', True) for i, data in filtered_df.iterrows()]
    involvement_cards = [card(data['Общее количество вовлеченной молодежи'], data['Уровень вовлеченности населения'],
                              'Уровень вовлеченности населения', f'Количество вовлеченной молодежи в {df.iloc[i]["Регион"]}', color=colors.pop(0)) for i, data in filtered_df.iterrows()]

    histogram_budget = go.Figure()
    for i, data in filtered_df.iterrows():
        x1 = data["Бюджет МиММ"]
        x2 = data['Бюджет ПВ']
        x3 = data['Бюджет ВД']
        x4 = data['Бюджет ПиП']
        x5 = data['Бюджет других расходов']
        budget_values = [x1, x2, x3, x4, x5]
        budget_objects = [{'value': val, 'title': title}
                          for val, title in zip(budget_values, titles)]
        sorted_budget_objects = sorted(
            budget_objects, key=lambda obj: obj['value'])
        budget_values = [object["value"] for object in sorted_budget_objects]
        budget_titles = [object["title"] for object in sorted_budget_objects]

        histogram_budget.add_trace(go.Bar(
            y=budget_titles,
            x=budget_values,
            orientation='h',
            name=data['Регион'],
            showlegend=True
        ))
        histogram_budget.update_layout(legend={
            "title": '<b>Бюджет</b>',
            "font": {
                "family": 'Arial, sans-serif',
                "size": 14,
                "color": 'black'
            },
            "traceorder": 'normal',
        }, margin=dict(l=0, r=0, t=50, b=0))

        histogram_amount = go.Figure()
    for i, data in filtered_df.iterrows():
        y1 = data['Численность МиММ']
        y2 = data['Численность ПВ']
        y3 = data['Численность ВД']
        y4 = data['Численность ПиП']
        y5 = data['Численность других отделений']
        amount_values = [y1, y2, y3, y4, y5]
        amount_objects = [{'value': val, 'title': title}
                          for val, title in zip(amount_values, titles)]
        sorted_amount_objects = sorted(
            amount_objects, key=lambda obj: obj['value'])
        amount_values = [object["value"] for object in sorted_amount_objects]
        amount_titles = [object["title"] for object in sorted_amount_objects]

        histogram_amount.add_trace(go.Bar(
            y=amount_titles,
            x=amount_values,
            orientation='h',
            name=data['Регион'],
            showlegend=True
        ))
        histogram_amount.update_layout(legend={
            "title": '<b>Численность</b>',
            "font": {
                "family": 'Arial, sans-serif',
                "size": 14,
                "color": 'black'
            },
            "traceorder": 'normal',
        }, margin=dict(l=0, r=0, t=50, b=0))

    return budget_cards, involvement_cards, [dcc.Graph("histogram_budget", figure=histogram_budget), dcc.Graph("histogram_amount", figure=histogram_amount)]
# [card(budget, budget_per_person, 'Бюджет на человека', 'Бюджет', True),
#             card(youth_involvement, population_involvement, 'Уровень вовлеченности населения', 'Количество вовлеченной молодежи', color=color)], []
    # [dcc.Graph(id="histogram", figure=fig),dcc.Graph(id="histogram2", figure=fig2)]


compare = html.Div(
    [
        html.H1('Сравнение регионов и округов',
                style={'color': "#897AD6"}),
        html.Label('Выберите регионы/округи для сравнения', style={
                   "text-align": "center", "width": "100%", "font-weight": "bold", "margin": "1rem 0", "font-size": "1.5rem"}),
        html.Div([
            dcc.Dropdown(
                options=[
                    {'label': '{}'.format(name), 'value': '{}'.format(name)} for name in df['Регион']
                ],
                value=[],
                id='dropdown',
                style={"min-width": "300px",
                       "padding": "1rem 0", "max-width": "500px"},
                placeholder="Выберите регионы",
                multi=True,
                maxHeight=300,
            )
        ],
            style={"display": "flex", "gap": "20px", "justify-content": "center"}),
        html.Div([], style={"display": "flex"}, id="regionsData"),
        html.Div([html.Div(id="regions_cards_budget", style={"display": "flex", "gap": "20px",
                                                             "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "flex-start", "flex-direction": "column"}),
                 html.Div(id="regions_cards_involvement", style={"display": "flex", "gap": "20px",
                                                                 "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "flex-start", "flex-direction": "column"})],
                 style={"display": "flex", "gap": "30px", "justify-content": "space-between", "padding": "0 1rem", })
    ]
)
