import json
from unicodedata import name
import os
from math import cos, acos, sin
import sys

class CityBike:
    def __init__(self, obj) -> None:
        self.object = obj


    def active_stations(self):
        online_counter = 0
        for object in self.object['network']['stations']:
            for k, v in object['extra'].items():
                if k=="status" and v=="online":
                    online_counter+=1
        print(f"Online stations: {online_counter}")


    def count_free_bikes(self):
        free_bikes_counter = 0
        for main_list in self.object['network']['stations']:
            for k, v in main_list.items():
                if k=="free_bikes":
                    free_bikes_counter+=int(v)
        print(f"Free bikes: {free_bikes_counter}")


    def distance_coords(self, lat1, lng1, lat2, lng2):
        deg2rad = lambda x: x * 3.141592 / 180
        lat1, lng1, lat2, lng2 = map(deg2rad, [ lat1, lng1, lat2, lng2 ]) 
        R = 6378100 
        return R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))
    

    def closest_bike_station(self, lat, lon):
        min_distance = sys.float_info.max
        for stations in self.object['network']['stations']:
            for k, v in stations.items():
                if k=="free_bikes":
                    free_bikes = int(v)
                if k=="latitude":
                    latitude = float(v)
                if k=="longitude":
                    longitude = float(v)
                if k=="name":
                    name= v
            distance = self.distance_coords(latitude,longitude,lat,lon)
            if distance<min_distance and free_bikes>0:
                min_distance = distance
                min_free_bikes = free_bikes
                min_name = name 
        
        print(f"Closest bike station is '{min_name}' with {min_free_bikes} available bike(s) " + '{:2f}'.format(min_distance) + " meters away from your position")
        

if __name__=='__main__':
    os.system('clear')
    with open("CityBike.json") as cityBike_file:
        obj = json.load(cityBike_file)
    cityBike_file.close()

    city_bike = CityBike(obj)

    city_bike.active_stations()
    city_bike.count_free_bikes()
    city_bike.closest_bike_station(45.074512,7.694419)
    