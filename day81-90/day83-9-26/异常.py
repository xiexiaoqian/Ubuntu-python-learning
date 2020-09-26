"""
异常
 常见异常：NameError -> 访问为申明变量
        ZeroDivisionError -> 初灵错误
        SyntaxErrot -> 解释器语法错误
        IndexError -> 索引超出序列范围
        KeyEooro -> 访问不存在的Key
        IOError -> 输入、输出错误
        AttributeError -> 访问未知的对象属性
        所有的错误类型都继承自 -> BaseException
"""


def catch_exception():
    # 声明x为局部变量
    x = 0
    # 将input方法返回的str类型转为int类型
    num = int(input('请输入被除数：'))
    try:
        x = 58 / num
    except ZeroDivisionError:
        print('除零异常：被除数不能为 ‘0’ ！')
    else:
        print(x)
    return x


if __name__ == '__main__':
    catch_exception()

'''
遇到的问题：
    UnboundLocalError： local variable 'xxx' referenced before assignment
    主要是因为没有让解释器清楚变量是全局变量还是局部变量。执行return 和 print 自然会抛出 UnboundLocalError

解决方法：
    1、在 Python 中，若要声明该变量为局部变量，则给变量赋初值 -> x = 0
    2、若要声明为全局变量，则使用 global 关键字 -> global x
'''
