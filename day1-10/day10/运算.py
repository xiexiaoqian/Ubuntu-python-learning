#交集、并集、差集、对称差运算

set1 = {9, 8, 7, 6, 5, 5, 5}
print(set1)
print('set1-Length = ',len(set1))
#构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 4, 5, 5))

print(set1 & set2)
print(set1.intersection(set2))
print(set1 | set2)
print(set1.union(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))
print(set3 <= set2)
print(set3.issubset(set2))
print(set1 >= set2)
print(set1.issuperset(set2))
print(set2 >= set3)
print(set2.issuperset(set3))

