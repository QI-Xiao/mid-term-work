import urllib.request
import urllib.parse

req = urllib.request.urlopen('http://www.baidu.com')
data = req.read().decode('utf8')
with open('baidu.html', 'w', encoding='utf8') as f:
    f.write(data)


# word = input('search;\n')
# word = urllib.parse.quote(word)
# url = 'http://www.baidu.com/s?wd%s' % word
# print (url)
# req = urllib.request.urlopen(url)
# data = req.read().decode('utf8')
# with open('search.html', 'w',encoding='utf8') as f:
#     f.write(data)

import urllib.request
import json
url = 'https://api.douban.com/v2/movie/top250'
req = urllib.request.urlopen(url)
data = req.read().decode('utf8')
data_dic = json.loads(data)
print(type(data_dic))
print(data_dic.keys())
print(data_dic['title'])
