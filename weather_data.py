import requests
import pandas as pd

class Data:
    def __init__(self):
        self.key = '147d1642a5254d08b7993928210201'

    def get_data(self,place,day):
        '''   {place : String, day : must be in range (1 - 3)}    '''
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.key}&q={place}&days={day}"
        data = requests.get(url).json()
        clear_data = data['forecast']['forecastday']
        path = "E:\Weather Boarcast [Python]\CSV"
        paths = []

        for i in range(day):
            day = clear_data[i]['date']
            # Add "Time" column from unclean time column "time"
            df = pd.DataFrame(clear_data[i]['hour'])
            time = df['time']
            Time = [str(t.split(' ')[1]) for t in time]
            df['Time'] = Time
            # Create csv files
            df.to_csv(f'{path}/Hour_day_{day}.csv')
            pd.DataFrame(clear_data[i]['day'],index=[0]).to_csv(f'{path}/Day_day_{day}.csv')
            pd.DataFrame(clear_data[i]['astro'],index=[0]).to_csv(f'{path}/Astro_day_{day}.csv')
            # append paths in paths
            paths.append(f'{path}/Hour_day_{day}.csv')
            paths.append(f'{path}/Day_day_{day}.csv')
            paths.append(f'{path}/Astro_day_{day}.csv')
        
        return paths

    def Current_Status(self,place):
        url = f'http://api.weatherapi.com/v1/current.json?key={self.key}&q={place}'
        data = requests.get(url).json()
        return data

if __name__ == '__main__':
    obj = Data()
    #print(obj.Current_Status('burdwan'))