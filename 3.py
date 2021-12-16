#!/usr/bin/python
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Data=pd.read_csv('population_prospects.csv',sep=',')
Data.head(1)
print(Data)


states = Data.country.drop_duplicates().to_list()

print(states)

COUNTRIES=[]

for st in states:
        y=Data.where(Data.country==st).dropna().population.to_list()   #list of populations
        x=Data.where(Data.country==st).dropna().year.to_list() 
        
        popul2100=np.interp(2100,x,y)
        popul2000=np.interp(2000,x,y)
        print(f" Country-{st} expected population in 2100 - {popul2100}, fact population in 2000 {popul2000}")
        
        COUNTRIES.append([ st ,popul2100,popul2000 ])
        


fig = go.Figure()

for  c in COUNTRIES:
        if (c[2]>c[1]):
                countr_col='crimson'
                info='населення зменьшуєтся'
        else:
                countr_col='royalblue'
                info='населення збільшується'
                
        fig.add_trace(go.Scattergeo(
                locationmode='country names',
                locations=[c[0]],
                text=[info + ' та в 2100 году буде ' + str(c[1]) +' що в процентному відношенні '+ str(int(c[1]/c[2]*100))],
                 marker = dict(
            size = 10,
            color = countr_col,
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'),
                geo='geo2'))
        fig.update_geos(
    visible=False, resolution=50,
    showcountries=True, countrycolor="RebeccaPurple"
)
fig.update_layout(height=800, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

