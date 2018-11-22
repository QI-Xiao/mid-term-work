import re

text = "Hi, I am Shirley Hilton 123. I am his wife. 456"

# 取出 text 中所有的数字
m = re.findall(r'[A-z]+', text)
print (m)

# 取出 text 中所有的单词（不包括数字）

n = re.findall( r'[0-9]+', text)
print (n)
