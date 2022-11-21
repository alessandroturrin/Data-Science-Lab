import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from map_f import Map_c

os.system('clear')

def get_df_by_category(df, category):
    counts = df[category].value_counts()
    new_df = []
    for cell_id in range(400):
        type = df.loc[df['cell_id']==cell_id][category].value_counts()
        type.name = cell_id
        new_df.append(type)
    new_pd_df = pd.DataFrame(new_df)
    new_pd_df = new_pd_df.fillna(0)
    return new_pd_df

df = pd.read_csv('pois_all_info', delimiter='\t')
imgpath = 'New_York_City_Map.png'

columns = df.columns
poi = ['amenity', 'shop', 'public_transport', 'highway']

#1.2
count_na = {}
for c in columns:
    count_na[c] = df[c].isna().sum()
for c in columns:
    print(f"{c} : {count_na[c]}")

#1.3
map_categories = dict()
for c in poi:
    tmp_dict = dict()
    map_categories[c] = dict()
    tmp_dict = df.groupby(c).size().sort_values(ascending=False).to_dict()
    max_val = max(tmp_dict.values())
    for k,v in tmp_dict.items():
        if v>max_val*0.1:
            map_categories[c][k] = v 

print(len(map_categories[poi[0]]))


fig, ax = plt.subplots(nrows=2, ncols=2)
index = 0
for row in ax:
    for col in row:
        x = np.arange(len(map_categories[poi[index]]))
        col.bar(x, map_categories[poi[index]].values())
        col.set_title(poi[index])
        index += 1
plt.show()

#1.4
nyc_map = Map_c(imgpath, df)

#1.5
ax = nyc_map.split_map('shop')
df = nyc_map.get_pd_table()
plt.show()
print(df)

#1.6
new_pd_df = get_df_by_category(df, 'amenity')
print(new_pd_df)
