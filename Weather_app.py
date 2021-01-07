from tkinter import *
import weather_data

class app:
    '''
    Create full Frame of weather app
    '''
    def __init__(self,root):
         ###### Variable Declaration ######
        self.status = StringVar(value = "Weather in Modha Prodesh")
        self.current_city = StringVar()
        self.set_Date = StringVar(value = " 06 JAN,  2021")
        self.set_Time = StringVar(value = " 06.30.43 PM")
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
        self.left_Frame.place(x=0,y=105,height=495,width =200)
        self.right_Frame = Frame(root,bg = bg_color)
        self.right_Frame.place(x=205,y=105,height=495,width =550)
        self.graph_Frame =Frame(root,bg = bg_color)
        self.graph_Frame.place(x=760,y=105,height=375,width =285)

        ###### Top Frame Left ######
        Label(self.top_Frame_Left_up, text = 'WEATHER REPORT', font = ('algerian', 20, 'bold'), bg = bg_color, fg = fg_color).pack(fill = X)
        Label(self.top_Frame_Left_down, text = 'Search City :', font = ('georgia', 12), bg = bg_color, fg = fg_color).pack(side = LEFT, padx =20)
        Entry(self.top_Frame_Left_down, textvariable = self.current_city, width = 20, font = ('georgia', 12)).pack(side = LEFT, padx = 5)
        Button(self.top_Frame_Left_down, text = 'Search', font = ('georgia', 10),bg = 'Forest green', fg = fg_color).pack(side = LEFT,padx = 5)
        Label(self.top_Frame_Left_down,text = '',bg= bg_color).pack(side=LEFT,padx=70)
        Label(self.top_Frame_Left_down, textvariable = self.status, font = ('georgia', 16), bg = 'dodger blue2', fg = fg_color,anchor = E).pack(side = RIGHT)

        ###### Top Frame Right ######
        Label(self.top_Frame_Right, textvariable = self.set_Date,font = ('century', 12, 'bold'), bg = bg_color, fg = fg_color).pack(pady =5, padx = 5)
        Label(self.top_Frame_Right, textvariable = self.set_Time,font = ('century', 12), bg = bg_color, fg = fg_color).pack(pady = 5, padx = 5)

if __name__ == '__main__':
    root = Tk()
    root.geometry('1050x600+200+40')
    root.resizable(False,False)
    #root.wm_iconbitmap("weather.ico")
    root.title("Weather - By B Nayak")
    obj = app(root)
    print(obj.__doc__)
    root.mainloop()

