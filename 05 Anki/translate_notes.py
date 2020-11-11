import pandas as pd
from googletrans import Translator

class anki_tools:
    

    def __init__(self):
        self.trans = Translator()
        self.word_list = []


    def set_word_list(self,in_list):
        if type(in_list) == str:
            in_list = [in_list]
        self.word_list = in_list
    
    def hanzi2anki(self,word_list = False):
        '''
        Word list must be list of 汉字
        Using google translate
       [['汉字', 'Hànzì', 'Chinese character']]
        '''
        if word_list:
            self.set_word_list(word_list)

        out_list = []
        translated = self.trans.translate(self.word_list,src = 'zh-cn')

        for item in translated:
            # hz = word_list[i]
            test_list = [item.origin, item.extra_data['translation'][1][3],item.text]
            # print(test_list)
            out_list.append(test_list)
        return out_list
    
    def hanzi2pinyin(self,word_list = False):
        '''
        Using google translate to get pinyin
        '''
        if word_list:
            self.set_word_list(word_list)

        out_list = []
        translated = self.trans.translate(self.word_list,src = 'zh-cn')

        for item in translated:
            # hz = word_list[i]
            test_list = [item.origin, item.extra_data['translation'][1][3]]
            # print(test_list)
            out_list.append(test_list)
        return out_list

        

worklist = [
    '白宫',
    '国会',
    '政策',
    '众议院',
    '参议院',
    '停运',
    '跌宕起伏',
    '人生中的跌宕起伏',
    '阳性',
    '阴性',
    '假期',
    '一战',
    '清单',
    '医疗保险',
    '预测',
    '理工男',
    '情商',
    '智商',
    '全面发展',
    '社交能力',
    '专业术语',
    '方差',
    '电影院',
    '歌曲',
    '悲伤',
    ]

tools = anki_tools()
tools.set_word_list(worklist)
# out = tools.hanzi2anki()
out = tools.hanzi2pinyin()