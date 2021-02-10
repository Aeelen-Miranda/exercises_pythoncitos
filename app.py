import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Irina'
label1='IBU'
label2='ABV'
githublink='https://github.com/Aeelen-Miranda/flying-dog-beers'
sourceurl='https://dash.plotly.com/dash-core-components/graph'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

####################dos
histograma = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
dcc.Graph(
        id='example-graph-2',
        figure=histograma
    )
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#C0C0C0'
}
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.Div(children = [ 
    dbc.NavbarSimple(
        children=[
        dbc.NavItem(dbc.NavLink("Web Portal",
                                style={'textAlign': 'center','color': colors['text']},
                                       href="https://plotly.com/python/figure-labels/")),
        ],
        brand="Analytics Dashboard",
        brand_href="https://matplotlib.org/gallery/api/font_family_rc_sgskip.html",
        color="#E3E4E5",
        dark=True,)],
        style={'textAlign': 'center','color': colors['text'],
               'font-family': 'Montserrat', 'font-weight': 'bold','width': '100%',},
        ),
    
    html.Div( children = [dcc.Graph(id='flyingdog',
        figure=beer_fig
    ),
    html.Div( children = [dcc.Graph(id='example-graph-2',
        figure=histograma
    ),                      
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )

if __name__ == '__main__':
    app.run_server()
