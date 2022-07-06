import re
x = 'My two favorite numbers are -27 and 38'
y = re.findall('[]+',x)
print(y)
