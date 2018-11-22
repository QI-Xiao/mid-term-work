import urllib.request
# url =  'http://flash.weather.com.cn/wmaps/xml/china.xml'
# req = urllib.request.urlopen(url)
# data = req.read()
# print (data)

url2 =  'http://m.weather.com.cn/data5/city.xml'
req2 = urllib.request.urlopen(url2)
data2 = req2.read()
print (type(data2))
data3 = data2.decode('utf8')
print (type(data3))
data_list = data3.split(',')   #字符串变列表
for d in data_list:
    print (d)