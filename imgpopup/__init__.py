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
    def __init__(self, parent, color1="red", color2="black", direct='+x', animated=False, speed=50, stretch=2, **kwargs):
        tkinter.Canvas.__init__(self, parent, **kwargs)
        self._width = kwargs.get('width')
        self._height = kwargs.get('height')
        self._color1 = color1
        self._color2 = color2
        self._animated = animated
        self._direct = direct
        self._midColor = None
        self._limit = self._width
        self._active = False
        self._speed = speed
        self._stretch = stretch
        if 'y' in self._direct:
            self._limit = self._height

        self.colors = list(Color(self._color1).range_to(Color(self._color2), self._limit))
        if '-' in self._direct:
            c1 = self._color2
            c2 = self._color1

            self.colors = list(c1.range_to(c2, self._limit))

        if self._animated:
            self._thread = threading.Thread(target=self.Animate)
            self._thread.setDaemon(True)
            self._draw_gradient()
            self._active = True
            self.Play()
        else:
            self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")

        for i in range(self._limit):
            color = "%s" % self.colors[i]
            if 'y' in self._direct:
                self.create_line(0,i,self._width,i, tags=("gradient",), fill=color)
            else:
                self.create_line(i,0,i,self._height, tags=("gradient",), fill=color)
        self.lower("gradient")

    def Stop(self):
        self._active = False

    def Play(self):
        c1 = self._color1
        c2 = self._color2
        if '-' in self._direct:
            c1 = self._color2
            c2 = self._color1

        colors1 = list(c1.range_to(c2, int(self._limit*self._stretch)))
        colors2 = list(c2.range_to(c1, int(self._limit*self._stretch)))

        self.colors = colors1+colors2
        self._thread.start()

    def Animate(self):
        if self._active:
            self.colors.append(self.colors.pop(0))
            self._draw_gradient()
            self.after(self._speed, self.Animate)


class WidgetConfig:
    def __init__(self, padding=(10, 10), font='Fira Sans', fontSize=12, ):
        self.padding = padding
        self.font = (font, fontSize)
        self.h1 = (font, fontSize+9)
        self.h2 = (font, fontSize+6)
        self.h3 = (font, fontSize+3)

