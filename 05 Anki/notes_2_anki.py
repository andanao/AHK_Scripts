# %%
from microsoft_translator import Translator
from process_class_notes import clean_notes

def process_notes(notes_raw,notes_out):
    print('testing')

def make_anki(input_f = "notes_cleaned.txt"):
    f = open(input_f, "r",encoding='utf-8').read()
    word_list = f.split('\n')

    print(word_list)
    print('\n\nINCOMPLETE FN')

# %%
if __name__ == "__main__":
    notes_raw = 'notes_raw.txt'
    clean_notes(to_file=True)



# %%
