from imgpopup import ImageConfig, ColorConfig, BaseWindow, ChoiceWindow

config = ColorConfig(350, 200, '#00ffff', '#ffa500', 0.99, 0.8, '-y', True, 1.0, 0.1)
config.animation(70, 4)
#config = ImageConfig(150, 400, '#00ffff', '#ffa500', 1.0, '-y', False, './test-bg.png')


win = ChoiceWindow(config)
txt = '''this is a multi line string
that is going to span multiple lines'''
#win.Ask('Ask a question?')
x = win.Ask('Ask a question?', '1', '2', True)
#x = win.Ask(txt)

print(x.response)


#win.Show()
