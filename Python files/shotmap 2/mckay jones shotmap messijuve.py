# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 02:24:51 2021

@author: dev
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import mplsoccer
df = pd.read_csv('E:\mckayjohnes\github\Shotmaps-main\shotmaps.csv')

fig,ax= plt.subplots(figsize=(13,8.5))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = mplsoccer.VerticalPitch(pitch_type='statsbomb', pitch_color='#22312b',
              line_color='#c7d5cc',half=True)
pitch.draw(ax=ax)
#plt.gca().invert_yaxis()
plt.scatter(df['x'], df['y'],c='red',s=80,alpha=0.6)
plt.title('Messi shots vs juventus ', fontsize=30,c='White')