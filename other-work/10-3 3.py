import re
string ='sdfds@sdc.com  ' \
        ' dsfdsgdgdfg'
result1 =re.findall(r'.+@.+\..+',string)
print (result1)
print (string)
result2 =re.findall(r'.+@.+\..+','dsfdsgdgdfg')
print (result2)

result1 =re.findall(r'\S+@\S+\.\S+',string)
print (result1)