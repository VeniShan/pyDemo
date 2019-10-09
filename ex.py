fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
dic = dict()
mail = None
max = 0
maxk  = None

fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    mail = line.split()[5].split(':')[0]
    dic[mail] = dic.get(mail, 0) + 1

#print(sorted([(k,v)for k,v in dic.items()]))
lst = sorted([(k,v)for k,v in dic.items()])
for (k,v) in lst:
    print(k,v)
