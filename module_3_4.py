# Task "Однокоренные"



def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        if root_word in other_words[i].lower() or other_words[i].lower() in root_word:
            same_words.extend([other_words[i]])
        else:
            continue
    print(same_words)
    return same_words



single_root_words('Дом', 'домовой', 'Домосед', 'Управдом', 'котовасия', 'домашний', 'Домой')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')