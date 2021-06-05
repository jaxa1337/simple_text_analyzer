import PySimpleGUI as sg
import os.path
import os
import main.py

tuple_of_files_types = ('*.txt','*.doc')

file_list_column = [
        [sg.Text("Choose file"), sg.In(size=(25, 1), enable_events=True, key="-FILE-"), 
        sg.FileBrowse(file_types=(("Text Files", "*.txt"),('Word Files','*.doc'),('All types of files',tuple_of_files_types)))],
        [sg.Button('Show text')],
        [sg.Button('')],
        [sg.Button('')],
        [sg.Button('End')]
    ]

image_viewer_column = [
        [sg.Text("File content:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Text(key="-TEXT-")],
    ]

layout = [[sg.Column(file_list_column),sg.VSeperator(),sg.Column(image_viewer_column)]]
# Create the window
window = sg.Window("Simple text analyzer", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == 'Show Text':

    if event == "End" or event == sg.WIN_CLOSED:
        break

window.close()