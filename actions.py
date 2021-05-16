ascii_numbers_of_sign = [0,1,2,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126,127,167,168,169,170,173,174,175]
punctuation_marks = [',','.','?','!',';','-','(',')','\'','"','[',']','{','}']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','U','V','X','Y','Z','Ł','Ó','Ż','Ź']
digits = [0,1,2,3,4,5,6,7,8,9]

def count_words(text):
    counter = 0
    temp = 3
    previous_letter_3 = text[0]
    previous_letter_2 = text[1]
    previous_letter_1 = text[2]

    for x in text[3:]:
        temp += 1
        if x == chr(32) or x==chr(10):
            if not(ord(previous_letter_1) in ascii_numbers_of_sign):
                counter += 1
            else:
                if not(ord(previous_letter_2) in ascii_numbers_of_sign):
                    counter += 1
                else:
                    if not(ord(previous_letter_3) in ascii_numbers_of_sign):
                        counter += 1
        if temp == len(text):
            counter+=1
            break

        previous_letter_3 = previous_letter_2 
        previous_letter_2 = previous_letter_1
        previous_letter_1 = x
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
        if x == '.' and previous_letter != '.' and next_letter == ' ':
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


def letter_statistics(text):
    letters = {}
    counter = 0

    for x in text.lower():
        if not(x in letters):
            letters[x] = 1
        else:
            letters[x] += 1 

    for key in sorted(letters):
        print('Letter "',key,'" :',letters[key],'\t| Percent: %.2f' %((letters[key]/len(text))*100))