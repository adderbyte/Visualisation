import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

df =  pd.read_excel('population.xlsx',skiprows=range(0, 2)) 
colors = {
    'background': '#111111',
    'text': 'teal'
}
app = dash.Dash()
years = np.array(['2013','2014','2015','2016'])
app.layout = html.Div([
		html.H3(
			children='UK Population Analytics Plot',
			style={
				'textAlign': 'center',
				 'fontWeight': 'bold',
				 'color': 'teal'
			}
		),
		html.Div([
			
			html.Div([
				dcc.Dropdown(
					id='state-id',
					options=[{'label': i, 'value': i} for i in df.Geography.unique()],multi = True,
					placeholder='Filter by UK region...'
				)
			],
			style={'width': '49%', 'display': 'inline-block'}),
			html.Div([
			dcc.Dropdown(
				id='years-id', 
				options=[{'label': i , 'value': i} for i in years],
				multi=True, placeholder='Filter by Year...'
				)
			],
			style={'width':'48%', 'display': 'inline-block'}),
		
		
			
		
		    html.Div([
			dcc.Dropdown(
				id='indicator-id',
				options=[{'label': i , 'value': i} for i in df.Age.unique()],
				multi=True, placeholder='Filter by Age ...'
				)
			],
			style={'width':'48%', 'display': 'inline-block'}),
		
		
		dcc.Graph(id='indicator-graphic',style={'width':'1300','height':'700'})
		])
	])


@app.callback(
	dash.dependencies.Output('indicator-graphic', 'figure'),
	[dash.dependencies.Input('state-id', 'value'),
	 dash.dependencies.Input('indicator-id', 'value'),dash.dependencies.Input('years-id', 'value')])

def update_time_series(state_id, indicator_ids,years_id):
	
	#print(dff.head())
	data = []
	if state_id is not None or indicator_ids is not None or years_id is not None:
		for state in state_id :
			for  indicator_id in indicator_ids:
				for year in years_id:
					#print(state,indicator_id)
					#print(df.head())
					if state_id is not None or indicator_ids is not None or years_id is not None:
						dff = df.loc[(df['Geography'] == state ) &  (df['Age'] == indicator_id)   ]
						#for indicator_id in indicator_ids:
							#print(indicator_id)
						#for columns in ['2013','2014','2015','2016']:
						#	print()
						trace = go.Bar(
							x = dff['Sex'],
							y = dff[year],#mode='lines'
							name = 'Plot for State ' + state + ' Year ' + year + ' Age ' + indicator_id
							
							)
						data.append(trace)
					else:
						pass
		return {
			'data' : data,
			'layout' : go.Layout(
				xaxis={'title': 'Gender'},
				yaxis={'title': 'Population By Gender'},
				
			)
		}
	else:
		pass

if __name__ == '__main__':
	app.run_server(debug=True)
