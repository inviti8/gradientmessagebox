from imgpopup import ImageConfig, ColorConfig, BaseWindow, ChoiceWindow

config = ColorConfig(150, 100, '#00ffff', '#ffa500', 0.9, 1.0, '-y', True, 1.0, 0.1)
#config = ImageConfig(150, 400, '#00ffff', '#ffa500', 1.0, '-y', False, './test-bg.png')


win = ChoiceWindow(config)

win.Show()