class Config:
    def __init__(self, width=250, height=300):
        self.width = width
        self.height = height
        self.widgetConfig = None

    def DefaultWidgetConfig(self):
        self.widgetConfig = WidgetConfig()

    def CustomWidgetConfig(self, padding, font, fontSize):
        self.widgetConfig = WidgetConfig(padding, font, fontSize)

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
        self.animated = False
        self.speed = 0
        self.stretch = 1

    def animation(self, speed=50, stretch=2):
        self.speed = speed
        self.stretch = stretch
        self.animated = True

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
        self.animated = config.animated
        self.speed = config.speed
        self.stretch = config.stretch
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

        if config.widgetConfig is None:
            config.DefaultWidgetConfig()

        self.widgetConfig = config.widgetConfig
        self.padding = self.widgetConfig.padding
        self.font = self.widgetConfig.font
        self.h1 = self.widgetConfig.h1
        self.h2 = self.widgetConfig.h2
        self.h3 = self.widgetConfig.h3

        self.root = None
        self.canvas = None
        self.bg = None
        self.btns = []

    def add_choice_btn(self, btn_txt):
        btn = tkinter.Button(self.canvas, text=btn_txt)
        btn['command'] = lambda: self.entry_to_dict(dict_key)
        self.btns.append(btn)
        return btn

    def configure_btns(self):
        for btn in self.btns:
            hlt_bg = Color(self.color2.hex_l)
            hlt_fg = Color(self.color1.hex_l)
            hlt_bg.luminance = 0.45
            hlt_fg.luminance = 0.75
            btn.configure(fg=self.color1.hex_l, bg=self.color2.hex_l, highlightthickness = 0, activebackground=hlt_bg.hex_l, activeforeground=hlt_fg.hex_l, font=self.h3, bd=0)

    def add_entry(self):
        bg = Color(self.color2.hex_l)
        fg = Color(self.color1.hex_l)
        bg.luminance = 0.65
        fg.luminance = 0.65
        ent = tkinter.Entry(self.canvas, bg=bg.hex_l,fg=fg.hex_l,  bd=0, highlightthickness=0, font=self.font)
        return ent  

    def entry_to_dict(self, dict_key):
        data = self.entry.get()
        if data:
            d, key = dict_key
            d[key] = data
            self.top.destroy()

    def _center_window(self, win):
        win.wait_visibility() # make sure the window is ready
        x = ((win.winfo_screenwidth()//2) - (win.winfo_width())) // 2
        y = (win.winfo_screenheight() - (win.winfo_height())) // 2
        win.geometry(f'+{x}+{y}')

    def _Show(self):
        self.root = tkinter.Tk()
        self.root.pack_propagate(0)
        #self.root.resizable(width=False, height=False)
        self.root.withdraw()
        self.window = tkinter.Toplevel(width=self.width, height=self.height)
        self.window.resizable(width=False, height=False)
        self.window.pack_propagate(0)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        if not self.hasframe:
            self.window.overrideredirect(True)

        self._center_window(self.window)
        self.canvas = GradientFrame(self.window, self.color1, self.color2, self.direct, self.animated, self.speed, self.stretch, width=self.width, height=self.height, bd=0,
                   highlightthickness=0, relief="ridge")
        self.canvas.pack(expand=True, fill='both')

        if self.hasImg:
            self.img = tkinter.PhotoImage(file=self.path, format='png')
            self.canvas.create_image(self.width/2, self.height/2, image=self.img)

        self.window.wm_attributes("-alpha", self.alpha)

    def on_close(self):
        self.canvas.Stop()
        self.root.destroy()

        
class DebugFontWindow(BaseWindow):
    def __init__(self, config):
        BaseWindow.__init__(self, config)
    def Show(self):
        self._Show()
        fonts=list(font.families())
        fonts.sort()
        listnumber = 1
        for item in self.fonts:
            label = "listlabel" + str(listnumber)
            label = tkinter.Label(self.canvas,text=item,font=(item, 16)).pack()
            listnumber += 1


class ChoiceWindow(BaseWindow):
    def __init__(self, config):
        BaseWindow.__init__(self, config)
        self.b1 = None
        self.b2 = None
        self.entry = None
        self.response = None

    def Ask(self, msg, b1='OK', b2='Cancel', entry=False, horizontal=True):
        self._Show()
        x = self.padding[0]
        y = self.height*0.15
        rely = 0.333
        relHeight = 0.25
        inc=1
        self.canvas.create_text(self.width/2, y, text=msg, fill=self.color2.hex_l, font=self.h3, anchor='center')
        if entry:
            rely=0.3
            relHeight=0.2
            inc=2
            self.entry = self.add_entry()
            self.entry.place(x = self.width/2-((self.width/2)*0.85), rely = rely, relwidth = 0.85)
            rely=0.23

        if horizontal:
            self._add_horizontal_buttons(b1, b2)
        else:
            self._add_vertical_buttons(b1, b2, rely, relHeight, inc)
        self.root.mainloop()
        return self
        
    def _add_vertical_buttons(self, b1, b2, rely=0.333, relHeight=0.8, inc=1):
        b1 = self.add_choice_btn(b1)
        b2 = self.add_choice_btn(b2)
        b1.place(x = self.width/2-((self.width/2)*0.8), rely = rely*inc, relheight = relHeight, relwidth = 0.75)
        b2.place(x = self.width/2-((self.width/2)*0.8), rely = rely*(inc+1), relheight = relHeight, relwidth = 0.75)
        self.configure_btns()

    def _add_horizontal_buttons(self, b1, b2):
        self.b1 = self.add_choice_btn(b1)
        self.b1['command'] = self.b1_action
        self.b2 = self.add_choice_btn(b2)
        self.b2['command'] = self.b2_action
        self.b1.place(x = self.padding[0], rely = 0.55, relheight = 0.333, relwidth = 0.45)
        self.b2.place(x = (self.width-(self.width*0.45))-self.padding[0], rely = 0.55, relheight = 0.333, relwidth = 0.45)
        self.configure_btns()

    def b1_action(self, event=None):
        self.root.quit()
        if self.entry != None:
            self.response = self.entry.get()
        else:
            self.response = self.b1.cget('text')
            self.root.quit()

        self.root.destroy()

    def b2_action(self, event=None):
        self.response = self.b2.cget('text')
        self.root.quit()
        self.root.destroy()


class CopyTextWindow(BaseWindow):
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
        # for item in self.fonts:vnvbvbvcb
        #     label = "listlabel" + str(listnumber)
        #     label = tkinter.Label(self.canvas,text=item,font=(item, 16)).pack()
        #     listnumber += 1

        t1.place(x = self.width/2-((self.width/2)*0.8), rely = 0.1, relheight = 0.3, relwidth = 0.8)

        #l1.grid(row=0, column=0, sticky="ew", padx=60, pady=10)
        # e1.grid(row=1, column=0, sticky="ew", padx=60, pady=10)
        # t1.grid(row=2, column=0, sticky="nsew", padx=60, pady=10)

        self.canvas.grid_rowconfigure(2, weight=1)
        self.canvas.grid_columnconfigure(2, weight=1)
        # widget = tkinter.Label(self.canvas, text='Spam', fg='white', bg='black')
        # widget.pack()
        # self.canvas.create_window(self.width/2, self.height/2, window=widget)
        self.root.mainloop()


