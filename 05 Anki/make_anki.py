

def make_anki(input_f = "notes_cleaned.txt"):
    f = open(input_f, "r",encoding='utf-8').read()
    word_list = f.split('\n')

    print(word_list)
    print('\n\nINCOMPLETE FN')