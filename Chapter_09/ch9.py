
# coding: utf-8

# In[100]:

# line chart
import plotly.plotly as py
from plotly.graph_objs import Scatter
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 50)

trace0 = Scatter(x=x.tolist(),
    y=np.sin(x).tolist(),
    name='sin(x)'
)
trace1 = Scatter(
    x=x.tolist(),
    y=np.cos(x).tolist(),
    name='cos(x)'
)

data = [trace0, trace1]

unique_url = py.plot(data, filename = 'sin-cos')


# In[96]:

# bar charts
import pandas as pd
crimes = pd.read_csv('crim_gen.tsv', sep=',|\t', na_values=': ')
crimes = crimes[crimes.country.isin(['IT','ES','DE'])]

burglary = crimes.query('iccs == "burglary"')[['country', '2012 ']].sort(columns='country').values
robbery = crimes.query('iccs == "robbery"')[['country', '2012 ']].sort(columns='country').values
motor_theft = crimes.query('iccs == "theft_motor_vehicle"')[['country', '2012 ']].sort(columns='country').values

import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Bar(
    x=burglary[:,0].tolist(),
    y=burglary[:,1].tolist(),
    name='burglary'
)

trace2 = Bar(
    x=motor_theft[:,0].tolist(),
    y=motor_theft[:,1].tolist(),
    name='motor_theft'
)

trace3 = Bar(
    x=robbery[:,0].tolist(),
    y=robbery[:,1].tolist(),
    name='robbery'
)


data = Data([trace1, trace2, trace3])
layout = Layout(
    barmode='stack'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='bars-crimes')


# In[98]:

import numpy as np
import plotly.plotly as py
from plotly.graph_objs import Scatter3d, Data, Layout
from plotly.graph_objs import Figure, Line, Margin, Marker

from numpy import linspace,pi,cos,sin
phi = linspace(0,2*pi,250)
x = sin(phi)+2*sin(2*phi)
y = cos(phi)-2*cos(2*phi)
z = -sin(3*phi)

traces = list()
colors = ['rgb(%d,50,210)' % c for c in np.abs(z / max(z)) * 255]
for i in linspace(-np.pi,np.pi,50):
    trace = Scatter3d(x=x+np.cos(i)*.5, y=y+np.sin(i)*.5, z=z,
                       mode='markers',
                       marker=Marker(color=colors, size=13))
    traces.append(trace)
    
data = Data(traces)

layout = Layout(showlegend=False, autosize=False,
                width=500, height=500,
                margin=Margin(l=0,r=0,b=0,t=65))

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='3d-trifoil')


# In[151]:

# map bubbles
import plotly.plotly as py
from plotly.graph_objs import *

import pandas as pd
crimes = pd.read_csv('crim_gen.tsv', sep=',|\t', na_values=': ')
crimes = crimes[crimes.country.isin(['IT','ES','DE','FR','NO','FI'])]

total_crimes = crimes.query('iccs == "TOTAL"')[['country', '2012 ']].sort(columns='2012 ').values
coords = {'IT': (13.007813, 42.553080), 'ES': (-3.867188, 39.909736), 'DE': (9.316406,50.736455),
          'FR': (2.636719, 46.195042), 'NO': (8.613281, 61.100789), 'FI': (25.839844, 62.431074)}
scale = 300000
countries = []


for info in total_crimes:
    c = coords[info[0]]
    country = dict(
        type = 'scattergeo',
        lon = [c[0]],
        lat = [c[1]],
        text = info[0]+':'+str(info[1]),
        sizemode = 'diameter',
        name= info[0],
        marker = dict( 
            size = info[1] / scale, 
            color = 'red',
            line = dict(width = 1,color = 'red')
        ))
    countries.append(country)

layout = dict(
        title = '2012 Reported crimes',
        showlegend = True,
        geo = dict(
            scope='europe'      
        ),  
    )
    
fig = dict( data=countries, layout=layout )
url = py.plot( fig, validate=False, filename='bubble-map-crimes' )


# In[ ]:



