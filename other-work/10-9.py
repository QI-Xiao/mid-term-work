# -*- coding: utf-8 -*-

import re

with open('words.txt', encoding='utf8') as f:
    result = f.read()

total_words = re.findall(r'[A-z]+', result) # 对于can't这种单词会被认为是两个词，应怎么考虑

print(total_words)
print('There are %d words in word.txt.' % len(total_words))
