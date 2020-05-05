#跑马灯
import os
import time

def main():
    content = '我爱小破站，小电视加油，小贴士：视频互动可以一定程度减少ta亏损'
    while True:
        #清理屏幕上的输出
        os.system('cl')    #os.system('clear')
        print(content)
        #休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]



if __name__ == '__main__':
    main()