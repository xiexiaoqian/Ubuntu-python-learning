"""
迭代器节省内存的写法
"""

# 求一组数据累积乘

# 一般方法
# 这个方法开辟一段新内存rtn, 空间复杂度为O(n)
def accumulate_div(a):
    if a is None or len(a) == 0:
        return []
    rtn = [a[0]]
    for i in a[1:]:
        rtn.append(i*rtn[-1])
    return rtn

rtn = accumulate_div([1, 2, 3, 4])
print(rtn)

# 更节省内存的写法
def accumulate_div_new(a):
    if a is None or len(a) == 0:
        return []
    it = iter(a)
    total = next(it)
    yield total
    for i in it:
        total = total * i
        yield total

# 调用生成器函数 accumulate_div, 结合 for，输出结果
acc = accumulate_div([1, 2, 3, 4])
for i in acc:
    print(i, end=' ')

print()

# 直接转化为list
rtn = list(accumulate_div_new([1, 2, 3, 4]))
print(rtn)
