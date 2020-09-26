"""
函数的学习
def关键字开头，后接函数标识符名称和圆括号
函数内容以冒泡起始，并且缩进
return[表达式]结束函数，选择性地返回一个值给调用方，不带表达式的return相当于返回None
任何传入参数和自变量必须放在圆括号中间
无参方法
"""

'''
isalnum()方法，判断字符串是否是由数字组成，但可能对中文无效，
    需先将字符串用encode()编码 -> 将str型转为bytes型
islower()方法，判断字符串是否由小写字母组成（判断过程中，会自动避过中文）

'''

import re


# def get_isword(str):
#     if str.isalnum():
#         if str.islower():
#             print('字符串由数字和小写字母构成')
#     else:
#         print("字符串不是数字或小写字母")

def get_str(str):
    low = 0
    digit = 0
    upper = 0
    i = 0
    while i < len(str):
        if str[i].isalnum:
            if str[i].islower():
                low += 1
            if str[i].isdigit():
                digit += 1
            if str[i].isupper():
                upper += 1
        i += 1
    if low != 0 and digit != 0 and upper == 0:
        print('字符串由小写字母和数字组成')
    else:
        print('字符串不符合规范')


def check_str():
    '''
    作用：让用户输入一个字符串，判断是否符合 “只包含小写字母和数字” 的要求
    :return: answer
    '''
    text = input('请输入字符串：')
    answer = text.encode().isalnum() and text.islower()
    print('该字符串是否满足要求：{}'.format(answer))
    return answer


#
# def get_word_type:
#     s = input('输入一串字符：')
#     char = re.findall(r'[a-z]', s)
#     bigchar = re.findall(r'[A-Z]', s)
#     num = re.findall(r'[0-9]', s)
#     blank = re.findall(r' ', s)
#     # \u4E00-\u9FFF是中文的范围
#     chi = re.findall(r'[\u4E00-\u9FFF]', s)
#     other = len(s) - len(char) - len(bigchar) - len(num) - len(blank) - len(chi)
#     print("小写字母：", len(char), "\n大写字母：", len(bigchar), "\n数字：", len(num), "\n空格：", len(blank), "\n中文：", len(chi),
#           "\n其他：", other)

if __name__ == '__main__':
    get_str('123456')
    get_str('abc123')
    get_str('cbA')
    check_str()
