# -*- coding: utf-8 -*-
'''
dcc docu: https://dash.plot.ly/dash-core-components

Getting documentaion
$ pydoc dash_html_components.Div -w 

'''


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

app = dash.Dash()

## CSS styling
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
colors = {'background':'#111111','text': '#7fDBFF'}

###defining a figure in code first
def generate_fig():
    numberOfPoints = 200
    values_x = np.linspace(0,1,numberOfPoints)
    #print(values_x)
    values_y = np.random.randn(numberOfPoints)
    
    trace0 = go.Scatter(x= values_x, y=values_y + 5, 
                       mode='markers', name = 'markers')
    trace1 = go.Scatter(x= values_x, y= values_y,
                       mode='lines', name = 'lines')
    trace2 = go.Scatter(x = values_x, y= values_y -3, 
                       mode='lines+markers', name='lines and markers')
    datalines = [trace0, trace1, trace2]
    layoutLine= go.Layout(title='Line Charts')
    fig = go.Figure(data=datalines, layout=layoutLine)
    return fig

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

    
markdown_text = '''
# This is Header 1 in Markdown
This looks very promising
```
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
```
That was some code ....
'''
app.layout= html.Div(children =[
        html.H1('Hello Tom again', style={'textAlign': 'center', 'color': '#7FDBFF'}),
        html.Div("That is my first one with style", style={'color':colors['text'
                                                                          ]}),
        html.Div('''
        and more divs in a trible quote         
        '''
        ),
        dcc.Graph(id='graph in code', figure = generate_fig())     
        ,
        html.Label('Dropdown'),
        dcc.Dropdown(id='dropdown1', options = [{'label' : 'New York', 'value':'NYC'},
                                                dict(label = 'Chattanooga', value='CHA'),
                                                dict(label = 'Atlanta', value = 'ATL')],
                    value='CHA'),
        html.P(['Multiple Dropdown Selection']),
        dcc.Dropdown(id='dropdown2', options =[{'label' : 'New York', 'value':'NYC'},
                                                dict(label = 'Chattanooga', value='CHA'),
                                                dict(label = 'Atlanta', value = 'ATL')],
                    value='CHA',
                    multi= True)
        , html.Label('Slider'),
        
        html.P(dcc.Slider(id='slider',min=0, max=10, 
                   marks = {i: 'Floor {}'.format(i) for i in range(10) },
                   value = 5)),
        
        html.P(html.Div('Graph example with black background'))
        ,
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization with dark background',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font':{'color': colors['text']}
            }
        }
    ),
    dcc.Markdown(markdown_text)
    ,
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
