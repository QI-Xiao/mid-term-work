# -*- coding: utf-8 -*-
import re

with open('from.txt', encoding='utf8') as f:
    report = f.read()

to_txt = re.findall(r'[A-z]+', report)

# to_txt = sorted([x for x in to_txt], key=lambda x:x[0], reverse= False) 很傻逼了。。。
to_txt = sorted(to_txt)
to_txt = '\n'.join(to_txt)
print(to_txt)
with open('to.txt','w', encoding='utf8') as f:
    f.write(to_txt)
