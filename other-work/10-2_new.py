import re

string = 'Crossin 编程123教室 hi2333.'


result = re.findall(r'\s.i', string)
print(result)