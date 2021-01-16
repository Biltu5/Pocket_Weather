import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

key = '147d1642a5254d08b7993928210201'
url1 = 'http://api.weatherapi.com/v1/current.json?key=147d1642a5254d08b7993928210201&q=London' #Current
url2 = "http://api.weatherapi.com/v1/forecast.json?key=147d1642a5254d08b7993928210201&q=burdwan&days=1" # for 1 days
url3 = "http://api.weatherapi.com/v1/timezone.json?key=147d1642a5254d08b7993928210201&q=burdwan" #Time zone
url4 = "http://api.weatherapi.com/v1/astronomy.json?key=147d1642a5254d08b7993928210201&q=burdwan&dt=2021-01-02" #Astronomy
url5 = "http://api.weatherapi.com/v1/sports.json?key=147d1642a5254d08b7993928210201&q=burdwan" # sports

data = requests.get(url1).json()
data1 = requests.get(url2).json()
#df = pd.DataFrame(data1)
data = {'location': {'name': 'London', 'region': 'City of London, Greater London', 'country': 'United Kingdom', 
        'lat': 51.52, 'lon': -0.11, 'tz_id': 'Europe/London', 'localtime_epoch': 1610023834,
        'localtime': '2021-01-07 12:50'}, 'current': {'last_updated_epoch': 1610022611, 'last_updated': '2021-01-07 12:30',
         'temp_c': 3.0, 'temp_f': 37.4, 'is_day': 1, 'condition': {'text': 'Sunny', 
         'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 6.9, 'wind_kph': 11.2, 
         'wind_degree': 270, 'wind_dir': 'W', 'pressure_mb': 1018.0, 'pressure_in': 30.5, 'precip_mm': 0.0,
         'precip_in': 0.0, 'humidity': 75, 'cloud': 0, 'feelslike_c': 0.6, 'feelslike_f': 33.1, 'vis_km': 10.0,
         'vis_miles': 6.0, 'uv': 2.0, 'gust_mph': 7.4, 'gust_kph': 11.9}}
#print(data)

# Clean some data
# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
# df = pd.DataFrame(data5[0]['hour'])
# time = df['time']
# Time = [str(t.split(' ')[1]) for t in time]
# df['Time'] = Time

def lineplot():
        plt.figure(figsize=(14,8))
        sns.lineplot('Time','wind_kph',data=df,label="Wind Speed (kph)")
        sns.lineplot('Time','humidity',data=df,label="Humidity")
        sns.lineplot('Time','feelslike_c',data=df,label="Fells Like (C)")
        sns.lineplot('Time','temp_c',data=df,label="Temperature (C)")
        plt.title('Burdwan Temparature')
        plt.xlabel('Time')
        plt.ylabel('Temparature , Wind Speed ,Humidity')
        plt.show()

def scatterplot():
        plt.figure(figsize=(14,8))
        sns.scatterplot('Time','temp_c',data=df)
        plt.title('Burdwan Temparature')
        plt.xlabel('Time')
        plt.ylabel('Temparature')
        plt.show()

def barplot():
        plt.figure(figsize=(14,8))
        sns.barplot('Time','temp_c',data=df)
        plt.title('Burdwan Temparature')
        plt.xlabel('Time')
        plt.ylabel('Temparature')
        plt.show()


