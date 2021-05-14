ascii_numbers_of_sign = [0,1,2,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126,127,167,168,169,170,173,174,175]

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
                counter+=1
            else:
                if not(ord(previous_letter_2) in ascii_numbers_of_sign):
                    counter+=1
                else:
                    if not(ord(previous_letter_3) in ascii_numbers_of_sign):
                        counter+=1
            if temp == len(text):
                counter+=1
                break
        previous_letter_3 = previous_letter_2 
        previous_letter_2 = previous_letter_1
        previous_letter_1 = x
    print('There are %d words in the text.' %counter)