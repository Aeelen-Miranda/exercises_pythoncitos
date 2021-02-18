

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import pandas as pd


###############################
# DATABASES
############################### Abre archivos

zacatecas = pd.read_csv('https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/Tabla%202.%20Delitos%20Zacatecas%20(2020)_2.csv', )
covid = pd.read_csv("https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/cdmx_deaths.csv")
bullet = pd.read_csv("https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/Tabla%20bullets.csv", encoding= "Latin1")


contagios = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Confirmados_20210216.csv")
decesos = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Defunciones_20210216.csv")




###############################
# TRATAMIENTO 
###############################   Contagios  por día



endall = len(contagios)

#Select and sum all columns data
contagios1 = contagios.iloc[:,3:endall].sum()

# Make a DataFrame
contagios2 = pd.DataFrame(contagios1)

# index decesos 
contagios2['index'] = contagios2.index 
contagios2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)



############################### Total de contagios 
contagiostotal = contagios2.cases.sum()
###############################


###############################   Contagios por mes  
# by moths 

format = '%d-%m-%Y'
contagios2['days'] = pd.to_datetime(contagios2['days'], format=format)

# Filtering by years and months
dec_feb20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 2)]
dec_mar20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 3)]
dec_abr20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 4)]
dec_may20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 5)]
dec_jun20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 6)]
dec_jul20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 7)]
dec_ago20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 8)]
dec_sep20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 9)]
dec_oct20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 10)]
dec_nov20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 11)]
dec_dic20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 12)]
dec_ene21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 1)]
dec_feb21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 2)]


# Summarize by months 
contagios_feb20 = dec_feb20.cases.sum()
contagios_mar20 = dec_mar20.cases.sum()
contagios_abr20 = dec_abr20.cases.sum()
contagios_may20 = dec_may20.cases.sum()
contagios_jun20 = dec_jun20.cases.sum()
contagios_jul20 = dec_jul20.cases.sum()
contagios_ago20 = dec_ago20.cases.sum()
contagios_sep20 = dec_sep20.cases.sum()
contagios_oct20 = dec_oct20.cases.sum()
contagios_nov20 = dec_nov20.cases.sum()
contagios_dic20 = dec_dic20.cases.sum()
contagios_ene21 = dec_ene21.cases.sum()
contagios_feb21 = dec_feb21.cases.sum()



###############################   Contagios por dia  

endall1 = len(decesos)
decesos1 = decesos.iloc[:,3:endall1].sum().T
decesos2 = pd.DataFrame(decesos1)
decesos2['index'] = decesos2.index 
decesos2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)


############################### Total de decesos 
decesos_tot = decesos2.cases.sum()
###############################


format = '%d-%m-%Y'
decesos2['days'] = pd.to_datetime(decesos2['days'], format=format)
decesos2

dec_feb20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 2)]
dec_mar20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 3)]
dec_abr20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 4)]
dec_may20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 5)]
dec_jun20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 6)]
dec_jul20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 7)]
dec_ago20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 8)]
dec_sep20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 9)]
dec_oct20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 10)]
dec_nov20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 11)]
dec_dic20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 12)]
dec_ene21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 1)]
dec_feb21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 2)]

decesos_feb20 = dec_feb20.cases.sum()
decesos_mar20 = dec_mar20.cases.sum()
decesos_abr20 = dec_abr20.cases.sum()
decesos_may20 = dec_may20.cases.sum()
decesos_jun20 = dec_jun20.cases.sum()
decesos_jul20 = dec_jul20.cases.sum()
decesos_ago20 = dec_ago20.cases.sum()
decesos_sep20 = dec_sep20.cases.sum()
decesos_oct20 = dec_oct20.cases.sum()
decesos_nov20 = dec_nov20.cases.sum()
decesos_dic20 = dec_dic20.cases.sum()
decesos_ene21 = dec_ene21.cases.sum()
decesos_feb21 = dec_feb21.cases.sum()












