from gradientmessagebox import  ColorConfig, BaseWindow, ChoiceWindow, MultiTextChoiceWindow, CopyTextWindow, UserPasswordWindow, TextWindow, ThreadedWindow
import time

#config = ColorConfig(450, 300)
config = ColorConfig(width=450, height=300, color1="#4ed8a7", color2="#cf5270", alpha=1.0, saturation=1.0, direct='+x', hasframe=True)
bar_config = ColorConfig(width=600, height=50, color1="#4ed8a7", color2="#cf5270", alpha=1.0, saturation=1.0, direct='+x', hasframe=False)
#config = ColorConfig(350, 200, '#00ffff', '#ffa500', 0.99, 0.8, '-y', True)
#config.swap_mg_for_bg()
#config.invert()

#config.fg_saturation(0.5)
#config.bg_saturation(0.5)
#config.gradient_saturation(0.5)
config.imagery('./hvym_3d_logo.png', './logo.png')

config.animation(20, 4)
bar_config.animation(20, 1)


#win = ChoiceWindow(config)
#win = MultiTextChoiceWindow(config)
#win = CopyTextWindow(config)
#win = UserPasswordWindow(config)
win = ThreadedWindow(TextWindow, bar_config, 'HEAVYMETA')
txt = '''this is a multi line string
that is going to span multiple lines'''
#win.Ask('Ask a question?')
#x = win.Ask('Ask a question?', '1', '2', True)
#x = win.Ask(txt)
#x = win.Ask('Ask a question?', 'copy', 'cancel', txt)
x = win.Show()

#print(x.response)
time.sleep(10)

win.Close()
print('GETS HERE')

#win.Show()
