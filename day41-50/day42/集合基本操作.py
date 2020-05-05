"""
集合基本操作
"""

# 创建，也是{}，但容器内的元素不是键值对
a = {1, 2, 3}
print(a)

# 也可以用内置的set函数创建
b = set([1, 3, 5, 7])
print(b)

# 常用方法：集合间的并、交、差集、子集判断
# 求并集
a = {1, 3, 5, 7}
b, c = {3, 4, 5, 6},{6, 7, 8, 9}
d = a.union(b, c)

# 求差集
a = {1, 3, 5, 7}
b, c = {3, 4 ,5 ,6}, {6, 7, 8, 9}
d = a.difference(b, c)

# 求交集
a = {1, 3, 5, 7}
b, c = {3, 4, 5, 6}, {6, 7, 8, 9}
d = a.intersection(b, c)

# 判断a是否为b的子集
a = {1, 3, 5, 7}
b = {3, 4, 5, 6}
print(a.issubset(b))
print(a.issubset({1, 3, 5, 7, 8}))

