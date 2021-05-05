import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
data = data.decode()
tree = ET.fromstring(data)

suma = 0
comments = tree.findall('.//comment')
for item in comments:
    num = item.find('count').text
    numc = int(num)
    suma = suma + numc
print('Count:', len(comments))
print('Sum:', suma)
