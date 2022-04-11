# 2018 Winter Olympics Medals won by Country.
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data1.csv')

data = [go.Bar(
    x=df['NOC'],  
    y=df['Total']
)]
layout = go.Layout(
    title='Erasmus students outgoing Spain, Poland and Turkey'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')