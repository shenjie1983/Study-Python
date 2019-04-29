import re

s = 'abc, acc, adc, aec, afc, ahc'

r = re.findall('a[A-Z]c', s)

print(r)