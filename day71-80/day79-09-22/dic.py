dic1 = {'name': '猫荷','age': 21,}
print(dic1)

# 增
dic1['school'] = 'NJUIT'
print(dic1)

# 删
# del dict['school']
# print()

# 改
dic1['name'] = '改他！'
print(dic1)

# 查
print(dic1['name'])

dic1.clear()
print(dic1)

# 字典中的key必须是不可变对象
# 同一个键被赋值两次，前一个会被覆盖