import numpy as np
import matplotlib.pyplot as plt

class Map_c:
    def __init__(self, imgpath, df):
        self.imgpath = imgpath
        self.df = df
        self.lat_min = df['@lat'].min()
        self.lat_max = df['@lat'].max()
        self.long_min = df['@lon'].min()
        self.long_max = df['@lon'].max()
        self.df = self.df.dropna(subset=['@lat', '@lon'])

    def plot_map(self, category):
        fig, ax = plt.subplots()
        values = self.df.dropna(subset=category)
        lon = values['@lon'].dropna()
        lat = values['@lat'].dropna()

        img_map = plt.imread(self.imgpath)
        ax.imshow(img_map, zorder=0, extent=[self.long_min, self.long_max, self.lat_min, self.lat_max])
        ax.scatter(lon, lat, s=1)
        return ax

    def split_map(self, category):
        ax = self.plot_map(category)
        lat_space = np.linspace(self.lat_min, self.lat_max, 21)
        lon_space = np.linspace(self.long_min, self.long_max, 21)
        ax.hlines(lat_space, self.long_min, self.long_max)
        ax.vlines(lon_space, self.lat_min, self.lat_max)
        return ax

    def cell_id(self, long, lat):
        x = int((long - self.long_min)/(self.long_max - self.long_min)*20)
        y = int((lat - self.lat_min)/(self.lat_max - self.lat_min)*20)
        return y * 20 + x

    def get_pd_table(self):
        self.df['cell_id'] = self.df.apply(lambda x: self.cell_id(x['@lon'], x['@lat']), axis=1)
        return self.df



    
        