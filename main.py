import actions, charts
#input('TEXT ANALISYS IN THE TERMINAL\nPaste text into the file \'text.txt\', then press ENTER ...')

text_file = open('text.txt','r',encoding='utf-8')
text = text_file.read()
action = -1

#MAIN LOOP
while action != 0:
    print('0 - End the program.\n1 - Print text\n2 - Count the words.')
    print('3 - Basic statistics.\n4 - Signs statistics\n5 - Letters statistics')
    action = int(input("Select the action, enter a number: "))
    #COUNT THE WORDS
    if action == 1:
        print(text)
    elif action == 2:
        print('=======================Word counter=======================')
        print('There are %d words in the text.\n' % actions.count_words(text))
    elif action == 3:
        print('======================Basic statistics====================')
        actions.basic_statistics(text)
    elif action == 4:
        print('======================Signs statistics===================')
        actions.sign_statistics(text)
    elif action == 5:
        print('======================Letters statistics===================')
        actions.letters_statistics(text)