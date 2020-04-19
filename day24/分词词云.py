# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
# 构建并配置词云对象w
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#6c909e',
    colormap='GnBu',
    font_path='./res/font/SimHei.ttf'
)

# 调用jieba的lcut()方法对原始文本进行中文分词，得到string

txt = '根据2016年10月学校官网显示，学校毗邻著名的南京钟山风景区，有仙林、中山、天堂三个校区，占地面积1360余亩，建筑面积40余万平方米；\
    教学科研仪器设备总值1.8亿元，馆藏图书百万余册；设有10院2部，开设53个专业；\
    教职员工800余人，在校生近14000人，其中专科生13000余人，本科生近1000人，外国留学生近100人。'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的general()方法，给词云输入文字
w.generate(string)

# 将词云图片导出当前文件夹
w.to_file('./res/img/output4.png')