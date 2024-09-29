from gradientmessagebox import *
import time

# shared = SharedRoot()

def test_1(*args):
	print('1')
	w = PresetLoadingMessage('LOADING')
	w.Play()
	time.sleep(5)
	# win = PresetThreadedMessage('TEST!!!')
	# win.Show()

def test_2(*args):
	w = PresetPromptWindow(text)
	w.Prompt()
	print('2')

def test_3(*args):
	link_txt = "https://docs.cartesi.io/cartesi-rollups/1.5/tutorials/erc-721-token-wallet/"
	w = PresetWidePromptWindow(link_txt)
	w.Prompt()
	print(args)
	print('3')

def test_4(*args):
	link_txt = "https://docs.cartesi.io/cartesi-rollups/1.5/tutorials/erc-721-token-wallet/"
	w = PresetLinkWindow(link_txt)
	w.Prompt()
	print('4')

def test_5(*args):
	print('5')



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
# win = PresetLoadingMessage('LOADING', None)
# win.Play()
cool='''
Cool?

'''
text = '''A very simple tkinter prompt window
 with an animated gradient background.'''
# win = PresetChoiceWindow(cool, 'Yup', 'Nope')
# win.Ask()
#win = PresetDropDownWindow(txt)
#win = PresetChoiceEntryWindow(txt, '1', '2')
#win = PresetChoiceMultilineEntryWindow(txt, '1', '2')
#x = win.Ask()
btn_dict = { '1': test_1, '2': test_2,'3': test_3,'4': test_4,'5': test_5 }
win = PresetMultiButtonWindow(btn_dict)
win.Show()
#win = PresetCopyTextWindow(txt)
#win = PresetFileSelectWindow(txt)
#win.default_entry_text('Some default text')
#win =  PresetImageBgMessage(msg='HEAVYMETA', bg_img='./hvym_3d_logo.png', logo_img='./logo.png')
#win = PresetUserPasswordWindow(txt, '1', '2')
# win = PresetPromptWindow(text)
# win.Prompt()
# win.custom_txt_color('black')
#win.custom_msg_color('pink')
#win.set_title_text('GRADIENT MESSAGE BOX')
#win.set_file_select_types([("SVG Files", "*.svg"), ("PNG Files", "*.png")])
#win.imagery('./hvym_3d_logo.png', './logo.png')
#win.vertical_btns()
#x = win.Prompt()
#x = win.FileSelect()
#x = win.Ask('Ask a question?', 'copy', 'cancel', txt)
#x = win.Show()
#win.Play()
#x=win.DropDown(['1', '2', '3'])



#print(x.response)
time.sleep(5)

# win.Close()
#win.Stop()
# print('GETS HERE')

#win.Show()
