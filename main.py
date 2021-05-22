import actions, charts
#input('TEXT ANALISYS IN THE TERMINAL\nPaste text into the file \'text.txt\', then press ENTER ...')

text_file = open('text.txt','r',encoding='utf-8')
text = text_file.read()
action = -1
pline = '=' * 20
#MAIN LOOP
while action != 0:
    print('0 - End the program.\n1 - Print text\n2 - Count the words.')
    print('3 - Basic statistics.\n4 - Signs statistics\n5 - Letters statistics')
    print('6 - Consonants and vowels')
    action = int(input("Select the action, enter a number: "))
    #COUNT THE WORDS
    if action == 1:
        print(text)
    elif action == 2:
        print(pline,'Word counter',pline)
        print('There are %d words in the text.\n' % actions.count_words(text))
    elif action == 3:
        print(pline,'Basic statistics',pline)
        actions.basic_statistics(text)
    elif action == 4:
        print(pline,'Signs statistics',pline)
        actions.sign_statistics(text)
    elif action == 5:
        print(pline,'Letters statistics',pline)
        actions.letters_statistics(text)  
    elif action == 6:
        print(pline,'Vowels and consonats statistics',pline)
        actions.vowels_and_consonats(text)