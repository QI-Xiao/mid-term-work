# -*- coding: utf-8 -*-

import os

def findfile (key, inputdir= '.'):
    found_list = []
    for path, dirnames, filenames in os.walk(inputdir):  #dirnames 此处并没有用，只是为了格式
        print ('searching', path, '...')
        for n in filenames:
            full_name = path + '/' + n
            if key in n:
                found_list.append(full_name)
            with open(full_name) as f:
                for l in f.readlines():
                    if key in l:
                        found_list.append(full_name + ':' + l)
    return found_list

keyword = input('search:')
path = input('in:')
if not path.strip():
    path = '.'

result = findfile(keyword, path)

print ('\n============ result ============\n\n')
for i in result:
    print (i)