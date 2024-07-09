from gradientmessagebox import  ColorConfig, BaseWindow, ChoiceWindow, PresetPromptWindow, PresetChoiceEntryWindow, PresetChoiceWindow, PresetImageBgMessage, PresetCopyTextWindow, PresetChoiceMultilineEntryWindow, CopyTextWindow, PresetUserPasswordWindow, TextWindow, ThreadedWindow, PresetLoadingMessage
import time

#config = ColorConfig(450, 300)
config = ColorConfig(width=450, height=300, color1="#4ed8a7", color2="#cf5270", alpha=1.0, saturation=1.0, direct='+x', hasFrame=True)
bar_config = ColorConfig(width=600, height=50, color1="#4ed8a7", color2="#cf5270", alpha=1.0, saturation=1.0, direct='+x', hasFrame=False)
#config = ColorConfig(350, 200, '#00ffff', '#ffa500', 0.99, 0.8, '-y', True)
#config.swap_mg_for_bg()
#config.invert()

#config.fg_saturation(0.5)
#config.bg_saturation(0.5)
#config.gradient_saturation(0.5)
config.imagery('./hvym_3d_logo.png', './logo.png')

config.animation(20, 4)
bar_config.animation(20, 1)
txt = '''this is a multi line string
that is going to span multiple lines
that is going to span multiple lines
that is going to span multiple lines
that is going to span multiple lines
that is going to span multiple lines
that is going to span multiple lines
that is going to span multiple lines
that is going to span multiple lines'''

#win = ChoiceWindow(config)
#win = MultiTextChoiceWindow(config)
#win = CopyTextWindow(config)
#win = UserPasswordWindow(config)
#win = ThreadedWindow(TextWindow, bar_config, 'HEAVYMETA')
#win = PresetLoadingMessage('LOADING')
cool='''
Cool?

'''
text = '''A very simple tkinter prompt window
 with an animated gradient background.'''
#win = PresetChoiceWindow(cool, 'Yup', 'Nope')
#win = PresetChoiceEntryWindow(txt, '1', '2')
#win = PresetChoiceMultilineEntryWindow(txt, '1', '2')
#win = PresetCopyTextWindow(txt, '1', '2')
#win.default_entry_text('Some default text')
#win =  PresetImageBgMessage(msg='HEAVYMETA', bg_img='./hvym_3d_logo.png', logo_img='./logo.png')
#win = PresetUserPasswordWindow(txt, '1', '2')
win = PresetPromptWindow(text)
# win.custom_txt_color('black')
win.set_title_text('GRADIENT MESSAGE BOX')
#win.imagery('./hvym_3d_logo.png', './logo.png')
#win.vertical_btns()
x = win.Prompt()
#x = win.Ask()
#x = win.Ask('Ask a question?', 'copy', 'cancel', txt)
#x = win.Show()
#win.Play()



print(x.response)
#time.sleep(10)

#win.Close()
# win.Stop()
# print('GETS HERE')

#win.Show()
