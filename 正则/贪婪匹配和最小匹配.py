import re

#贪婪匹配
match = re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0))

#最小匹配
match = re.search(r'PY.?N','PYANBNCNDN')
print(match.group(0))