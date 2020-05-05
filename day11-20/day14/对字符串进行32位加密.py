"""
对字符串进行32位加密
"""

import hashlib
#对字符串s实现32位加密

def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()


print(hash_cry32(123))       #202cb962ac59075b964b07152d234b70
print(hash_cry32('hello'))  #5d41402abc4b2a76b9719d911017c592