import charts
punctuation_marks = [',','.','?','!',';','-','(',')','\'','"','[',']','{','}','…','»','«','—']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z','Ł','Ó','Ż','Ź','Ą','Ę','Ń','Ś','Ć','É','Á']
digits = ['0','1','2','3','4','5','6','7','8','9']
vowels = ['a','o','i','e','y','u','ę','ą']
end_of_sentence = ['.','!','?']
space = [' ','\n','\t']

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

    for x in text[1:]:
        temp += 1
        if x in end_of_sentence and not(previous_letter in end_of_sentence) and next_letter in space:
            number_of_sentence+=1 

        previous_letter = x
        position += 1
        if temp < len(text) - 3:
            next_letter = text[position + 2]
        else:
            number_of_sentence+=1
            break

    return number_of_sentence


def basic_statistics(text):

    len_of_text = len(text)
    list_of_statistics = [count_words(text),len_of_text, (len_of_text - count_sign(text, ' ')),count_sign(text, punctuation_marks),
                        count_sign(text, digits),count_sentence(text)]
    return list_of_statistics


def sign_statistics(text):
    signs = {}
    sort_dict = {}

    for x in text:
        if x in signs:
            signs[x] += 1 
        else:
            signs[x] = 1

    v = sorted(signs.values(), reverse= True)

    for j in v:
        for i in signs:
            if signs[i] == j:
                sort_dict[i] = j

    return sort_dict

def letters_statistics(text):
    letters = {}
    sign_counter = 0

    for x in text.lower():
        if x.upper() in capital_letters:
            sign_counter += 1
            if not(x in letters):
                letters[x] = 1
            else:
                letters[x] += 1 

    return letters, sum(letters.values())
    
def vowels_and_consonats(text):
    vowelsCounter = 0
    consonantsCounter =0
    letterCounter = 0

    for x in text.lower():
        if x.upper() in capital_letters:
            letterCounter +=1
            if x in vowels:
                vowelsCounter += 1
            else:
                consonantsCounter +=1
    return vowelsCounter, consonantsCounter
    