###############################
# GRAFICAS
###############################


############################### 1 Contagios Graph 

figaro = go.Figure()
figaro.add_trace(go.Bar(x=contagios2['days'],y=contagios2['cases'],
                #name='Contagios confirmados COVID-19',
                marker_color='#0776a8'  # cambiar nuemeritos de rgb
                ))
figaro.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Contagios diarios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"))



############################### 3 Decesos Graph 

figaro2 = go.Figure()
figaro2.add_trace(go.Bar(x=decesos2['days'],y=decesos2['cases'],
                #name='Contagios confirmados COVID-19',
                marker_color='#0776a8'  # cambiar nuemeritos de rgb
                ))
figaro2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Decesos diarios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"))




############################### 1 Cintillo 1  
#Tabla de titulos     
    
patabla2 = {'Contagios': [str(f"{contagiostotal:,d}")] }
patabla3 = pd.DataFrame (patabla2)

tabla2 = go.Figure(data=[go.Table(
#Header
    header=dict(values=list(patabla3),
                align= 'left'),

#Cells 
    cells=dict(values=[ patabla3
                      ],
              
               font_size=2,
               height= 80,
               align= 'left',
              ))])

#HEADER
tabla2.update_traces(header_fill_color='rgba(227,227,227,0.5)', selector=dict(type='table'))
tabla2.update_traces(header_font_family= "Montserrat ExtraBold", selector=dict(type='table'))
tabla2.update_traces(header_font_size=14, selector=dict(type='table'))
tabla2.update_traces(header_font_color="black", selector=dict(type='table'))
tabla2.update_traces(header_line_color="#e3e3e3", selector=dict(type='table'))

#cells
tabla2.update_traces(cells_font_size=50, selector=dict(type='table'))
tabla2.update_traces(cells_font_color= "goldenrod", selector=dict(type='table'))
tabla2.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla2.update_traces(cells_fill_color = 'rgba(227,227,227,0.5)', selector =dict(type="table"))
tabla2.update_traces(hoverlabel_namelength=80, selector=dict(type='table'))
tabla2.update_traces(cells_line_color= "#e3e3e3", selector=dict(type='table'))

tabla2.update_layout(paper_bgcolor='rgba(227,227,227,0.5)', #color de fondo
                    plot_bgcolor='rgba(227,227,227,0.5)',
                    )


############################### 1 Cintillo 2  
#Tabla de titulos     
    
patabla2a = {'Decesos': [str(f"{decesos_tot:,d}") ] }
patabla3a = pd.DataFrame (patabla2a)

tabla2a = go.Figure(data=[go.Table(
#Header
    header=dict(values=list(patabla3a),
                align= 'left'),

#Cells 
    cells=dict(values=[ patabla3a
                      ],
              
               font_size=2,
               height= 80,
               align= 'left',
              ))])

#HEADER
tabla2a.update_traces(header_fill_color='rgba(227,227,227,0.5)', selector=dict(type='table'))
tabla2a.update_traces(header_font_family= "Montserrat ExtraBold", selector=dict(type='table'))
tabla2a.update_traces(header_font_size=16, selector=dict(type='table'))
tabla2a.update_traces(header_font_color="black", selector=dict(type='table'))
tabla2a.update_traces(header_line_color="#e3e3e3", selector=dict(type='table'))

#cells
tabla2a.update_traces(cells_font_size=50, selector=dict(type='table'))
tabla2a.update_traces(cells_font_color= "goldenrod", selector=dict(type='table'))
tabla2a.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla2a.update_traces(cells_fill_color = 'rgba(227,227,227,0.5)', selector =dict(type="table"))
tabla2a.update_traces(hoverlabel_namelength=80, selector=dict(type='table'))
tabla2a.update_traces(cells_line_color= "#e3e3e3", selector=dict(type='table'))

