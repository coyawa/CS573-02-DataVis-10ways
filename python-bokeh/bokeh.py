
# coding: utf-8

# In[31]:

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import FixedTicker
data =pd.read_csv("cars-sample.csv")

x=data["Weight"]
y=data["MPG"]

colormap = {'bmw':'tomato','ford':'goldenrod','honda':'lightseagreen','mercedes':'lightskyblue','toyota':'blueviolet'}
colors = [colormap[x] for x in data['Manufacturer']]

p = figure(width=600, height=500, x_range=[1500, 5000], y_range=[5, 50],)
p.xaxis.axis_label = 'Weigh'
p.yaxis.axis_label = 'MPG'
p.yaxis.axis_label_text_font_style = "normal"
p.yaxis.axis_label_text_font_style = "bold"
p.xaxis.axis_label_text_font_style = "normal"
p.xaxis.axis_label_text_font_style = "bold"
p.xaxis[0].ticker = FixedTicker(ticks=[2000,3000,4000,5000])
p.yaxis[0].ticker = FixedTicker(ticks=[10,20,30,40,50])

p.circle(x, y, radius=size, color=colors, alpha=0.5,line_color=None)

output_file("python-bokeh.html")

show(p)


# In[ ]:



