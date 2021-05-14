import actions
#input('TEXT ANALISYS IN THE TERMINAL\nPaste text into the file \'text.txt\', then press ENTER ...')

text_file = open('text.txt','r',encoding='utf-8')
text = text_file.read()
action = -1

#MAIN LOOP
while action != 0:
    print('0 - End the program.\n1 - Print text\n2 - Count the words.')
    action = int(input("Select the action, enter a number: "))
    #COUNT THE WORDS
    if action == 1:
        print(text)
    elif action == 2:
        actions.count_words(text)
        