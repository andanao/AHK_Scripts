import pinyin
import pandas as pd
import re
import click

def clean_notes():
    file = open("class_notes.txt", "r",encoding='utf-8').read()

    cleaned_text = re.sub(r'(?<=[\u4e00-\u9fff])\d','',file)
    cleaned_text = re.sub(r'.*\:.*','',cleaned_text)
    cleaned_text = re.sub(r'.*\ds.*','',cleaned_text)
    cleaned_text = re.sub(r'\/','\n',cleaned_text)
    cleaned_text = re.sub(r'(早上好|你好)','',cleaned_text)
    cleaned_text = re.sub(r'[^\u4e00-\u9fff]+','\n',cleaned_text)

    f = open("cleaned.txt", "w+",encoding='utf-8')
    f.write(cleaned_text)
    f.close()

def make_anki(out_f = "cleaned.txt"):
    f = open("cleaned.txt", "r",encoding='utf-8').read()
    word_list = f.split('\n')
    print('not_done')


if __name__ == "__main__":
    clean_notes()

    # if click.confirm('Check cleaned.txt for logic',default=True):
    # make_anki()