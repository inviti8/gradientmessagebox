from imgpopup import  ColorConfig, BaseWindow, ChoiceWindow, MultiTextChoiceWindow, CopyTextWindow, UserPasswordWindow

config = ColorConfig(450, 300)
#config = ColorConfig(350, 200, '#00ffff', '#ffa500', 0.99, 0.8, '-y', True)
#config.invert()
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
