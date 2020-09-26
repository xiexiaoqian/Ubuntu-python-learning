# 元组
tup = (1, 2, 3, 4, 5)

# 重新赋值，以实现“改变”效果
tup = (2, 3)

# 将整个元组删除,打印 tup会抛出 tup 未定义异常
del tup
# print(tup)

# 为了区分数学运算中的小括号，元组定义数字时，后加逗号 以区分
tup = (1,)
num = (1 * 6)
print(type(tup), type(num))

