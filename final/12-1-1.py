# -*- coding: utf-8 -*-

import requests
import re
import os
import threading


# 获取网址
def get_url(i, reqHeader):
    url = r'https://www.qiushibaike.com/pic/page/%d/?s=5144405' % i
    req = requests.get(url, headers=reqHeader)
    picUrl = re.findall(r'src="(\S*\.jpg)"', req.text)
    return picUrl


# 下载图片
def save_content(j, reqHeader):
    picGet = requests.get('http:' + j, headers=reqHeader)
    piclocal = r'picture\%s' % str(j.split('/')[-1])
    with open(piclocal, 'wb') as f:
        f.write(picGet.content)


if __name__ == '__main__':
    i_begin = int(input('请输入起始页：'))
    i_end = int(input('请输入结束页：'))
    temperary_save = []  # 将每一页的内容放在一起，共同抓取
    reqHeader = {'User-Agent': 'Chrome'}

    for i in range(i_begin, i_end + 1):
        picUrl = get_url(i, reqHeader)
        temperary_save += picUrl

    threads = []
    files = range(len(temperary_save))

    direxist = os.path.isdir('picture')
    if not direxist:
        os.mkdir('picture')

    for i in files:  # 创建线程
        t = threading.Thread(target=save_content, args=(temperary_save[i],reqHeader))
        threads.append(t)
    for i in files:  # 启动线程
        threads[i].start()
    for i in files:
        threads[i].join()
        # print('%s 下载完成' % temperary_save[i].split('/')[-1])
        # 这里应该不能print，没有找到一个线程结束后print的方法
    print('结束下载')
