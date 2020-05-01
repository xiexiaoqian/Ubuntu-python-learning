"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和字数构成
"""

import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    ：param code_len: 验证码的长度（默认4个字符）
    ：return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


# 调用函数
code = generate_code(6)
print('随机验证码：', code)


"""
判断传入的文件是否为图片类型的文件
并返回所有图片类型的文件
"""


def img_type(file_list):
    image_type = ['png', 'jpg', 'webp', 'bmp']
    nfile_list = []
    for file_name in file_list:
        # 以小数点切割文件名，获取切割的最后一个结果
        curr_type = file_name.split('.')[-1]
        
        if curr_type in image_type:
            nfile_list.append(file_name)
    return nfile_list

def img_type_v2(file_list):
    image_type = ['png', 'jpg', 'webp', 'bmp']
    nfile_list = []
    for file_name in file_list:
        for target in image_type:
            if file_name.endswith(target):
                nfile_list.append(file_name)
    return nfile_list

"""
判断一组文件中图片的个数
"""


def count_img(file_list):
    count = 0
    for file in file_list:

        if file.endswith('png') or file.endswith('jpg') \
            or file.endswith('webp') or file.endswith('bmp'):
            count += 1
    return count


if __name__ == "__main__":
    file_list = ['1.jpg', '2.2.bmp', '3.webp', '4.png', '5.6.zip']

    print('返回图片类型的文件：', img_type(file_list))
    print('返回图片类型的文件v2：', img_type_v2(file_list))

    print('一组文件中图片的个数：', count_img(file_list) )
    


