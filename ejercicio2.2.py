# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()

inp = fh.read()
rtd = inp.upper()
for line in rtd:
    line = line.rstrip()
print(rtd)
