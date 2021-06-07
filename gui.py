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
        [sg.Button('Signs statistics'), sg.Button('Letters statistics')],
        [sg.Button('Vowels and consonats statistics')],
        [sg.Text('', size = (35,1), key='-STAT1-')],
        [sg.Text('', size = (35,1), key='-STAT2-')],
        [sg.Text('', size = (35,1), key='-STAT3-')],
        [sg.Text('', size = (35,1), key='-STAT4-')],
        [sg.Text('', size = (35,1), key='-STAT5-')],
        [sg.Text('', size = (35,1), key='-STAT6-')],
        # [sg.Button('')],
        [sg.Text(size = (30,1)),sg.Button(' End ')]
    ]

image_viewer_column = [
        [sg.Text("File name:"), sg.Text(key = '-NameOut-',size=(25,1))],
        [sg.Multiline(key="-TEXT-", size=(60,30))],
    ]

layout = [[sg.Column(file_list_column,pad = (0,0), element_justification='left'),sg.VSeperator(),sg.Column(image_viewer_column,pad = (0,0))]]
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

        try:
            window['-TEXT-'].update(text)
            list_of_statistics = actions.basic_statistics(text)
            window['-STAT1-'].update('Number of words: %d' % list_of_statistics[0])
            window['-STAT2-'].update('Number of all characters: %d' % list_of_statistics[1])
            window['-STAT3-'].update('Number of characters without spaces: %d' % list_of_statistics[2])
            window['-STAT4-'].update('Number of punctuation marks: %d' % list_of_statistics[3])
            window['-STAT5-'].update('Number of digits: %d' % list_of_statistics[4])
            window['-STAT6-'].update('Number of sentence: %d' % list_of_statistics[5])
        except:
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    if event == " End " or event == sg.WIN_CLOSED:
        break

window.close()