#file
fname = input("Enter file name: ")
fh = open(fname)
bigstr = fh.read()

#listas
lst = list()
wordlst = list()
lst = bigstr.split()

#acciones
for thing in lst:
    if thing not in wordlst:
        wordlst.append(thing)
wordlst.sort()
print(wordlst)
