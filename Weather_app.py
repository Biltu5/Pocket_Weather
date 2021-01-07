from tkinter import *
from PIL import ImageTk,Image
import weather_data
from itertools import cycle
from random import randint

class app:
    '''
    Create full Frame of weather app
    '''
    def __init__(self,root,image):
        ###### Variable Declaration ######
        self.root = root
        self.image = image
        obj = weather_data.Data()
        #obj.get_data('Delhi',3)
        current = obj.Current_Status('Delhi')

        self.status = StringVar(value = "Weather in Delhi")
        self.select_city = StringVar()
        self.set_Date = StringVar(value = " 06 JAN,  2021")
        self.set_Time = StringVar(value = " 06.30.43 PM")

        self.country_name = f"{current['location']['name']}, {current['location']['region']}"
        self.temprature = f"{current['current']['temp_c']}°C"
        self.current_weather = f"{current['current']['condition']['text']}"

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
        self.middle_Frame = Frame(root,bg = bg_color)
        self.middle_Frame.place(x=205,y=145,height=450,width =550)
        self.right_Frame =Frame(root,bg = 'green')
        self.right_Frame.place(x=755,y=145,height=375,width =290)

        ###### Top Frame Left ######
        Label(self.top_Frame_Left_up, text = 'WEATHER REPORT', font = ('algerian', 20, 'bold'), bg = bg_color, fg = fg_color).pack(fill = X)
        Label(self.top_Frame_Left_down, text = 'Search City :', font = ('georgia', 12), bg = bg_color, fg = fg_color).pack(side = LEFT, padx =20)
        Entry(self.top_Frame_Left_down, textvariable = self.select_city, width = 20, font = ('georgia', 12)).pack(side = LEFT, padx = 5)
        Button(self.top_Frame_Left_down, text = 'Search', font = ('georgia', 10),bg = 'Forest green', fg = fg_color).pack(side = LEFT,padx = 5)
        Label(self.top_Frame_Left_down,text = '',bg= bg_color).pack(side=LEFT,padx=70)
        Label(self.top_Frame_Left_down, textvariable = self.status, font = ('georgia', 16), bg = 'dodger blue2', fg = fg_color,anchor = E).pack(side = RIGHT)

        ###### Top Frame Right ######
        Label(self.top_Frame_Right, textvariable = self.set_Date,font = ('century', 12, 'bold'), bg = bg_color, fg = fg_color).pack(pady =5, padx = 5)
        Label(self.top_Frame_Right, textvariable = self.set_Time,font = ('century', 12), bg = bg_color, fg = fg_color).pack(pady = 5, padx = 5)

        ###### Heding Frame ######
        Label(self.Heading_Frame,text = "Reports",font = ('georgia', 15, 'bold'), bg = 'blue', fg = fg_color).pack(fill = BOTH)

        ###### Middle Frame ######
        #Label(self.middle_Frame,textvariable=self.country_name).pack()
        no = randint(1,8)
        self.change_image(image[f'bg{no}'])

    def change_image(self,img):
        bg_Label = Label(self.middle_Frame,image=img)
        bg_Label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        bg_Label.image = img

if __name__ == '__main__':
    root = Tk()
    root.geometry('1050x600+200+40')
    root.resizable(False,False)
    image = {}
    for i in range(1,9):
        image[f'bg{i}'] = ImageTk.PhotoImage(Image.open(f"E:\\Weather Boarcast [Python]\\Images\\bg{i}.jpg").resize((550,450)))
    #root.wm_iconbitmap("weather.ico")
    root.title("Weather - By B Nayak")
    obj = app(root,image)
    print(obj.__doc__)
    root.mainloop()

