import urllib.request
import json

url = 'http://api.douban.com/v2/movie/top250'
req = urllib.request.urlopen(url)
data = req.read()
#print (data)
data_dict = json.loads(data)  #转成字典
print (type(data_dict))
print(data_dict.keys())
print (data_dict['title'])