tabla2a.update_layout(paper_bgcolor='rgba(227,227,227,0.5)', #color de fondo
                    plot_bgcolor='rgba(227,227,227,0.5)',
                    )



############

############################### 3 Cintillo meses CONTAGIOS

patabla6 = {#COLUMNS        #FILAS
            #'    '        : ['Contagios'],#, 'Decesos'],
            'febrero20'   : [str(f"{contagios_feb20:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{contagios_mar20:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{contagios_abr20:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{contagios_may20:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{contagios_jun20:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{contagios_jul20:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{contagios_ago20:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{contagios_sep20:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{contagios_oct20:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{contagios_nov20:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{contagios_dic20:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{contagios_ene21:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{contagios_feb21:,d}")],#, decesos_feb21],
                            }



patabla7 = pd.DataFrame (patabla6, columns = [#'blanc',
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])
tabla6 = go.Figure(data=[go.Table(
    header=dict(values=list(patabla6),
                align=['left']),
                columnwidth = 2,
    
    cells=dict(values=[#patabla7.blanc,
                       patabla7.febrero20,patabla7.marzo20,patabla7.abril20,patabla7.mayo20,patabla7.junio20,patabla7.julio20,
                       patabla7.agosto20,patabla7.septiembre20,patabla7.octubre20,patabla7.noviembre20,patabla7.diciembre20,
                       patabla7.enero21,patabla7.febrero21],
               # fill_color='#e3e3e3',
               font_size=2,
               height= 25,
               align='left'),)])
#HEADER
tabla6.update_traces(header_fill_color='#284740', selector=dict(type='table'))
tabla6.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla6.update_traces(header_font_size=9, selector=dict(type='table'))
tabla6.update_traces(header_font_color="white", selector=dict(type='table'))
tabla6.update_traces(header_line_color='rgba(255,255,255,0)', selector=dict(type='table'))

#cells
tabla6.update_traces(cells_font_size=15, selector=dict(type='table'))
tabla6.update_traces(cells_font_color= "white", selector=dict(type='table'))
tabla6.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla6.update_traces(cells_fill_color = '#284740', selector =dict(type="table"))
tabla6.update_traces(hoverlabel_namelength=13, selector=dict(type='table'))
tabla6.update_traces(cells_line_color= "rgba(255,255,255,0)", selector=dict(type='table'))

tabla6.update_layout(paper_bgcolor='rgba(255,255,255,0)', #color de fondo
                    plot_bgcolor='rgba(255,255,255,0)',
                    #line_color = 'rgba(255,255,255,0)'
                    )






############

############################### 3 Cintillo meses DECESOS

patabla6a = {#COLUMNS        #FILAS
            #'    '        : ['Contagios'],#, 'Decesos'],
            'febrero20'   : [str(f"{decesos_feb20:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{decesos_mar20:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{decesos_abr20:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{decesos_may20:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{decesos_jun20:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{decesos_jul20:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{decesos_ago20:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{decesos_sep20:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{decesos_oct20:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{decesos_nov20:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{decesos_dic20:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{decesos_ene21:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{decesos_feb21:,d}")],#, decesos_feb21],
                            }



patabla7a = pd.DataFrame (patabla6a, columns = [#'blanc',
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])
tabla6a = go.Figure(data=[go.Table(
    header=dict(values=list(patabla6a),
                align=['left']),
                columnwidth = 2,
    
    cells=dict(values=[#patabla7.blanc,
                       patabla7a.febrero20,patabla7a.marzo20,     patabla7a.abril20,patabla7a.mayo20,patabla7a.junio20,patabla7a.julio20,
                       patabla7a.agosto20, patabla7a.septiembre20,patabla7a.octubre20,patabla7a.noviembre20,patabla7a.diciembre20,
                       patabla7a.enero21,  patabla7a.febrero21],
               # fill_color='#e3e3e3',
               font_size=2,
               height= 25,
               align='left'),)])
