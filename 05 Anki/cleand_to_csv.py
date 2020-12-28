from anki_tools import anki_tools
from googletrans import Translator

# def make_anki():
f = open("cleaned.txt", "r",encoding='utf-8').read()
word_list = f.split('\n')
print('not_done')
# tools = anki_tools()
# tools.set_word_list(word_list)
trans = Translator()