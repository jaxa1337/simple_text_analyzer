import PySimpleGUI as sg
import os.path
import os
import actions
import ntpath

tuple_of_files_types = ('*.txt','*.doc')
y = 50
x = 50
file_list_column = [
        [sg.Text("Choose file: "), 
        sg.In(size=(20, 1), enable_events=True, key="-FILE-"), 
        sg.FileBrowse(file_types=(("Text Files", "*.txt"),('Word Files','*.doc'),('All types of files',tuple_of_files_types)))],
        [sg.Button('ShowText')],
        # [sg.Button('')],
        # [sg.Button('')],
        [sg.Button('End')]
    ]

image_viewer_column = [
        [sg.Text("File name:",key = '-NameOut-',size=(29,1))],
        [sg.Multiline(key="-TEXT-", size=(60,50))],
    ]

layout = [[sg.Column(file_list_column),sg.VSeperator(),sg.Column(image_viewer_column)]]
# Create the window
window = sg.Window("Simple text analyzer", layout, resizable = True)

# Create an event loop
while True:
    event, values = window.read()
    count = 0
    if event == '-FILE-':
        filename = 'File name: '+ ntpath.basename(values["-FILE-"])
        window['-NameOut-'].update(filename)

    if event == 'ShowText':
        text_file = open(values['-FILE-'],'r',encoding='utf-8')
        text = text_file.read()
        window['-TEXT-'].update(text)
    elif event == "End" or event == sg.WIN_CLOSED:
        break

window.close()