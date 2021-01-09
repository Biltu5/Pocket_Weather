from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import weather_data
from itertools import cycle
from random import randint
import time

class app:
    '''
    Create full Frame of weather app
    '''
    def __init__(self,root,image):
        ###### Variables for Future uses ######
        self.root = root
        self.image = image
        obj = weather_data.Data()
        #obj.get_data('Delhi',3)
        current = obj.Current_Status('Delhi')

        self.select_city = StringVar()
        self.set_Date = StringVar(value=self.get_day())
        self.set_Time = StringVar(value=self.get_time())

        self.status = StringVar(value = f"Weather in {current['location']['name']}, {current['location']['region']}")
        self.current_temprature = StringVar(value = f"{current['current']['temp_c']}°C")
        self.current_weather = StringVar(value = f"{current['current']['condition']['text']}")
        self.current_pressure = StringVar(value = f"{current['current']['pressure_mb']} mb")
        self.current_humidity = StringVar(value = f"{current['current']['humidity']} %")
        self.current_wind_speed = StringVar(value = f"{current['current']['wind_kph']} kph")

        self.First_Combo = StringVar()
        self.Second_Combo = StringVar()

        bg_color = 'dodger blue'
        fg_color = 'ghost white'

        ###### Frame Section ######
        self.top_Frame_Left_up = Frame(root, bg = bg_color)
        self.top_Frame_Left_up.place(x=0,y=0,width = 905,height=45)
        self.top_Frame_Left_down = Frame(root, bg = bg_color)
        self.top_Frame_Left_down.place(x=0,y=50,width = 905,height=50)

        self.top_Frame_Right = Frame(root, bg = bg_color)
        self.top_Frame_Right.place(x=910,y=0, height =100)

        self.left_Frame = Frame(root,bg=bg_color)
        self.left_Frame.place(x=0,y=105,height=490,width =200)

        self.Heading_Frame = Frame(root,bg = 'blue')
        self.Heading_Frame.place(x=205,y=105,height=40,width=840)
        self.middle_Frame = Frame(root)
        self.middle_Frame.place(x=205,y=145,height=450,width =550)
        self.right_Frame = Frame(root,bg = 'green')
        self.right_Frame.place(x=755,y=145,height=375,width =290)
        self.Button_Frame = Frame(root,bg = bg_color)
        self.Button_Frame.place(x=755, y= 520,height = 75 ,width=290)

        ###### Top Frame Left ######
        Label(self.top_Frame_Left_up, text = 'WEATHER REPORT', font = ('algerian', 20, 'bold'), bg = bg_color, fg = fg_color).pack(fill = X)
        Label(self.top_Frame_Left_down, text = 'Search City :', font = ('georgia', 12), bg = bg_color, fg = fg_color).pack(side = LEFT, padx =20)
        Entry(self.top_Frame_Left_down, textvariable = self.select_city, width = 20, font = ('georgia', 12)).pack(side = LEFT, padx = 5)
        Button(self.top_Frame_Left_down, text = 'Search', font = ('georgia', 10),bg = 'Forest green', fg = fg_color).pack(side = LEFT,padx = 5)
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
        ###### Right Frame ######
        ###### Right Cornaer Frame #####
        Label(self.Button_Frame,text = 'X Axis :').place(x=10,y=10)
        X_choosen = ttk.Combobox(self.Button_Frame, width = 10, textvariable = self.First_Combo)
        X_choosen['values'] = ('Time')
        X_choosen.place(x=70,y=10)
        Label(self.Button_Frame,text = 'Y Axis :').place(x=10,y=40)
        Y_choosen = ttk.Combobox(self.Button_Frame, width = 10, textvariable = self.Second_Combo)
        Y_choosen['values'] = ('Temperature','Humidity','Pressure','Wind Speed')
        Y_choosen.place(x=70,y=40)
        Button(self.Button_Frame,text='Show Graph',bg = 'forest green',fg = 'ghost white').place(x=170,y = 10)

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
        return (self.hours+" : "+self.minute+" : "+self.second+" "+self.am_pm)

    '''
    Return today's date
    '''
    def get_day(self):
        self.day=time.strftime("%d")
        self.mounth=time.strftime("%b")
        self.year=time.strftime("%Y")
        return (self.day+" "+self.mounth+",  "+self.year)

if __name__ == '__main__':
    root = Tk()
    root.geometry('1050x600+200+40')
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
    print(obj.__doc__)
    root.mainloop()

