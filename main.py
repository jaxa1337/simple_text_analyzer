
    print('3 - Basic statistics.\n4 - Signs statistics\n5 - Letters statistics')
    print('6 - Consonants and vowels')

    elif action == 4:
        print(pline,'Signs statistics',pline)
        actions.sign_statistics(text)
    elif action == 5:
        print(pline,'Letters statistics',pline)
        actions.letters_statistics(text)  
    elif action == 6:
        print(pline,'Vowels and consonats statistics',pline)
        actions.vowels_and_consonats(text)
    
    text_file.close()
    text_file = open('text.txt','r',encoding='utf-8')
    text = text_file.read()