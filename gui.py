import PySimpleGUI as sg
import os.path
import os
import actions
import ntpath
import charts

sg.theme('SystemDefault')
files_types = ('*.txt','*.doc')

file_list_column = [
        [sg.Text("Choose file: "), 
        sg.In(size=(38, 1), enable_events=True, key="-FILE-"), 
        sg.FileBrowse(file_types=(("Text Files", "*.txt"),('Word Files','*.doc'),('All types of files',files_types)))],
        [sg.Button('Signs statistics'), sg.Button('Letters statistics'),sg.Button('Vowels and consonats statistics')],
        [sg.Text("File name:", size=(30,1)), sg.Text(key = '-NameOut-',size=(20,1),justification = 'right')],
        [sg.Text("Number of words:",size=(30,1)),sg.Text(key = '-STAT1-', size=(20,1),justification = 'right')],
        [sg.Text("Number of all characters:",size=(30,1)),sg.Text(key = '-STAT2-', size=(20,1),justification = 'right')],
        [sg.Text("Number of characters without spaces:",size=(30,1)),sg.Text(key = '-STAT3-', size=(20,1),justification = 'right')],
        [sg.Text("Number of punctuation marks:",size=(30,1)),sg.Text(key = '-STAT4-', size=(20,1),justification = 'right')],
        [sg.Text("Number of digits:",size=(30,1)),sg.Text(key = '-STAT5-', size=(20,1),justification = 'right')],
        [sg.Text("Number of sentences:",size=(30,1), justification = 'left'),sg.Text(key = '-STAT6-', size=(20,1),justification = 'right')],
        [sg.Multiline(key="-TEXT-", size=(60,40), justification = 'left')],
        [sg.Button('End', size = (15, 1),pad = ((300,0),(0,0)))]
    ]

stat_chart_column = [[sg.Text("Additional information",size = (30,1), justification = 'center', font = 'bold')],
                    [sg.Multiline(key="-LETTER-STAT-", size = (40,55),do_not_clear = True, font='courier 10')]]

layout = [[sg.Column(file_list_column, pad = ((0,0),(0,0))),sg.Column(stat_chart_column, element_justification = 'center', visible=False, key = '-COLUMN2-')]]

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

    if event == 'Signs statistics':
        try:
            sign_stat_dict = actions.sign_statistics(text)
            window['-LETTER-STAT-'].update('')
            for letter in sign_stat_dict:
                if letter != '\n':
                    percent = sign_stat_dict[letter]/list_of_statistics[1]*100
                    if sign_stat_dict[letter] > 9999:
                        window['-LETTER-STAT-'].update('Character: {0} = {1} | Percent: {2:.4f}%\n'.format(letter, sign_stat_dict[letter], percent), append = True)
                        continue
                    if sign_stat_dict[letter] > 999:                        
                        window['-LETTER-STAT-'].update('Character: {0} = {1}  | Percent: {2:.4f}%\n'.format(letter, sign_stat_dict[letter], percent), append = True)
                        continue
                    if sign_stat_dict[letter] > 99:                        
                        window['-LETTER-STAT-'].update('Character: {0} = {1}   | Percent: {2:.4f}%\n'.format(letter, sign_stat_dict[letter], percent), append = True)
                        continue
                    if sign_stat_dict[letter] > 9:
                        window['-LETTER-STAT-'].update('Character: {0} = {1}    | Percent: {2:.4f}%\n'.format(letter, sign_stat_dict[letter], percent), append = True)
                        continue
                    else:
                        window['-LETTER-STAT-'].update('Character: {0} = {1}     | Percent: {2:.4f}%\n'.format(letter, sign_stat_dict[letter], percent), append = True)

            window['-COLUMN2-'].update(visible = True)
            window.refresh()
        except:
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    if event == 'Letters statistics':
        try:
            letter_stat_dict, sum_of_letters = actions.letters_statistics(text)
            charts.draw_bar_chart(letter_stat_dict)
        except:
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    if event == 'Vowels and consonats statistics':
        try:
            vowels_sum, consonats_sum = actions.vowels_and_consonats(text)
            charts.draw_pie_chart([vowels_sum,consonats_sum],['Vowels','Consonants'])
        except:
            sg.popup("YOU MUST CHOOSE A FILE!", title = 'ERROR')

    if event == "End" or event == sg.WIN_CLOSED:
        break

window.close()