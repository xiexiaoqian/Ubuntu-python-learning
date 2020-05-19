"""
Counter: 分析数据时统计计数
"""
from collections import Counter
# 用list统计
sku_purchase = [3, 5, 6, 2, 6, 9, 5, 7, 8, 4, 7, 6, 2, 1, 9, 0]

d = {}
for i in sku_purchase:
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1

d_most = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# 最受欢迎的商品（键为商品编号），排序结果：
print(d_most)

# 使用Counter，一行搞定，并且输出按照购买次数的由大到小排序好的列表
print(Counter(sku_purchase).most_common())
# 除此之外，还能还素统计一句话中单词出现次数，一个单词中字符出现次数
print(Counter('I do do do love you').most_common())

