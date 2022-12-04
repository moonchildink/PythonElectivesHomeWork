"""
10.	使用不超过三条语句，生成一个字典，字典的键分别是52个大小写字母，其值为对应的ASCII值。
"""

import string

li = list(map(ord,[letter for letter in string.ascii_letters]))
d = dict(zip([letter for letter in string.ascii_letters],li))
print(d)