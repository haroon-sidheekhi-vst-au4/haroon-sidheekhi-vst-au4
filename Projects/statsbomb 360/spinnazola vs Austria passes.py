# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:24:03 2023

@author: hp
"""

import pandas as pd
from statsbombpy import sb
from mplsoccer import Pitch

MATCH_ID = 3794685		
file_name=str(MATCH_ID)+'.json'


#event data

import json
with open('E:/Docs/Data/Github/open-data/data/events/'+str(MATCH_ID)+'.json') as f:
    data = json.load(f)
from pandas.io.json import json_normalize
from pandas.io import json
match_events_df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])


#360 data

match_360_df = pd.read_json(f'E:/Docs/Data/Github/open-data/data/three-sixty/{MATCH_ID}.json')

#data integration into one central location

df = pd.merge(left=match_events_df, right=match_360_df, left_on='id', right_on='event_uuid', how='left')

#Displaying passes made by Spinazzola
player1_df = df[(df['player_name'] == 'Leonardo Spinazzola') & (df['type_name'] == 'Pass')].reset_index(drop=True)

player1_df[['x_start','y_start']] = pd.DataFrame(player1_df.location.tolist(), index=player1_df.index)
player1_df[['x_end','y_end']] = pd.DataFrame(player1_df.pass_end_location.tolist(), index=player1_df.index)

#figure
p = Pitch(pitch_type='statsbomb')
fig,ax = p.draw(figsize=(12,8))

player1_df = player1_df[50:51]

p.scatter(x=player1_df['x_start'],y=player1_df['y_start'],s=150, ax=ax)
p.lines(xstart=player1_df['x_start'],ystart=player1_df['y_start'],xend=player1_df['x_end'],yend=player1_df['y_end'], ax=ax, comet=True)

for x in player1_df.iloc[0]['freeze_frame']:
    if x['teammate']:
        color = 'blue'
    else :
        color = 'red'
        
    p.scatter(x=x['location'][0],y=x['location'][1],ax=ax,c=color,s=100)

#title
fig.text(
    0.515, 0.98, "Leonardo Spinazzola- Left back - ITALY", size=18,
    ha="center", color="#000000"
)

# add subtitle
player1_df['minute'] = pd.to_numeric(player1_df['minute'], errors='coerce') + 1
fig.text(
    0.515, 0.949,
    'Position of players during the pass against Austria at the minute of '+ player1_df['minute'].astype(str).str.cat(sep=', ')  +'"',
    size=15,
    ha="center", color="#000000"
)