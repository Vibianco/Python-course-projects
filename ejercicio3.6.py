import urllib.request, urllib.parse, urllib.error
import json
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
js = json.loads(data)

suma = 0
loop = js['comments']
for item in loop:
    num = item['count']
    numc = int(num)
    suma = suma + numc
print('Count:', len(loop))
print('Sum:', suma)
