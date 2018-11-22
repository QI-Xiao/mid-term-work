import requests
req = requests.get('http://www.baidu.com')
print (req)
print (req.encoding)
req.encoding = 'utf8'
print (req.text)
print (type(req.text))

# import requests
# req2 = requests.get('http://api.douban.com/v2/movie/top250')
# print (req2)   # http协议，200，404,400
# #print (req2.text)    # 输出text
# print (type(req2.text))    # 字符类型
# print (req2.status_code)   # 状态保存于status_code
# if req2.status_code == requests.codes.ok:
#     print ('success')
#
# req3_header = {
#     'User-Agent':'Chrome'
# }
# req3 = requests.get('https://xueqiu.com/p/discover',headers = req3_header)
# print (req3.text)
#
# try:
#     req4 = requests.get('https://www.google.com',timeout = 1)
#     print (req4.text)
# except:
#     print ('timeout')
#
#
# #data = req2.json()
# #print (data)
# #print (type(data))
# #print (data['title'])
