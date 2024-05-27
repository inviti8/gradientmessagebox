"""A Simple tkinter prompt window with a settable image background window, By: Fibo Metavinci"""

__version__ = "0.01"

import threading
import tkinter
from tkinter import font
from PIL import Image, ImageTk
import sys
import time
from colour import Color


class GradientFrame(tkinter.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="red", color2="black", saturation=1.0, direct='+x', **kwargs):
        tkinter.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self._saturation = saturation
        self._direct = direct
        self._midColor = None
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        if 'y' in self._direct:
            limit = height

        print('limit')
        print(limit)

        colors = list(Color(self._color1).range_to(Color(self._color2), limit))

        if '-' in self._direct:
            c1 = self._color1
            c2 = self._color2
            c1.saturation = self._saturation
            c2.saturation = self._saturation
            colors = list(c1.range_to(c2, limit))

        for i in range(limit):
            color = "%s" % colors[i]
            if 'y' in self._direct:
                self.create_line(0,i,width,i, tags=("gradient",), fill=color)
            else:
                self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

class Config:
    def __init__(self, width=250, height=300):
        self.width = width
        self.height = height
        self.font = ('Fira Sans', 12)

class ColorConfig(Config):
    def __init__(self, width=250, height=300, color1="#00ffff", color2="#ffa500", alpha=1.0, saturation=1.0, direct='+x', hasframe=True, widgetSaturation=1.0, widgetLuminance=0.5):
        Config.__init__(self, width, height)
        self.color1 = Color(color1)
        self.color2 = Color(color2)
        self.alpha = alpha
        self.saturation = saturation
        self.direct = direct
        self.hasframe = hasframe
        self.widgetSaturation = widgetSaturation
        self.widgetLuminance = widgetLuminance

class ImageConfig(ColorConfig):
    def __init__(self, width, height, color1, color2, alpha, direct, hasframe, path):
        ColorConfig.__init__(self, width, height, color1, color2, alpha, direct, hasframe)
        self.path = path
        self.file = Image.open(self.path)
        self.width, self.height = self.file.size


class BaseWindow:
    def __init__(self, config):
        self.path = None
        self.img = None
        self.hasImg = False
        self.width = config.width
        self.height = config.height
        self.color1 = config.color1
        self.color2 = config.color2
        self.saturation = config.saturation
        limit = self.width
        if 'y' in config.direct:
            limit = self.height
        
        colors = list(Color(self.color1).range_to(Color(self.color2), limit))
        self.midColor = colors[int(len(colors)/2)]
        self.fg = Color(self.color1.hex_l)
        self.bg = Color(self.color2.hex_l)
        self.alpha = config.alpha
        self.direct = config.direct
        self.hasframe = config.hasframe
        self.widgetSaturation = config.widgetSaturation
        self.widgetLuminance = config.widgetLuminance
        self.midColor.saturation = self.widgetSaturation
        if self.widgetLuminance != 0.5:
            self.midColor.luminance = self.widgetLuminance

        if hasattr(config, 'file'):
            self.file = config.file
            self.path = config.path
            self.hasImg = True

        self.root = None
        self.canvas = None
        self.bg = None

    def _center_window(self, win):
        win.wait_visibility() # make sure the window is ready
        x = ((win.winfo_screenwidth()//2) - (win.winfo_width())) // 2
        y = (win.winfo_screenheight() - (win.winfo_height())) // 2
        win.geometry(f'+{x}+{y}')

    def _Show(self):
        self.root = tkinter.Tk()
        self.root.withdraw()
        self.window = tkinter.Toplevel(width=self.width, height=self.height)

        if not self.hasframe:
            self.window.overrideredirect(True)

        self._center_window(self.window)
        self.canvas = GradientFrame(self.window, self.color1, self.color2, self.saturation, self.direct, width=self.width, height=self.height, bd=0,
                   highlightthickness=0, relief="ridge")
        self.canvas.pack(expand=True, fill='both')

        if self.hasImg:
            self.img = tkinter.PhotoImage(file=self.path, format='png')
            self.canvas.create_image(self.width/2, self.height/2, image=self.img)

        self.window.wm_attributes("-alpha", self.alpha)
        


class ChoiceWindow(BaseWindow):
    def __init__(self, config):
        BaseWindow.__init__(self, config)
    def Show(self):
        self._Show()

        bg_fill = self.color1.hex_l
        fg_fill = self.color2.hex_l

        self.canvas.grid_anchor(anchor='center')
        #l1 = tkinter.Label(self.canvas, text="Hello, world", width=int(self.width*0.1))
        #l1.place(x = 1, rely = 0, relheight = 0.3, relwidth = 0.7)
        e1 = tkinter.Entry(self.canvas, bg=bg_fill,fg=fg_fill,  bd=0, highlightthickness=0, font=('Fira Sans', 12))
        t1 = tkinter.Text(self.canvas, bg=bg_fill, fg=fg_fill, bd=0, highlightthickness=0, font=('Fira Sans', 12))

        # listnumber = 1
        # for item in self.fonts:
        #     label = "listlabel" + str(listnumber)
        #     label = tkinter.Label(self.canvas,text=item,font=(item, 16)).pack()
        #     listnumber += 1

        #t1.place(x = self.width/2-((self.width/2)*0.7), rely = 0.1, relheight = 0.3, relwidth = 0.7)

        #l1.grid(row=0, column=0, sticky="ew", padx=60, pady=10)
        e1.grid(row=1, column=0, sticky="ew", padx=60, pady=10)
        t1.grid(row=2, column=0, sticky="nsew", padx=60, pady=10)

        self.canvas.grid_rowconfigure(2, weight=1)
        self.canvas.grid_columnconfigure(2, weight=1)
        # widget = tkinter.Label(self.canvas, text='Spam', fg='white', bg='black')
        # widget.pack()
        # self.canvas.create_window(self.width/2, self.height/2, window=widget)
        self.root.mainloop()


