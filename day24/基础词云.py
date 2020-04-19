"""
基础词云
"""

import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
w.generate('From tomorrow on, be a happy man.Feed horses, chop wood, travel the workd.\
    From tomorrow on, care about food and vegetables. I have a house, facing the sea, spring flowers.')
# 生成本地图片
w.to_file('./res/img/output1.png')


# 创建词云对象，设置词云图片宽、高、字体、背景颜色等参数
# 中文字体需要提前下载中文字体文件

w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#212121',
    font_path='./res/font/SimHei.ttf'
)
w.generate('从明天起，做一个幸福的人，喂马、劈柴，周游世界，从明天起，关心粮食和蔬菜。\
    我有一所房子，面朝大海，春暖花开。从明天起，和每一个亲人通信，告诉他们我的幸福。\
    愿你有一个灿烂的前程，愿你有情人终成眷属，愿你在尘世获得幸福，我只愿面朝大还，春暖花开。')
w.to_file('./res/img/output2.png')