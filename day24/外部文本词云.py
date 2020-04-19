"""
外部文本词云
"""

import wordcloud
import random

# 读入外部文本文件
f = open('./res/txt/词云.txt', encoding='utf-8')
txt = f.read()
# 背景颜色和整体风格 https://matplotlib.org/examples/color/colormaps_reference.html
w = wordcloud.WordCloud(
    scale=2,  # 缩放2倍
    max_font_size=100,
    background_color='#FFECB3',
    colormap='YlOrBr',
    font_path='./res/font/SimHei.ttf'
)
# 将txt变量传入
w.generate(txt)
w.to_file('./res/img/output3.png')
