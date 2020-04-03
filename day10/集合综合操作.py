"""
集合综合操作
"""
#创建集合的各种方法
#字面量语法
set1 = {9, 8, 7, 6, 5, 5, 5}
print(set1)
print('Length = ',len(set1))
#构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 4, 5, 5))
print(set2,set3)
#推导式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

#集合添加删除元素
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)
