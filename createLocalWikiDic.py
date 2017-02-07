#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd

sheets = pd.ExcelFile('./regional_words_localWiki.xlsx').parse('Sheet1')

for w, y in zip(sheets['単語'], sheets['読み']):
    print(f"{w},,,1,名詞,固有名詞,地域,一般,*,*,{w},{y},{y},地域固有")
