# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div([
        dcc.Input(id='my-id',value='Initial value', type= 'text'),
        html.Div(id= 'my-div', style={'border':'2px blue solid'})
        
        
        
])

@app.callback(output = Output(component_id='my-div', component_property='children'),
              inputs=[Input(component_id='my-id', component_property='value')])
def update_output_div(value):
    return "You entered: {}".format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
