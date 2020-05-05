"""
查找当前目录所有文件
"""
import os
from pyecharts.charts import Pie
from pyecharts import options as opts

result = []
# 获取当前目录所有文件（含子目录）
def get_all(cwd):
    # 遍历当前目录，获取文件列表，
    get_dir = os.listdir(cwd)
    # print(get_dir)
    for i in get_dir:
        # print(i)
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)
            # print(file_name)
            result.append(file_name)
    return result


# 获取文件后缀
def get_sufname(file_list):
    result = []
    # print(file_list)
    for file in file_list:
        suf = os.path.splitext(file)[-1][1:]
        # print(suf)
        result.append(suf)
    return result


# 统计各类型文件数量
def file_count(sufname_list):
    dict = {}
    for i in sufname_list:
        # 如果元素之前在字典里，则对应的value增加
        if i in dict.keys():
            dict[i] = int(dict[i]) + 1
        # 如果不在，字典中新增对应的items
        else:
            dict[i] = 1
    # print(dict.values())
    list_count = list(dict.values())
    return list_count


# 画图
def drawPie(sufname, data):
    count = file_count(sufname)
    sufname = list(set(sufname))
    print(count, sufname)
    c = (
        Pie().add(
            "", data_pair=[list(z) for z in zip(sufname, count)],
            radius=["40%", "75%"]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="文件类型统计"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%"
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render(path='./res/pie.html')


if __name__ == "__main__":
    # 取得当前目录, 拼上子目录
    cur_path = os.getcwd() + '/res'
    # print(cur_path)
    # 调用函数，统计res目录下文件
    # print('当前目录的所有文件', get_all(cur_path))
    sufname = get_sufname(get_all(cur_path))
    drawPie(sufname, get_all(cur_path))
