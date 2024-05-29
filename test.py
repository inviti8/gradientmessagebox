from gradientmessagebox import  ColorConfig, BaseWindow, ChoiceWindow, MultiTextChoiceWindow, CopyTextWindow, UserPasswordWindow

#config = ColorConfig(450, 300)
config = ColorConfig(width=250, height=300, color1="#00ffff", color2="#ffa500", alpha=1.0, saturation=1.0, direct='+x', hasframe=True)
#config = ColorConfig(350, 200, '#00ffff', '#ffa500', 0.99, 0.8, '-y', True)
#config.swap_mg_for_bg()
config.invert()

#config.fg_saturation(0.5)
#config.bg_saturation(0.5)
#config.gradient_saturation(0.5)
#config.imagery('./test-bg.png', './logo.png')

config.animation(20, 4)



#win = ChoiceWindow(config)
#win = MultiTextChoiceWindow(config)
#win = CopyTextWindow(config)
win = UserPasswordWindow(config)
txt = '''this is a multi line string
that is going to span multiple lines'''
#win.Ask('Ask a question?')
#x = win.Ask('Ask a question?', '1', '2', True)
#x = win.Ask(txt)
x = win.Ask('Ask a question?', 'copy', 'cancel', txt)

print(x.response)


#win.Show()
