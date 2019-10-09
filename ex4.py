# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cn = input('Enter - ')
ps = input('Enter - ')

for i in range(int(cn)):
    if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Aisa.html'
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags[:int(ps)]:
        url = tag.get('href', None)

print(url)