#HEADER
tabla6a.update_traces(header_fill_color='#284740', selector=dict(type='table'))
tabla6a.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla6a.update_traces(header_font_size=9, selector=dict(type='table'))
tabla6a.update_traces(header_font_color="white", selector=dict(type='table'))
tabla6a.update_traces(header_line_color='rgba(255,255,255,0)', selector=dict(type='table'))

#cells
tabla6a.update_traces(cells_font_size=15, selector=dict(type='table'))
tabla6a.update_traces(cells_font_color= "white", selector=dict(type='table'))
tabla6a.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla6a.update_traces(cells_fill_color = '#284740', selector =dict(type="table"))
tabla6a.update_traces(hoverlabel_namelength=13, selector=dict(type='table'))
tabla6a.update_traces(cells_line_color= "rgba(255,255,255,0)", selector=dict(type='table'))

tabla6a.update_layout(paper_bgcolor='rgba(255,255,255,0)', #color de fondo
                    plot_bgcolor='rgba(255,255,255,0)',
                    #line_color = 'rgba(255,255,255,0)'
                    )


















####################################

# A P P

####################################



########### Define your variables

mytitle=''
tabtitle='COVID-19 en México'
githublink='https://github.com/Aeelen/exercises_pythoncitos/'
sourceurl='https://plotly.com/python/histograms/'


app = dash.Dash()
colors = {
    'background': '#e3e3e3',
    'text': '#b38115',
    'table': 'rgba(227,227,227,0.5)'
    }

server = app.server
app.title=tabtitle


#################################### TITULOS GENERALES DE APP

app.layout = html.Div(children=[
    
    html.Div(children = [ dcc.Markdown(''' 
    # COVID-19 en México
    ###### Cámara de Diputados, México, 17 de febrero de 2021
    
    ''',)],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'],'width': '100%',
                  }), 
    
  
#################################### DISEÑO DE APP

       
# Primera franja (lista)
    html.Div(children = [dcc.Graph(figure=tabla2)],
             style={'margin': '0% 0px -500px 70px', 'width':'50%',  #margen: arriba,derecha,abajo,izquierda
                                                                                                    
                    'font-family': 'Montserrat'}),
                   
# Segunda franja (Lista)
    html.Div( children = [dcc.Graph(figure=figaro)],                  
             style = {'margin': '0% 0px 0px 0px', 'width':'100%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),


    
# Tercera franja (lista)
    html.Div(children = [dcc.Graph(figure=tabla2a)],
             style={'margin': '0% 0px -500px 70px', 'width':'50%',  #margen: arriba,derecha,abajo,izquierda
                                                                                                    
                    'font-family': 'Montserrat'}),
                   
    
# Cuarta franja
    html.Div( children = [dcc.Graph(figure=figaro2)],                  
             style = {'margin': '0% -600px -100px 0x', 'width':'100%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),

 
# Quinta franja
    
    html.Div(children = [dcc.Graph(figure=tabla6)],
             style={'margin': '-63.9% 0px -50% 55px', 'width':'100%',  #margen: arriba,derecha,abajo,izquierda
                                                                                                    
                    'font-family': 'Montserrat'}),
                   
 

# Sexta franja
    
    html.Div(children = [dcc.Graph(figure=tabla6a)],
             style={'margin': '-22.8% 0px 0% 55px', 'width':'100%',  #margen: arriba,derecha,abajo,izquierda
                                                                                                    
                    'font-family': 'Montserrat'}),
                   
    

#############################################################      

  
    #html.A('Code on Github', href=githublink),
    html.Br(),
    #html.A('Data Source', href=sourceurl),

],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )
                     

if __name__ == '__main__':
    app.run_server()




# autosize=True,
# Elegir colores CSS
#https://developer.mozilla.org/es/docs/Web/CSS/CSS_Colors/Herramienta_para_seleccionar_color
