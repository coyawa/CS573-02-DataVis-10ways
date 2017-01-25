
# coding: utf-8

# In[ ]:




# In[11]:

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

a2 = pd.read_csv("/Users/Coyawa/Git/02-DataVis-10ways/python-plotly/cars-sample.csv")
a2.head()

bmw = go.Scatter(
                   x = a2['Weight'][a2['Manufacturer'] == 'bmw'],
                   y = a2['MPG'][a2['Manufacturer'] == 'bmw'],
                   mode = 'markers',
                   name='bmw',
                   marker = dict(
                       size = a2['Weight'][a2['Manufacturer'] == 'bmw']/200,
                       opacity = 0.5,
                       color = 'tomato'
                   )
)

ford = go.Scatter(
                   x = a2['Weight'][a2['Manufacturer'] == 'ford'],
                   y = a2['MPG'][a2['Manufacturer'] == 'ford'],
                   mode = 'markers',
                   name='ford',
                   marker = dict(
                       size = a2['Weight'][a2['Manufacturer'] == 'ford']/200,
                       opacity = 0.5,
                       color = 'goldenrod'
                   )
)

honda = go.Scatter(
                   x = a2['Weight'][a2['Manufacturer'] == 'honda'],
                   y = a2['MPG'][a2['Manufacturer'] == 'honda'],
                   mode = 'markers',
                   name='honda',
                   marker = dict(
                       size = a2['Weight'][a2['Manufacturer'] == 'honda']/200,
                       opacity = 0.5,
                       color = 'lightseagreen'
                   )
)

mercedes = go.Scatter(
                   x = a2['Weight'][a2['Manufacturer'] == 'mercedes'],
                   y = a2['MPG'][a2['Manufacturer'] == 'mercedes'],
                   mode = 'markers',
                   name='mercedes',
                   marker = dict(
                       size = a2['Weight'][a2['Manufacturer'] == 'mercedes']/200,
                       opacity = 0.5,
                       color = 'lightskyblue'
                   )
)

toyota = go.Scatter(
                   x = a2['Weight'][a2['Manufacturer'] == 'toyota'],
                   y = a2['MPG'][a2['Manufacturer'] == 'toyota'],
                   mode = 'markers',
                   name='toyota',
                   marker = dict(
                       size = a2['Weight'][a2['Manufacturer'] == 'toyota']/200,
                       opacity = 0.5,
                       color = 'blueviolet'
                   )
)

layout = go.Layout(
     width=760,
     height=700,
     xaxis = dict(
                  title = 'Weight'
                  ),
     yaxis = dict(
                 title = 'MPG'
                  ),
                   )

data = [bmw, ford, honda, mercedes, toyota]
fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename='A2-Congyang')


# In[ ]:




# In[ ]:



