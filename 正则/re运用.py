'''
re.search(pattern，string ，flags = 0)              返回match对象
re.match(pattern，string ，flags = 0)               返回match对象
re.findall(pattern，string ，flags = 0)
re.split(pattern，string ，maxsplit = 0,flags = 0)
re.finditer(pattern，string ，flags = 0)            返回match对象
re.sub(pattern，repl，string ，count =0，flags = 0)

pattern ：正则表达式
string ： 待匹配字符串
flags ：
    re.I ： 忽略大小写
    re.M ：正则表达式中的^操作符能够将给定的字符串的每行当作匹配的开始
    re.S ：正则表达式中的.操作符能够匹配所有操作符，默认匹配出换行外的所有字符
maxsplit ：最大分割数，剩余部分当做一个输出
repl ：替换匹配字符串的字符
count ：匹配的最大替换次数

'''

import re


#面对对象用法
'''
compile(pattern,flags = 0)
'''
regex = re.compile(r'[1-9]\d{5}')
match = re.search(regex,'FA100081 GSD1000841')
print(match.group(0))


#函数用法

#re.search(pattern，string ，flags = 0)
#查找一个
'''
match = re.search(r'[1-9]\d{5}','BIT 1000811')
if match:
    print(match)
    #<_sre.SRE_Match object; span=(2, 8), match='100081'>
    print(match.group(0))
'''
#re.match(pattern，string ，flags = 0)
#从开头开始查找
'''
match = re.match(r'[1-9]\d{5}','BIT 1000811')
if match:
    print(match.group(0))
print(match.group(0))
#AttributeError: 'NoneType' object has no attribute 'group'

match = re.match(r'[1-9]\d{5}','1000811 BIT')
print(match.group(0)) 
'''
#re.findall(pattern，string ，flags = 0)
#查找全部
'''
ls = re.findall(r'[1-9]\d{5}','FA100081 GSD1000841')
print(ls)
print(type(ls))
'''
#re.split(pattern，string ，maxsplit = 0,flags = 0)
#切割,返回剩下的字符串
'''
ls = re.split(r'[1-9]\d{5}','FA100081 GSD100081 1512',maxsplit = 2)
print(ls)
'''
#re.finditer(pattern，string ，flags = 0)
#可迭代
'''
for i in re.finditer(r'[1-9]\d{5}','FA100081 GSD1000841 1512'):
    if i:
        print(i.group(0))
'''
#re.sub(pattern，repl，string ，count =0，flags = 0)
#替代
'''
m = re.sub(r'[1-9]\d{5}','grewgtr','FA100081 GSD1000841 1512')
print(m)
print(type(m))
'''
