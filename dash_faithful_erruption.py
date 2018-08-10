# -*- coding: utf-8 -*-
import plotly.graph_objs as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

def getFaithful():
    df = pd.read_csv('Data/OldFaithful.csv')
    
    trace1 = go.Scatter(x = df['X'], y = df['Y'], name='Faiful', mode = 'markers')
    data = [trace1]
    layout = go.Layout(title='Faithful duration vs. interval',
                       xaxis = dict(title = 'Inteval between erruptions'),
                       yaxis = dict(title ='Duration of erruptions'))
    fig = go.Figure(data = data, layout = layout )
    return fig

app.layout = html.Div(children = [html.H1("Faithful erruption"),
                    dcc.Graph(id = 'Faithful', figure= getFaithful())             
                                  
                    ])

if __name__ == '__main__':
    app.run_server(debug = True)

