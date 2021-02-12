import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


################################### Abre archivos
zacatecas = pd.read_csv('https://raw.githubusercontent.com/Aeelen-Miranda/flying-dog-beers/master/Tabla%202.%20Delitos%20Zacatecas%20(2020)_2.csv', )
covid = pd.read_csv("https://raw.githubusercontent.com/Aeelen-Miranda/flying-dog-beers/master/cdmx_deaths.csv")

################################### Prepara Grafica 1
pv = pd.pivot_table(zacatecas, index=['Municipio'], columns=['Tipo de delito'], values=['ene-20'],aggfunc=sum, fill_value = 0)

g1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Robo')], name = 'Robo')
gr1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Violencia familiar')], name = 'Violencia familiar')
gra1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Lesiones')], name = 'Lesiones')
graf1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Otros delitos del Fuero Común')], name = 'Otros delitos del Fuero Común')
grafi1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Daño a la propiedad')], name = 'Daño a la propiedad')
grafic1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Fraude')], name = 'Fraude')
grafica1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Amenazas')], name = 'Amenazas')

################################## Grafica 2
grafica2 = px.line(covid, x = covid['nom_mun'], y = covid['quincena0'])
grafica2.update_traces(orientation = 'v')
grafica2.update_layout(font_family="Montserrat",title = '<b>Quincena 0</b>',
                       template = 'plotly_dark',title_font_family="Montserrat",
                       title_font_color="goldenrod",)
#################################### Grafica 3
grafica3 = px.line(covid, x = covid['nom_mun'], y = covid['quincena2'])
grafica3.update_traces(orientation = 'v')
grafica3.update_layout(font_family="Montserrat",
                       title = '<b>Quincena 2</b>',
                       template = 'plotly_dark',
                       title_font_family="Montserrat",
                       title_font_color="goldenrod",)
################################### Grafica 4
grafica4 = px.line(covid, x = covid['nom_mun'], y = covid['quincena3'])
grafica4.update_traces(orientation = 'v')
grafica4.update_layout(font_family="Montserrat",title = '<b>Quincena 3</b>',
                      template='plotly_dark',title_font_family="Montserrat",
                      title_font_color="goldenrod",)
############################################ Grafica 5
grafica5 = px.line(covid, x = covid['nom_mun'], y = covid['quincena4'])
grafica5.update_traces(orientation = 'v')
grafica5.update_layout(font_family="Montserrat",title = '<b>Quincena 4</b>',
                      template='plotly_dark',title_font_family="Montserrat",
                       title_font_color="goldenrod", )
grafica5.update_xaxes(title_font_family="Montserrat")

############################################ Grafica 6
grafica6 = px.line(covid, x = covid['nom_mun'], y = covid['quincena5']) # , color= "nom_mun")

grafica6.update_traces(orientation = 'v', marker=dict(size=12,
                              line=dict(width=2,
                              color='LightGrey')),
                              selector=dict(mode='markers'))
                     
grafica6.update_layout(font_family="Montserrat", #Tipo de letra del contenido de gráfica 
                       title = '<b>Quincena 5</b>',
                       template='plotly_dark',
                      title_font_family="Montserrat", #Tipo de letra del titulo
                      title_font_color="goldenrod",
                      #line_color= "dark"
                      ) #Con esto se cambia color letra
grafica6.update_xaxes(title_font_family="Montserrat") #Tipo de letra de x,y
########################################### Grafica 8
grafica8 = px.scatter(covid, x='Total', y='nom_mun', size='Total', 
                      color='quincena6', title = '<b>Incidencia delictiva en alcaldias</b>',
                     template = "plotly_dark",
                     )
grafica8.update_traces(orientation = 'v')
grafica8.update_layout(
    font_family="Montserrat",
    font_color="lightgray",
    title_font_family="Montserrat",
    font_size=10,
    title_font_color="goldenrod",
    legend_title_font_color="green"
    
)
grafica8.update_xaxes(title_font_family="Montserrat")
#PRIMEr paso

