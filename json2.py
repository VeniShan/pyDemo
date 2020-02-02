import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_297365.json'
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
info = json.loads(data)
print('User count:', len(info['comments']))
summ = 0
print(info['comments'][0]['name'])
for item in info['comments']:
    summ = summ + int(item['count'])
print(summ)
