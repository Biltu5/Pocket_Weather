from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from itertools import cycle
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import weather_data
import time

class app:
    '''
    Create full Frame of weather app
    '''
    def __init__(self,root,image):
        ###### Variables for Future uses ######
        self.root = root
        self.image = image

        self.obj = weather_data.Data()
        self.paths = self.obj.get_data('Delhi',3)
        day1_df = pd.read_csv(self.paths[1])
        day2_df = pd.read_csv(self.paths[4])
        day3_df = pd.read_csv(self.paths[7])
        self.df = pd.read_csv(self.paths[0])
        current = self.obj.Current_Status('Delhi')

        self.select_city = StringVar(value = 'Delhi')
        self.set_Date = StringVar(value=self.get_day())
        self.set_Time = StringVar()
        self.get_time()

        self.status = StringVar(value = f"Weather in {current['location']['name']}, {current['location']['region']}")
        self.current_temprature = StringVar(value = f"{current['current']['temp_c']}°C")
        self.current_weather = StringVar(value = f"{current['current']['condition']['text']}")
        self.current_pressure = StringVar(value = f"{current['current']['pressure_mb']} mb")
        self.current_humidity = StringVar(value = f"{current['current']['humidity']} %")
        self.current_wind_speed = StringVar(value = f"{current['current']['wind_kph']} kph")

        self.day1_day = StringVar(value = f" {time.strftime('%d')} {time.strftime('%b')}")
        self.day1_temp = StringVar(value = f"Temprature {day1_df['maxtemp_c'][0]}/{day1_df['mintemp_c'][0]} °C")
        self.day1_wind_speed = StringVar(value = f"Wind Speed {day1_df['maxwind_kph'][0]} km/h")
        self.day1_humidity = StringVar(value = f"Humidity {day1_df['avghumidity'][0]} %")

        self.day2_day = StringVar(value = f" {int(time.strftime('%d'))+1} {time.strftime('%b')}")
        self.day2_temp = StringVar(value = f"Temprature {day2_df['maxtemp_c'][0]}/{day1_df['mintemp_c'][0]} °C")
        self.day2_wind_speed = StringVar(value = f"Wind Speed {day2_df['maxwind_kph'][0]} km/h")
        self.day2_humidity = StringVar(value = f"Humidity {day2_df['avghumidity'][0]} %")

        self.day3_day = StringVar(value = f" {int(time.strftime('%d'))+2} {time.strftime('%b')}")
        self.day3_temp = StringVar(value = f"Temprature {day3_df['maxtemp_c'][0]}/{day1_df['mintemp_c'][0]} °C")
        self.day3_wind_speed = StringVar(value = f"Wind Speed {day3_df['maxwind_kph'][0]} km/h")
        self.day3_humidity = StringVar(value = f"Humidity {day3_df['avghumidity'][0]} %")

        self.First_Combo = StringVar()
        self.Second_Combo = StringVar()
        self.Graph_Type = StringVar(value = 'bar')

        bg_color = 'dodger blue'
        fg_color = 'ghost white'

        ###### Frame Section ######
        self.top_Frame_Left_up = Frame(root, bg = bg_color)
        self.top_Frame_Left_up.place(x=0,y=0,width = 1175,height=45)
        self.top_Frame_Left_down = Frame(root, bg = bg_color)
        self.top_Frame_Left_down.place(x=0,y=50,width = 1175,height=50)

        self.top_Frame_Right = Frame(root, bg = bg_color)
        self.top_Frame_Right.place(x=1180,y=0, height =100)

        self.left_Frame = Frame(root,bg=bg_color)
        self.left_Frame.place(x=0,y=105,height=490,width =200)

        self.Heading_Frame = Frame(root,bg = 'blue')
        self.Heading_Frame.place(x=205,y=105,height=40,width=1100)
        self.middle_Frame = Frame(root)
        self.middle_Frame.place(x=205,y=145,height=450,width =550)
        self.right_Frame = Frame(root, relief = GROOVE, bd = 5)
        self.right_Frame.place(x=755,y=145,height=375,width =550)
        self.Button_Frame = Frame(root,bg = bg_color)
        self.Button_Frame.place(x=755, y= 520,height = 75 ,width=550)

        ###### Top Frame Left ######
        Label(self.top_Frame_Left_up, text = 'WEATHER REPORT', font = ('algerian', 20, 'bold'), bg = bg_color, fg = fg_color).pack(fill = X)
        Label(self.top_Frame_Left_down, text = 'Search City :', font = ('georgia', 12), bg = bg_color, fg = fg_color).pack(side = LEFT, padx =20)
        Entry(self.top_Frame_Left_down, textvariable = self.select_city, width = 20, font = ('georgia', 12)).pack(side = LEFT, padx = 5)
        Button(self.top_Frame_Left_down, text = 'Search', font = ('georgia', 10),bg = 'Forest green', fg = fg_color, command = self.set_middle_frame_data).pack(side = LEFT,padx = 5)
        Label(self.top_Frame_Left_down,text = '',bg= bg_color).pack(side=LEFT,padx=70)
        Label(self.top_Frame_Left_down, textvariable = self.status, font = ('georgia', 16), bg = 'dodger blue2', fg = fg_color,anchor = E).pack(side = RIGHT)

        ###### Top Frame Right ######
        Label(self.top_Frame_Right, textvariable = self.set_Date,font = ('century', 12, 'bold'), bg = bg_color, fg = fg_color).pack(pady =5, padx = 5)
        Label(self.top_Frame_Right, textvariable = self.set_Time,font = ('century', 11), bg = bg_color, fg = fg_color).pack(pady = 5, padx = 5)

        ###### Heding Frame ######
        Label(self.Heading_Frame,text = "Reports",font = ('georgia', 15), bg = 'blue', fg = fg_color).pack(fill = BOTH)

        ###### Middle Frame ######
        no = randint(1,8)
        self.change_image(image[f'bg{no}'])

        self.Temp_Frame = Frame(self.middle_Frame, bg = 'white')
        self.Temp_Frame.place(x = 10,y = 340,height = 100,width = 100)
        self.wind_Frame = Frame(self.middle_Frame, bg = 'white')
        self.wind_Frame.place(x = 115,y = 340,height = 100,width = 100)
        self.Fell_Frame = Frame(self.middle_Frame, bg = 'white')
        self.Fell_Frame.place(x = 220,y = 340,height = 100,width = 100)
        self.Rain_Frame = Frame(self.middle_Frame, bg = 'white')
        self.Rain_Frame.place(x = 325,y = 340,height = 100,width = 100)
        self.pressure_Frame = Frame(self.middle_Frame, bg = 'white')
        self.pressure_Frame.place(x = 430,y = 340,height = 100,width = 100)

        Label(self.Temp_Frame,image = image['thermometer']).pack(pady = 5)
        Label(self.Temp_Frame,textvariable=self.current_temprature,  font = "arial 14", bg = 'white').pack()
        Label(self.Fell_Frame,image = image['FellsLike']).pack()
        Label(self.Fell_Frame,textvariable=self.current_weather,  font = "arial 12", bg = 'white').pack(pady = 5)
        Label(self.wind_Frame,image = image['wind']).pack()
        Label(self.wind_Frame,textvariable=self.current_wind_speed,  font = "arial 14", bg = 'white').pack(pady = 5)
        Label(self.Rain_Frame,image = image['rain']).pack()
        Label(self.Rain_Frame,textvariable=self.current_humidity,  font = "arial 14", bg = 'white').pack(pady = 5)
        Label(self.pressure_Frame,image = image['pressure']).pack()
        Label(self.pressure_Frame,textvariable=self.current_pressure,  font = "arial 14", bg = 'white').pack(pady = 5)

        ###### Left Frame ######
        Label(self.left_Frame, text = '3 - Day Weather', font = "georgia 15 bold",fg = fg_color, bg = 'blue').pack(fill = X)

        self.Today_Frame = Frame(self.left_Frame, bg = 'white')
        self.Today_Frame.place(x = 10, y = 50, height = 135, width =180)
        self.Second_day_Frame = Frame(self.left_Frame, bg = 'white')
        self.Second_day_Frame.place(x = 10, y = 195, height = 135, width =180)
        self.Third_day_Frame = Frame(self.left_Frame, bg = 'white')
        self.Third_day_Frame.place(x = 10, y = 340, height = 135, width =180)

        Label(self.Today_Frame,textvariable=self.day1_day,  font = "arial 12", bg = 'white').pack(pady = 5)
        Label(self.Today_Frame,textvariable=self.day1_temp,  font = "arial 10", bg = 'white').pack(pady = 5)
        Label(self.Today_Frame,textvariable=self.day1_wind_speed,  font = "arial 10", bg = 'white').pack(pady = 5)
        Label(self.Today_Frame,textvariable=self.day1_humidity,  font = "arial 10", bg = 'white').pack(pady = 5)

        Label(self.Second_day_Frame,textvariable=self.day2_day,  font = "arial 12", bg = 'white').pack(pady = 5)
        Label(self.Second_day_Frame,textvariable=self.day2_temp,  font = "arial 10", bg = 'white').pack(pady = 5)
        Label(self.Second_day_Frame,textvariable=self.day2_wind_speed,  font = "arial 10", bg = 'white').pack(pady = 5)
        Label(self.Second_day_Frame,textvariable=self.day2_humidity,  font = "arial 10", bg = 'white').pack(pady = 5)

        Label(self.Third_day_Frame,textvariable=self.day3_day,  font = "arial 12", bg = 'white').pack(pady = 5)
        Label(self.Third_day_Frame,textvariable=self.day3_temp,  font = "arial 10", bg = 'white').pack(pady = 5)
        Label(self.Third_day_Frame,textvariable=self.day3_wind_speed,  font = "arial 10", bg = 'white').pack(pady = 5)
        Label(self.Third_day_Frame,textvariable=self.day3_humidity,  font = "arial 10", bg = 'white').pack(pady = 5)

        ###### Right Frame ######
        self.graph = Label(self.right_Frame)
        self.graph.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.graph_plot(self.df)

        ###### Right Cornaer Frame #####
        Label(self.Button_Frame,text = 'X Axis :').place(x=10,y=10)
        X_choosen = ttk.Combobox(self.Button_Frame, width = 10, textvariable = self.First_Combo)
        X_choosen['values'] = ('Time')
        X_choosen.place(x=70,y=10)
        Label(self.Button_Frame,text = 'Y Axis :').place(x=10,y=40)
        Y_choosen = ttk.Combobox(self.Button_Frame, width = 10, textvariable = self.Second_Combo)
        Y_choosen['values'] = ('Temperature','Humidity','Pressure','Wind Speed')
        Y_choosen.place(x=70,y=40)
        Button(self.Button_Frame,text='Show Graph',bg = 'forest green',fg = 'ghost white', command = self.graph_fun).place(x=170,y = 10)
        Button(self.Button_Frame,text='Change Graph',bg = 'forest green',fg = 'ghost white', command = self.set_graph_type).place(x=270,y = 10)

    '''
    Set a new image in middle frame background
    '''
    def change_image(self,img):
        bg_Label = Label(self.middle_Frame,image=img)
        bg_Label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        bg_Label.image = img

    '''
    Return the current time
    '''
    def get_time(self):
        self.hours=time.strftime("%I")
        self.minute=time.strftime("%M")
        self.second=time.strftime("%S")
        self.am_pm=time.strftime("%p")
        self.set_Time.set(self.hours+" : "+self.minute+" : "+self.second+" "+self.am_pm)
        self.root.after(1000,self.get_time)

    '''
    Return today's date
    '''
    def get_day(self):
        self.day=time.strftime("%d")
        self.mounth=time.strftime("%b")
        self.year=time.strftime("%Y")
        return (self.day+" "+self.mounth+",  "+self.year)
    
    '''
    Set new data into left frame when user click search button
    '''
    def set_left_frame_data(self):
        self.obj = weather_data.Data()
        self.paths = self.obj.get_data(self.select_city.get(),3)
        day1_df = pd.read_csv(self.paths[1])
        day2_df = pd.read_csv(self.paths[4])
        day3_df = pd.read_csv(self.paths[7])
        self.df = pd.read_csv(self.paths[0])

        self.day1_day.set(f" {time.strftime('%d')} {time.strftime('%b')}")
        self.day1_temp.set(f"Temprature {day1_df['maxtemp_c'][0]}/{day1_df['mintemp_c'][0]} °C")
        self.day1_wind_speed.set(f"Wind Speed {day1_df['maxwind_kph'][0]} km/h")
        self.day1_humidity.set(f"Humidity {day1_df['avghumidity'][0]} %")

        self.day2_day.set(f" {int(time.strftime('%d'))+1} {time.strftime('%b')}")
        self.day2_temp.set(f"Temprature {day2_df['maxtemp_c'][0]}/{day1_df['mintemp_c'][0]} °C")
        self.day2_wind_speed.set(f"Wind Speed {day2_df['maxwind_kph'][0]} km/h")
        self.day2_humidity.set(f"Humidity {day2_df['avghumidity'][0]} %")

        self.day3_day.set(f" {int(time.strftime('%d'))+2} {time.strftime('%b')}")
        self.day3_temp.set(f"Temprature {day3_df['maxtemp_c'][0]}/{day1_df['mintemp_c'][0]} °C")
        self.day3_wind_speed.set(f"Wind Speed {day3_df['maxwind_kph'][0]} km/h")
        self.day3_humidity.set(f"Humidity {day3_df['avghumidity'][0]} %")
    
    '''
    Set new data into middle frame when user click search button
    '''
    def set_middle_frame_data(self):
        city = self.select_city.get()
        if city:
            obj = weather_data.Data()
            current = obj.Current_Status(city)
            self.status.set(f"Weather in {current['location']['name']}, {current['location']['region']}")
            self.current_temprature.set(f"{current['current']['temp_c']}°C")
            self.current_weather.set(f"{current['current']['condition']['text']}")
            self.current_pressure.set(f"{current['current']['pressure_mb']} mb")
            self.current_humidity.set(f"{current['current']['humidity']} %")
            self.current_wind_speed.set(f"{current['current']['wind_kph']} kph")
            self.set_left_frame_data()
            self.graph_fun()

    '''
    function to show graph on right frame
    '''
    def graph_fun(self):
        # get current place search by user or default : Delhi
        place = self.select_city.get()
        # Create object of Data Class
        self.obj = weather_data.Data()
        # create csv files and store the path in current data
        currennt_data = self.obj.get_data(place,1)
        self.df = pd.read_csv(currennt_data[0])
        # get X axis and Y axis
        x = self.First_Combo.get()
        y = self.Second_Combo.get()

        if x and y :
            if y == 'Temperature':
                self.graph_plot(self.df,y = 'temp_c', y_label = 'Temparature')
            elif y == 'Humidity':
                self.graph_plot(self.df,y = 'humidity', y_label = 'Humidity')
            elif y == 'Pressure':
                self.graph_plot(self.df,y = 'pressure_mb', y_label = 'Pressure')
            elif y == 'Wind Speed':
                self.graph_plot(self.df,y = 'wind_kph', y_label = 'Wind Speed')
            else:
                pass
        else:
            self.graph_plot(self.df)

    '''
    function to draw bar & line graph
    '''
    def graph_plot(self,df,x = 'Time',y = 'temp_c', y_label = 'Temparature'):
        place = self.select_city.get()
        plt.figure(figsize=(14,8))
        # Select Figure type
        fig = sns.barplot(x,y,data = df) if self.Graph_Type.get() == 'bar' else sns.lineplot(x, y, data = df) 
        # Set Figure Title
        plt.title(f"Today's {place} {y_label}",fontsize = 20)
        # Set X-axis Label
        plt.xlabel('Time', fontsize = 15)
        # Set Y-axis Label
        plt.ylabel(y_label,fontsize = 15)
        # Save Figure into memory
        fig.figure.savefig("E:\\Weather Boarcast [Python]\\Fig\\bar.jpg")
        # Display Image into window
        self.image['bar'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Fig\\bar.jpg").resize((650,375)))
        self.graph.config(image = self.image['bar'])
    
    ''' 
    Set Graph type
    '''
    def set_graph_type(self):
        choice = 'line' if self.Graph_Type.get() == 'bar' else 'bar'
        self.Graph_Type.set(choice)
        self.graph_fun()

if __name__ == '__main__':
    root = Tk()
    root.geometry('1310x600+20+40')
    root.resizable(False,False)
    image = {}

    # Add Background image files
    for i in range(1,9):
        image[f'bg{i}'] = ImageTk.PhotoImage(Image.open(f"E:\\Weather Boarcast [Python]\\Images\\bg{i}.jpg").resize((550,450)))
    
    # Add icon image files
    image['pressure'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Images\\icon\\atmospheric_pressure.png").resize((50,50)))
    image['rain'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Images\\icon\\rain.png").resize((50,50)))
    image['FellsLike'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Images\\icon\\FellsLike.png").resize((50,50)))
    image['wind'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Images\\icon\\windy_weather.png").resize((50,50)))
    image['thermometer'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Images\\icon\\thermometer.png").resize((50,50)))
    image['icon'] = ImageTk.PhotoImage(Image.open("E:\\Weather Boarcast [Python]\\Images\\Weather.png").resize((50,50)))

    #root.wm_iconbitmap("Images\\weather.ico")
    icon = PhotoImage(file = "E:\\Weather Boarcast [Python]\\Images\\Weather.png")
    root.iconphoto(False, icon)
    root.title("Weather - By B Nayak")
    obj = app(root,image)
    root.after(1000,obj.get_time)
    root.mainloop()

