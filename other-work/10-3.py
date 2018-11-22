import re

string = 'Hi, i am shirley hilton. i am his wife.'
string2 = 'I am chinese'
pattern = re.compile(r'\b[Hh]i\b') #为避免正则表达式被转译，前面加上r

result0 = pattern.findall(string)
print (result0)
result = pattern.match(string)
print (result)
if result:
    print (result.group())
result2 = pattern.findall(string2)
print (result2)