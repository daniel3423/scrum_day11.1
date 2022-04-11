import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data1.csv')

trace1 = go.Bar(
    x=df['NOC'],  
    y=df['Spain'],
    name = 'Spain',
    marker=dict(color='#FFD700') 
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Poland'],
    name='Poland',
    marker=dict(color='#9EA0A1') 
)
trace3 = go.Bar(
    x=df['NOC'],
    y=df['Turkey'],
    name='Turkey',
    marker=dict(color='#CD7F32') 
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    title='Erasmus students outgoing Spain, Poland and Turkey'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar2.html')