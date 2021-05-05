import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
ecount = input('Enter count: ')
pos = input('Enter position: ')
count = int(ecount)
position = int(pos)

print('Retrieving:', url)

while count > 0:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    mytag = tags[position - 1]
    print('Retrieving:', mytag.get('href', None))

    url = mytag.get('href', None)
    count = count - 1
