fname = input("Enter file name: ")
handle = open(fname)
import re
suma = 0

for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    for value in stuff:
        nro = int(value)
        suma = suma + nro

print(suma)
