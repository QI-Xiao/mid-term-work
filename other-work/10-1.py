import urllib.request
import urllib.parse

word = input ('search:\n')
word = urllib.parse.quote(word)
url = 'http://www.baidu.com/s?wd=%s'%word
print (url)
req = urllib.request.urlopen(url)
data = req.read().decode('utf8')
print("------------")
print (req)
print ('++++++++++')
print (data)
with open ('search.html', 'w') as f:
    f.write(data).encode('utf8')