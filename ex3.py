import re
fname = input("Enter file:")
if len(fname) < 1 : fname = "regex_sum_297360.txt"
sm = 0

fh = open(fname)
str = fh.read()
lst = re.findall('[0-9]+', str)
for i in lst:
    sm = sm + int(i)
print(sm)
