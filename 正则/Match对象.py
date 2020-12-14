import re
'''
.string ：待匹配的文本
.re ：匹配是使用的正则表达式（patter对象）
.pos ；正则表达式搜索文本的开始位置
.enpos ；正则表达式搜索文本的结束位置

.group(0) ：获得匹配后的字符串
.start() ：匹配的字符串在原始字符串的开始位置
.start() ：匹配的字符串在原始字符串的结束位置
.span() ：返回(.start(),.end())
'''
match = re.search(r'[1-9]\d{5}','RIT 100081')
if match:
    print(match.group(0))