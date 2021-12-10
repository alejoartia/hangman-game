import random
from hangman import hangman

def read():
    """This method read the file and return a random word"""
    words = []
    with open("./words.txt","r", encoding="utf-8") as f:
        for w in f:
            words.append(str(w))

    random_word = random.randint(0,len(words))
    return words[random_word]


def is_str(key):
    """handle if the input is a number"""
    try:
        int(key)
        return False 
    except ValueError:
        return  True  


def input_exist(key, word):
    """here we get if the input is in the word"""
    word_list = [i for i in word]
    word_indexation = [str(i) for i in range(len(word_list))]

    key_list = [i for i in key]

    #here returns how many items were found 
    counting = [word_list.count(item) for item in key if item in word_list ]
    
    # dict to get the words and index
    list_word = list(zip(word_list,word_indexation))
    list_key = list(zip(key_list,counting))

    indexing_key_word =[i[1] for i in list_word if i[0] == 'a']

    print(indexing_key_word)
    
    #assign the lyric and key of the key input
    keys_list = []
    for i in list_word:
        for j in range(len(key)):
            if i[0] == str(key[j]):

                keys_list.append(list(zip(key[j],i[1])))
    
    #print('keys_list',keys_list)

    return list_key, list_word, keys_list


def punishment(fit):
    """this funtions count the times that the people fail """
    if len(fit) < 1:
        punish = 'PUNISHMENT'
        return punish
    else:
        punish = "Keep it up"
        return punish


def filling_word(word):

    default_dash = '_'

    filling_list =[default_dash for i in range(len(word))]

    return filling_list


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


if __name__=='__main__':

    hangmanword = hangman.hangedman_draw()
    h = 0

    #1.  read the file with all the words
    word = normalize(read())
    print(word)
    
    filling_list = filling_word(word)
    print('filling_word',filling_list[:-1])

    life_cycle = 6

    while True:
        #2. receive the digit with an input 
        print('------------HANGMAN GAME---------------')
        key = input("please digit a lyric: ")

        #3. validate if the lyric is not a number
        if not is_str(key):
            key = input("please digit a lyric not a number: ")
        
        #4. get the dicts with the times repited of the input values an dict with index of the random word
        number_repited, index_of_words, keys_list = input_exist(key=key,word=word)

        for i in range(len(keys_list)):
            # print(keys_list[i][0][0])
            filling_list[int(keys_list[i][0][1])] = keys_list[i][0][0]

        print('filling_word',filling_list[:-1])



        print(hangmanword[h])
        punish = punishment(number_repited)
        if punish == 'PUNISHMENT':
            life_cycle -= 1
            h += 1


        print("-----------")
        print('life',life_cycle)
        print("-----------")
        print('punish',punish)

        
        filling_word(word)

        if life_cycle == 0:
            print("GAME OVER")
            break

        # print('len(filling_list)',len(filling_list))
        # print('len(word)',len(word))
        word_list = [i for i in word]
        # print(word_list[:-1])
        # fill_list = filling_list[:-1]
        # print(fill_list)
        if filling_list[:-1] == word_list[:-1]:
            print("CONGRATS YOU ARE SAVED")
            break

        

