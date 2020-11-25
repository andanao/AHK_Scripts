import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from googletrans import Translator
import pinyin
from anki_tools import anki_tools
import pandas as pd


full_dir = r'C:\Users\Adrian\Dropbox\中文\航空航天专业翻译必备词汇 - 百度文库.html'

with open(full_dir,'r',encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents,'lxml')


find1 = soup.find_all("div",class_='ie-fix')

cleaned_text =''

for item in find1:
    cleaned_text += item.text

cleaned_text = cleaned_text[5:]
cleaned_text = re.sub(r'[\s,\d]','',cleaned_text)
cleaned_text = re.sub(r'([a-zA-Z]{1})(?=[\u4e00-\u9fff]{1})','\\1,\n',cleaned_text)
cleaned_text = re.sub(r'([\u4e00-\u9fff]{1})(?=[a-zA-Z]{1})','\\1,',cleaned_text)
# cleaned_text = re.sub(r'[\s,\d]','',cleaned_text)



hanzi = re.findall(r'[\u4e00-\u9fff]+(?=,)',cleaned_text)
words = re.findall(r'(?<=,)[a-zA-Z]+',cleaned_text)

# print(len(hanzi))
# print(len(words))

out_list = []
if len(hanzi) == len(words):
    for i in range(len(hanzi)):
        pyn = pinyin.get(hanzi[i])
        # print(hanzi[i]+'\t'+pyn+'\t'+words[i])
        out_list.append([hanzi[i], pyn, words[i]])

out_df= pd.DataFrame(out_list)
out_df.to_csv('aero_vocab.csv',index=False,header=False)