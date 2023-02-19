from dash import html, dcc, callback, Input, Output
import numpy as np
from components.card import card
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

df = pd.read_csv('https://raw.githubusercontent.com/dmitrykulakovfrontend/YouthBitDashboard/main/out.csv')
df_massmedia = pd.read_csv('https://raw.githubusercontent.com/dmitrykulakovfrontend/YouthBitDashboard/main/main.csv')


@callback(Output("charts", "style"),  Input("region", "value"), Input("type", "value"))
def toggle_menu(val1, val2):
    if val1 == None or val2 == None: return {"display": "none"}
    return {"display": "flex", "position": "relative", "right": "25px"}



@callback(Output("cards", "children"),Output('charts', "children"), Output("cards", "style"), Input("region", "value"), Input("type", "value"))
def display_region_info(region_name, type):
    if region_name == None or type == None: return '','',{}
    if type == "СМИ":
      filtered_df = df_massmedia.loc[df['Регион'] == region_name]

      financings = filtered_df["Финансирование"].iloc[0]
      financings_percentage = filtered_df["Финансирование, тенденция"].iloc[0]

      visitors = filtered_df["Кол-во просмотров сайта"].iloc[0]
      visitors_percentage = filtered_df["Кол-во просмотров сайта, тенденция"].iloc[0]

      subscribers = filtered_df["Число подписчиков сообщества"].iloc[0]
      subscribers_percentage = filtered_df["Число подписчиков сообщества, тенденция"].iloc[0]

      financings_card = card(financings,financings_percentage,'Финансирование, тенденция','Финансирование', True)
      visitors_card = card(visitors,visitors_percentage,"Кол-во просмотров сайта, тенденция","Кол-во просмотров сайта")
      subscribers_card = card(subscribers,subscribers_percentage,"Число подписчиков сообщества, тенденция","Число подписчиков сообщества")
      x1 = filtered_df["В ТВ-сюжетах"].iloc[0]
      x2 = filtered_df['В интернет-СМИ'].iloc[0]
      x3 = filtered_df['В печатных СМИ'].iloc[0]

      y1 = filtered_df['Кол-во новостей'].iloc[0]
      y2 = filtered_df['Кол-во публикаций в соц. сетях'].iloc[0]
      y3 = filtered_df['Кол-во печатных статей'].iloc[0]
      y4 = filtered_df['Кол-во электронных статей'].iloc[0]

      titles_mentions = ["В ТВ-сюжетах", 'В интернет-СМИ', 'В печатных СМИ']
      titles_publications = ["Кол-во новостей", 'Кол-во публикаций <br>в соц. сетях', 'Кол-во печатных<br> статей','Кол-во электронных<br> статей']

      mentions_values = [x1, x2, x3]
      publications_values = [y1, y2, y3, y4]

      mentions_objects = [{'value': val, 'title': title} for val, title in zip(mentions_values, titles_mentions)]
      publications_objects = [{'value': val, 'title': title} for val, title in zip(publications_values, titles_publications)]

      sorted_mentions_objects = sorted(mentions_objects, key=lambda obj: obj['value'])
      sorted_publications_objects = sorted(publications_objects, key=lambda obj: obj['value'])

      mentions_values = [object["value"] for object in sorted_mentions_objects]
      publications_values = [object["value"] for object in sorted_publications_objects]

      mentions_titles = [object["title"] for object in sorted_mentions_objects]
      publications_titles = [object["title"] for object in sorted_publications_objects]

      
      unique_visitors = filtered_df['Число уникальных пользователей сайта'].iloc[0]
      population = filtered_df['Население'].iloc[0]

      fig = go.Figure(data=[
              go.Bar( y=mentions_titles, x=mentions_values, orientation='h',
      marker_color='#b3e427', name="", showlegend=True)
      ])
      fig2 = go.Figure(data=[
              go.Bar( y=publications_titles, x=publications_values, orientation='h',
      marker_color='#897AD6', name="", showlegend=True )
      ])
      pie = go.Figure(data=[go.Pie(labels=['Число уникальных пользователей сайта','Население'], values=[unique_visitors, population],
    domain={'x': [0.7, 0], 'y': [1, 0]}),])
      fig.update_traces(
      hoverlabel_font_color='white'
  )
      fig2.update_traces(
      hoverlabel_font_color='white'
  )
      pie.update_traces(
      hoverlabel_font_color='white',
      hoverinfo='label+percent',
                  marker=dict(colors=['#b3e427', '#897AD6'])
  )
      pie.update_layout(legend={
          "title":'<b>Процент вовлеченности:</b>',
          "font":{
              "family":'Arial, sans-serif',
              "size":14,
              "color":'black'
          },
          "traceorder":'normal',
        'y': 1,
        'x': 0,
        'yanchor': 'middle',
        'xanchor': 'right',
      }, margin=dict(l=0, r=0, t=50, b=0),width=500,height=300)
      fig.update_layout(legend={
          "title":'<b>Количество упоминаний молодежной организации</b>',
          "font":{
              "family":'Arial, sans-serif',
              "size":14,
              "color":'black'
          },
          "traceorder":'normal',
          "y": 1,
          "x": 0.5,
          "orientation": "h",
          "yanchor":'bottom',
          "xanchor":'center',
      }, margin=dict(l=0, r=0, t=50, b=0),width=500,height=300)
      fig2.update_layout(legend={
          "title":'<b>Количество публикаций:</b>',
          "font":{
              "family":'Arial, sans-serif',
              "size":14,
              "color":'black'
          },
          "traceorder":'normal',
          "y": 1,
          "x": 0.5,
          "orientation": "h",
          "yanchor":'bottom',
          "xanchor":'center',
      },margin=dict(l=0, r=0, t=50, b=0),width=500,height=300)
      
      return [financings_card,visitors_card,subscribers_card], [dcc.Graph(id="histogram",figure=fig),dcc.Graph(id="histogram2", figure=fig2),dcc.Graph(id="pie", figure=pie)],{"display": "flex", "gap": "20px", "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "space-between" }
      # [dcc.Graph(id="histogram",figure=fig),
      #         dcc.Graph(id="histogram2", figure=fig2)]
    elif type == "Основное":

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

      titles = ['Развитие международного <br>и межрегионального<br> молодeжного сотрудничества', 'Патриотическое <br>воспитание молодeжи', 'Волонтёрская<br>деятельность', 'Содействие в подготовке<br> и переподготовке специалистов', 'Другие<br> отделения']
      budget_values = [x1, x2, x3, x4, x5]
      amount_values = [y1, y2, y3, y4, y5]

      budget_objects = [{'value': val, 'title': title} for val, title in zip(budget_values, titles)]
      amount_objects = [{'value': val, 'title': title} for val, title in zip(amount_values, titles)]

      sorted_budget_objects = sorted(budget_objects, key=lambda obj: obj['value'])
      sorted_amount_objects = sorted(amount_objects, key=lambda obj: obj['value'])

      budget_values = [object["value"] for object in sorted_budget_objects]
      amount_values = [object["value"] for object in sorted_amount_objects]

      budget_titles = [object["title"] for object in sorted_budget_objects]
      amount_titles = [object["title"] for object in sorted_amount_objects]

      color = "green" if population_involvement == "Высокий" else "red" if population_involvement == "Низкий" else "orange"

      fig = go.Figure(data=[
              go.Bar( y=budget_titles, x=budget_values, orientation='h',
      marker_color='#b3e427', name="В рублях", showlegend=True)
      ])
      fig2 = go.Figure(data=[
              go.Bar( y=amount_titles, x=amount_values, orientation='h',
      marker_color='#897AD6', name="Кол-во людей", showlegend=True )
      ])
      fig.update_traces(
      hoverlabel_font_color='white'
  )
      fig2.update_traces(
      hoverlabel_font_color='white'
  )
      fig.update_layout(legend={
          "title":'<b>Бюджет</b>',
          "font":{
              "family":'Arial, sans-serif',
              "size":14,
              "color":'black'
          },
          "traceorder":'normal',
          "y": 1,
          "x": 0.5,
          "orientation": "h",
          "yanchor":'bottom',
          "xanchor":'center',
      }, margin=dict(l=0, r=0, t=50, b=0))
      fig2.update_layout(legend={
          "title":'<b>Численность</b>',
          "font":{
              "family":'Arial, sans-serif',
              "size":14,
              "color":'black'
          },
          "traceorder":'normal',
          "y": 1,
          "x": 0.5,
          "orientation": "h",
          "yanchor":'bottom',
          "xanchor":'center',
      },margin=dict(l=0, r=0, t=50, b=0))
      return [card(budget,budget_per_person,'Бюджет на человека','Бюджет', True),
              card(youth_involvement,population_involvement,'Уровень вовлеченности населения','Количество вовлеченной молодежи', color=color)], [dcc.Graph(id="histogram",figure=fig),
              dcc.Graph(id="histogram2", figure=fig2)],{"display": "flex", "gap": "20px", "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "flex-start" }
    
    return "Ошибка", "Такого типа данных нет"
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
    "Основное", "СМИ"
                ],
                id='type',
                style={"min-width": "300px"},
                placeholder="Выберите данные"
            )
        ],
            style={"display": "flex", "gap": "20px", "justify-content": "flex-start"}),
            html.Div(id="cards", style={"display": "flex", "gap": "20px", "margin": "1rem 0", "flex-wrap": "wrap", "justify-content": "space-between" }),
            html.Div([], style={"display": "flex"}, id="charts")
            
    ]
)
