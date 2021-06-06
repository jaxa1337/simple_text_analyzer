import PySimpleGUI as sg
import os.path
import os
import actions
import ntpath
sg.theme('SystemDefault')
files_types = ('*.txt','*.doc')

file_list_column = [
        [sg.Text("Choose file: "), 
        sg.In(size=(20, 1), enable_events=True, key="-FILE-"), 
        sg.FileBrowse(file_types=(("Text Files", "*.txt"),('Word Files','*.doc'),('All types of files',files_types)))],
        [sg.Button('Show text'),
        sg.Button('Word counter')],
        [sg.Text('', size = (35,1), key='-STAT1-'),
         sg.Text('', size = (35,1), key='-STAT1-'),
         sg.Text('', size = (35,1), key='-STAT1-'),
        ],
        # [sg.Button('')],
        [sg.Text(size = (30,1)),sg.Button(' End ')]
    ]

image_viewer_column = [
        [sg.Text("File name:"), sg.Text(key = '-NameOut-',size=(25,1))],
        [sg.Multiline(key="-TEXT-", size=(60,30))],
    ]

layout = [[sg.Column(file_list_column,pad = (0,0), justification = 'center'),sg.VSeperator(),sg.Column(image_viewer_column,pad = (0,0))]]
window = sg.Window("Simple text analyzer", layout, resizable = False)

while True:
    event, values = window.read()

    if event == '-FILE-':
        try:
            filename = ntpath.basename(values["-FILE-"])
            window['-NameOut-'].update(filename)
            text_file = open(values['-FILE-'],'r',encoding='utf-8')
            text = text_file.read()
        except:
            pass

    if event == 'Show text':
        try:
            window['-TEXT-'].update(text)
        except: 
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    if event == 'Word counter':
        try:
            window['-STAT1-'].update('There are %d words in the text.\n' % actions.count_words(text))
        except: 
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    elif event == "End" or event == sg.WIN_CLOSED:
        break

window.close()