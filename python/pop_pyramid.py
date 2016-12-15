# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 07:49:42 2016

@author: Harry

This python module was modified from it's original context at

http://stackoverflow.com/questions/27694221/using-python-libraries-
to-plot-two-horizontal-bar-charts-sharing-same-y-axis

Pandas was imported and used as a dataframe manipulation toolkit that allowed
me to substitute data based on the census international dataset CSV files.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# User choice for country
filename = input('Enter a Country...')
# Importing Census CSV from local root of .py file
df=pd.read_csv('../csv/'+filename+'.csv',header=1, skiprows=[2])

# Funtion to normalize population values based on their magnitude
def scale_size(longint):
    longstring = str(longint)
    scale = 0.001
    for i in longstring:
        scale = scale * 10        
    return  scale
 
# Data
age_groups = df['Age']
f_pop = df['Female Population'].max()
f_scale = scale_size(f_pop)
f_pop_max = ((f_pop)//(f_scale))
f_pop_scaled = ((df['Female Population'])//(f_scale))
m_pop = df['Male Population'].max()
m_scale = scale_size(m_pop)
m_pop_max = ((m_pop)//(m_scale))
m_pop_scaled = ((df['Male Population'])//(m_scale))

# AxesFormat
y = np.arange(age_groups.size)
fig, axes = plt.subplots(ncols=2, sharey=True)
axes[0].barh(y, f_pop_scaled, align='center', color='gray', zorder=10)
axes[0].set(title=('Population Female (x' + str(f_scale)+')'))
axes[0].set_xlim(0,((f_pop_max)+10))
axes[1].barh(y, m_pop_scaled, align='center', color='gray', zorder=10)
axes[1].set(title=('Population Male (x' + str(f_scale)+')'))
axes[1].set_xlim(0,((m_pop_max)+10))
axes[0].invert_xaxis()
axes[0].set(yticks=y, yticklabels=age_groups)
axes[0].yaxis.tick_right()

# Layout Spacing
for ax in axes.flat:
    ax.margins(0.09)
    ax.grid(True)
fig.tight_layout()
fig.subplots_adjust(wspace=0.1975)

# Statistics

print(df.iloc[2:,:])
