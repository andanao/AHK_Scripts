import pinyin
import pandas as pd
import re
import click

def clean_notes(input_f = "notes_raw.txt",to_file= False, out_f='notes_cleaned.txt'):
    file = open("class_notes.txt", "r",encoding='utf-8').read()

    cleaned_text = re.sub(r'(?<=[\u4e00-\u9fff])\d','',file)
    cleaned_text = re.sub(r'.*\:.*','',cleaned_text)
    cleaned_text = re.sub(r'.*\ds.*','',cleaned_text)
    cleaned_text = re.sub(r'\/','\n',cleaned_text)
    cleaned_text = re.sub(r'(早上好|你好)','',cleaned_text)
    cleaned_text = re.sub(r'[^\u4e00-\u9fff]+','\n',cleaned_text)

    if to_file:
        f = open(out_f, "w+",encoding='utf-8')
        f.write(cleaned_text)
        f.close()
    else:
        print("\n\t{} cleaned".format(input_f))
        return cleaned_text

def make_anki(input_f = "notes_cleaned.txt"):
    f = open(input_f, "r",encoding='utf-8').read()
    word_list = f.split('\n')
    print(word_list)
    print('\n\nINCOMPLETE FN')


if __name__ == "__main__":
    clean_notes()

    # if click.confirm('Check cleaned.txt for logic',default=True):
    # make_anki()