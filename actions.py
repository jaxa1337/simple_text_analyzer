import charts
ascii_numbers_of_sign = [0,1,2,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126,127,167,168,169,170,171,173,174,175,187,8212,8230,]
punctuation_marks = [',','.','?','!',';','-','(',')','\'','"','[',']','{','}','…','»','«','—']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z','Ł','Ó','Ż','Ź','Ą','Ę','Ń','Ś','Ć','É','Á']
digits = ['0','1','2','3','4','5','6','7','8','9']
vowels = ['a','o','i','e','y','u','ę','ą']
end_of_sentence = ['.','!','?']

def count_words(text):
    counter = 0
    word_flag = False

    for x in range(len(text)):
        if text[x].upper() in capital_letters and word_flag == False:
            counter+=1
            word_flag = True
            continue
        elif not(text[x].upper() in capital_letters) and word_flag == True:
            word_flag = False
            continue
    
    if text[-1].upper() in capital_letters:
        counter += 1

    return counter

def count_sign(text, sign):
    counter = 0

    for x in text:
        if x in sign:
            counter += 1
    return counter

def count_sentence(text):
    number_of_sentence = 0
    position = 0
    temp = 1
    previous_letter = text[0]
    next_letter = text[2]
    next_letter_2 = text[3]

    for x in text[1:]:
        temp += 1
        if x == '.' and previous_letter != '.' and (next_letter == ' ' or next_letter == '\n'):
            if next_letter_2 in capital_letters: 
                number_of_sentence+=1 

        previous_letter = x
        position += 1
        if temp < len(text) - 3:
            next_letter = text[position + 2]
            next_letter_2 = text[position + 3]
        else:
            number_of_sentence+=1
            break

    return number_of_sentence


def basic_statistics(text):

    len_of_text = len(text)
    print('Number of words: %d' % count_words(text))
    print('Number of all characters: %d' % len_of_text)
    print('Number of characters without spaces: %d' % (len_of_text - count_sign(text, ' ')))
    print('Number of punctuation marks: %d' % count_sign(text, punctuation_marks))
    print('Number of digits: %d' % count_sign(text, digits))
    print('Number of sentence: %d' % count_sentence(text))
    print('')


def sign_statistics(text):
    signs = {}

    for x in text:
        if not(x in signs):
            signs[x] = 1
        else:
            signs[x] += 1 

    for key in sorted(signs):
        print('Sign "',key,'" :',signs[key],' \t| Percent: %.2f' %((signs[key]/len(text))*100),'%')

def letters_statistics(text):
    letters = {}
    sign_counter = 0

    for x in text.lower():
        if not(ord(x) in ascii_numbers_of_sign) and not(x in digits) and x != '\n':
            sign_counter += 1
            if not(x in letters):
                letters[x] = 1
            else:
                letters[x] += 1 

    for key in sorted(letters):
        print('Letter "',key,'" :',letters[key],' \t| Percent: %.2f' %((letters[key]/(len(text)-sign_counter))*100),'%')

    print('Sum of all letters: {sum_}'.format(sum_ = sum(letters.values())))
    
    cont = 'null'
    while cont != 'Y' or cont != 'N':
        cont = input('Do you want to draw a chart? [Y/N]: ')
        if cont == 'Y':
            charts.draw_bar_chart(letters)
            break
        elif cont == 'N':
            break
    
def vowels_and_consonats(text):
    vowelsCounter = 0
    consonantsCounter =0
    letterCounter = 0

    for x in text.lower():
        if not(ord(x) in ascii_numbers_of_sign):
            letterCounter +=1
            if x in vowels:
                vowelsCounter += 1
            else:
                consonantsCounter +=1

    print('Number of vowels: {v}    \t| Procent: {pv:.2f}%'.format(v = vowelsCounter, pv = vowelsCounter/letterCounter*100))
    print('Number of consonats: {c} \t| Procent: {pc:.2f}%'.format(c = consonantsCounter, pc = consonantsCounter/letterCounter*100))
    
    cont = 'null'
    while cont != 'Y' or cont != 'N':
        cont = input('Do you want to draw a chart? [Y/N]: ')
        if cont == 'Y':
            charts.draw_pie_chart([vowelsCounter,consonantsCounter],['Vowels','Consonants'])
            break
        elif cont == 'N':
            break