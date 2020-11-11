import pandas as pd
from googletrans import Translator


translator = Translator()

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


out = translator.translate(worklist)