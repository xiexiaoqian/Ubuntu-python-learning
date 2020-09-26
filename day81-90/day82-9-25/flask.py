import flask
import numpy as np

str = 'oooitcast and itheimaooo'
# 查找'it'在字符串中的索引
it_index = str.index('it')
if (it_index):
    print(it_index)
else:
    print('无法找到‘it’字符')

# 判断'it'在字符串中出现的次数
print(str.count('it'))

# 替换‘ooo’为空格
new_str = str.replace('ooo', ' ')
print(new_str)

# 将字符串全部转为大写
print(str.upper())