############################################ Grafica 9
eindex = covid[['nom_mun','Total' ,'quincena0', 'quincena2',
       'quincena3', 'quincena4', 'quincena5', 'quincena6']]

# segundo step

eindexx = eindex.groupby(by = 'nom_mun').agg(sum)


# tercer step

egroup_index = eindexx[['Total']].sort_values(by = 'nom_mun')
egroup_index

# creación de la gráfica 


grafica9 = go.Figure()
grafica9.add_trace(go.Bar(
    y=eindexx.quincena0.values,
    x=eindexx.index,
    name='quincena0',
    marker_color='#572364',
     
))

grafica9.add_trace(go.Bar(
    y=eindexx.quincena2.values,
    x=eindexx.index,
    name='quincena2',
    marker_color='#A18594'
))

grafica9.add_trace(go.Bar(
    y=eindexx.quincena3.values,
    x=eindexx.index,
    name='quincena3',
    marker_color='#6C4675'
))
grafica9.add_trace(go.Bar(
    y=eindexx.quincena4.values,
    x=eindexx.index,
    name='quincena4',
    marker_color='#AA00FF'
))
grafica9.add_trace(go.Bar(
    y=eindexx.quincena5.values,
    x=eindexx.index,
    name='quincena5',
    marker_color='#9C2780'
))
grafica9.add_trace(go.Bar(
    y=eindexx.quincena6.values,
    x=eindexx.index,
    name='quincena6',
    marker_color='#CE93D8'
))

grafica9.update_traces(orientation = 'v')
grafica9.update_layout(title = '<b>9. Delitos totales por Alcaldía</b>',
                       title_font_family="Montserrat",title_font_color="goldenrod",
                       
                 template='plotly_dark')
####################################################################################
########### Define your variables

mytitle='Añadir graficas'
tabtitle='Prueba Dash!'
githublink='https://github.com/Aeelen-Miranda/flying-dog-beers'
sourceurl='https://plotly.com/python/histograms/'



########### Initiate the app
app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#C0C0C0'
}
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    
    html.Div(children = [ dcc.Markdown(
        ''' 
    #Prueba de Dashboard
    ## prueba sobre delitos
    ###### jueves 11 de febrero de 2020
''',
         )],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'],'width': '100%'}
        ),
     
    
    html.Div( children = [dcc.Graph(id='grafica1',
              figure= {'data':[g1,gr1,gra1,graf1,grafi1,grafic1,grafica1],
                       'layout': go.Layout(paper_bgcolor='black', #color de fondo
                                           plot_bgcolor='black',
                                           title='Mayor incidencia delictiva',
                                           barmode='group')})],
             style = {'margin': '1% 0px 0px 0px', 'width':'60%',
                     'font-family': 'Montserrat',#Cambia tipo de letra
                    }),
   html.Div(children =[dcc.Graph(figure=grafica2)],
            style={'margin': '2% 0px 0px 1px', 'width':'50%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
   html.Div(children = [dcc.Graph(figure=grafica3)],
           style={'margin': '2% 0px 0px 1px', 'width':'50%',
                 'font-family': 'Montserrat',
                 'backgroundColor': colors['background']}),
    html.Div(children =[dcc.Graph(figure=grafica4)],
             style={'margin': '2% 0px 0px 1px', 'width':'50%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
    html.Div(children = [dcc.Graph(figure=grafica5)],
            style={'margin': '2% 0px 0px 0px', 'width':'22%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
    
    html.Div(children =[dcc.Graph(figure=grafica6)],
             style={'margin': '3% 0px 0px 0px', 'width':'100%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
    html.Div(children =[dcc.Graph(figure=grafica8)],
            style={'margin': '2% 0px 0px 0px', 'width':'60%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),

#quinta franja
    html.Div(children = [dcc.Graph(figure=grafica9)],
            style={'margin': '2% 0px 0px 0px', 'width':'100%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl)
    
],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )
                     

if __name__ == '__main__':
    app.run_server()

