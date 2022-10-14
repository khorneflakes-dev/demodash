from dash import Dash, dcc, html, Input, Output
import os
import pandas as pd
import plotly_express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src='assets/pizzalogo.png', className='pizza-logo'),
            html.Div([
                html.H1("Plato's Pizza", className='title'),
                html.P('Year Performance - 2015', className='subtitle-banner'),
            ], className = 'title-container'),
        ], className='pizza-container'),
        html.Img(src='assets/mavenlogo.png', className='maven-logo'),
    ], className = 'banner'),

    # row 1
    html.Div([

        html.Div([
            
            html.Div([
                dcc.RadioItems(id='dias-aux', value='', className='dias-aux'),

            ], className='row1-column1-row1'),

            html.Div([

                dcc.Graph(id='dias_graph', figure={}, clickData=None)

            ], className='row1-column1-row2')

        ], className='row1-column0'),

        html.Div([

            html.Div([

                dcc.Graph(id='horas-graph', figure={})

            ], className='horas-graph')

        ], className='row1-column1'),

        html.Div([
            
            html.Div([
            dcc.Graph(id='revenue-per-month', figure={}, clickData=None),
            ], className='rpm-graph'),

        ], className='row1-column3')

    ], className='row1'),
    
    html.Div([
        html.Div([

            html.P(id='anio', className='anio')

        ], className = 'row1-1-column1'),
        
        html.Div([

            html.P('Revenue', className='revenue-title'),

            html.P(id='revenue-value', className='revenue-value')

        ], className = 'row1-1-column2'),
        
        html.Div([

            html.P('# Orders', className='order-title'),

            html.P(id='orders-value', className='orders-value')

        ], className = 'row1-1-column3'),
        
        html.Div([

            html.P('Pizzas Sold', className='pizzas-sold-title'),

            html.P(id='pizzas-sold-value', className='pizzas-sold-value')

        ], className = 'row1-1-column4'),
        
        html.Div([

            html.P('Average Order Price', className='avg-title'),

            html.P(id='avg-value', className='avg-value')
        ], className = 'row1-1-column5'),
        

    ], className='row1-1'),

    html.Div([
        html.Div([

            dcc.Graph(id='size', figure={}),

        ], className='row2-column2'),

        html.Div([

            html.P('Top 5 Best and Worst pizzas sold, these sales can be filtered according to:', className = 'descriptor'),
            dcc.RadioItems(
                id='selector',
                options=[
                    {'label': 'Revenue', 'value': 'revenue'},
                    {'label': 'Quantity', 'value': 'quantity'},
                ], value='revenue', className='radio-items')

        ], className='row2-column3'),

        html.Div([

            dcc.Graph(id='best-selling', figure={}, className='graph-best-selling'),

        ], className='row2-column1'),

        html.Div([

            dcc.Graph(id='worst-selling', figure={}, className='graph-worst-selling'),

        ], className='row2-column4'),

    ], className='row2'),

    html.Div([

        html.Div([
            dcc.Graph(id='seats', figure={}, className='seats-graph')
        ], className='row3-column1'),

        html.Div([

            html.P('Seating Capacity Review', className='title'),

            html.P('We have 60 seats and 15 tables, so we have 4 seats per table'),

            html.P('Approximately 70% of the orders are for 1 or 2 pizzas and the remaining 30% are orders for 3, 4 or more pizzas'),

            html.P('In conclusion, we are using the full capacity of a table with only 30% of the orders')

        ], className = 'row3-column2'),

        html.Div([
            dcc.Graph(id='pie-seats', figure={}, className='pie-seats-graph')
        ], className = 'row3-column3')

    ], className='row3'),

    html.Div([

        html.P('About me', className='about-me-title'),

        html.Div([

            html.Div([

                html.A(
                    href="https://github.com/khorneflakes-dev/maven-pizza-challenge",
                    target="_blank",
                    children=[
                        html.Img(
                            alt="source code",
                            src="assets/github-logo.png",
                        )
                    ], className='github-logo'
                ),

            ], className = 'about-icon-1'),
            
            html.Div([

                html.A(
                    href="https://www.linkedin.com/in/khorneflakes/",
                    target="_blank",
                    children=[
                        html.Img(
                            alt="linkedin",
                            src="assets/linkedin-logo.png",
                        )
                    ], className='linkedin-logo'
                ),
            ], className = 'about-icon-2')

        ], className='about-icons')

    ], className='about-me')

], className = 'main-container')


# @app.callback(Output('display-value', 'children'),
#                 [Input('dropdown', 'value')])
# def display_value(value):
#     return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)