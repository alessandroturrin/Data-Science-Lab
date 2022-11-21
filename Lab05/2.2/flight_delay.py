import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

os.system('clear')

#2.1
df = pd.read_csv('831394006_T_ONTIME.csv')
#2.2
df.info()
df.describe()
#2.3
df = df.drop(df[df['CANCELLED']==1.0].index)
#2.4
flights_by_carrier = df[['UNIQUE_CARRIER','FL_NUM']].groupby(['UNIQUE_CARRIER']).count()
delay_list = ['UNIQUE_CARRIER', 'CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
mean_delay_df = df[delay_list].groupby('UNIQUE_CARRIER').mean()
#2.5
df['WEEKDAY'] = pd.to_datetime(df['FL_DATE'], format='%Y-%m-%d').dt.day_of_week
#2.6
df.boxplot(by='WEEKDAY', column='ARR_DELAY')
#plt.show()
#2.7
we = df.loc[df['WEEKDAY']>4].groupby(['UNIQUE_CARRIER']).ARR_DELAY.mean()
wd = df.loc[df['WEEKDAY']<=4].groupby(['UNIQUE_CARRIER']).ARR_DELAY.mean()
ax = pd.concat([we,wd], axis=1).plot.bar()
ax.grid()
#plt.show()
#2.8
mi_df = df.set_index(['UNIQUE_CARRIER','ORIGIN','DEST','FL_DATE'])
#2.9
res = mi_df.loc[(['AA', 'DL'], ['LAX']), ['DEP_TIME', 'DEP_DELAY']]
#2.10
#?
#2.11
pivot = pd.pivot_table(df, values='FL_NUM', index='UNIQUE_CARRIER', columns='WEEKDAY', aggfunc='count')
#2.12
pivot = pd.pivot_table(df, values='ARR_DELAY', index='UNIQUE_CARRIER', columns='WEEKDAY', aggfunc='mean')
#2.13
mask = df.UNIQUE_CARRIER.isin(["HA", "DL", "AA", "AS"])
df['DELTA_DELAY'] = df['ARR_DELAY']-df['DEP_DELAY']
pivot = pd.pivot_table(df.loc[mask], values='DELTA_DELAY', index='UNIQUE_CARRIER', columns='WEEKDAY', aggfunc='mean')
