lis = ['li', 'st']

# 末尾追加元素
lis.append('hello')
print(lis)

lis2 = ['and', 'hello']
lis.append(lis2)
print(lis)

# 末尾追加另一个列表
lis.extend(lis2)
print(lis)

# 指定位置插入元素
lis.insert(1, 'insert')
print(lis)

# 删除指定元素
del lis[2]
print(lis)

# 修改指定元素
lis[0] = 'one'
print(lis)

# 查找指定元素
print(lis[3])

# 切片
print(lis[3:])

# 从倒数第几个开始截取
print(lis[-4:])

# 逆序
print(lis[::-1])

# 降序
lis3 = ['mango', 'watermelon', 'apple']
lis3.sort(reverse=True)
print(lis3)










