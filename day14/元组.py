"""
元组类型练习
"""

#定义元组
t = ('张晨', 18, True, '四川成都')
print(t)            #('张晨', 18, True, '四川成都')
# 获取元组中的元素
print(t[0])         #张晨
# 遍历元组中的值
for member in t:
    print(member)   #张晨   18   Trueb   四川成都
# 重新给元组赋值,是不行的
# t[0] = '小黑'     #TypeError: 'tuple' object does not support item assignment
# 变量t重新引用了新的元组，原来的则被回收
t = ('小黑', 20, True, '云南昆明')
print(t)            #('小黑', 20, True, '云南昆明')
# 将元组转换成列表
person = list(t)
print(person)       #['小黑', 20, True, '云南昆明']
# 列表是可以修改它的元素的
person[0] = '小白' 
person[1] = 25
print(person)       #['小白', 25, True, '云南昆明']
# 将列表转换成元组
fruits_list = ['watermelon', 'mango', 'pitaya']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)     #('watermelon', 'mango', 'pitaya')