# %%
import pinyin
import csv
from microsoft_translator import Translator
from clean_notes import clean_notes


def process_notes(notes_raw,notes_out):
    print('testing')

def _get_word_list(input_f = "notes_cleaned.txt"):
    f = open(input_f, "r",encoding='utf-8').read()
    word_list = f.split('\n')
    return word_list

def make_anki(input_f = "notes_cleaned.txt",out_f = 'notes_import.csv'):
    """
    Loads cleaned class notes, saves as out_f
    """
    word_list = _get_word_list()
    trans = Translator()
    word_list_translated = trans.translate(word_list)
    full_list = []
    for i,val in enumerate(word_list):
        full_list.append([val,pinyin.get(val),word_list_translated[i]])
    print(full_list)
    with open(out_f,'w+',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(full_list)
    return full_list

if __name__ == "__main__":
    notes_raw = 'notes_raw.txt'
    clean_notes(to_file=True)
    full_list = make_anki()



