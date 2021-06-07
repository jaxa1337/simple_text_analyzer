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
        [sg.Button('Signs statistics'), sg.Button('Letters statistics'),sg.Button('Vowels and consonats statistics')],
    ]

stat_column = [
    [sg.Text("File name:"), sg.Text(key = '-NameOut-',size=(25,1))],
    [sg.Text("Number of words:"),sg.Text(key = '-STAT1-', size=(20,1))],
    [sg.Text("Number of all characters:"),sg.Text(key = '-STAT2-', size=(20,1))],
    [sg.Text("Number of characters without spaces:"),sg.Text(key = '-STAT3-', size=(20,1))],
    [sg.Text("Number of punctuation marks:"),sg.Text(key = '-STAT4-', size=(20,1))],
    [sg.Text("Number of digits:"),sg.Text(key = '-STAT5-', size=(20,1))],
    [sg.Text("Number of sentence:"),sg.Text(key = '-STAT6-', size=(20,1))]
]

text_viewer_column = [[sg.Multiline(key="-TEXT-", size=(60,30))]]

end_button_column = [[sg.Button('End', size = (15, 1))]]

layout = [[sg.Column(file_list_column, pad = ((0,0),(0,0)), element_justification='center')],[sg.Column(stat_column, pad = ((0,0),(0,0)),element_justification = 'left')],
        [sg.Column(text_viewer_column,pad = ((0,0),(0,0)), element_justification = 'center')],[sg.Column(end_button_column,pad = ((300,0),(0,0)),element_justification = 'right')]]
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
            window['-STAT1-'].update(list_of_statistics[0])
            window['-STAT2-'].update(list_of_statistics[1])
            window['-STAT3-'].update(list_of_statistics[2])
            window['-STAT4-'].update(list_of_statistics[3])
            window['-STAT5-'].update(list_of_statistics[4])
            window['-STAT6-'].update(list_of_statistics[5])
        except:
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    if event == "End" or event == sg.WIN_CLOSED:
        break

window.close()