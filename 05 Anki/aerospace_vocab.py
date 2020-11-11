from bs4 import BeautifulSoup
from urllib.request import urlopen
import anki_tools


full_dir = r'C:\Users\Adrian\Dropbox\中文\航空航天专业翻译必备词汇 - 百度文库.html'

with open(full_dir,r) as f :
    contents = f.read()

    soup = BeautifulSoup(contents,'lxml')