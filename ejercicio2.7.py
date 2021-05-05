name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = {}
lst = []

for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    hours = words[5]
    hour = hours.split(':')
    h = hour[0]
    counts[h] = counts.get(h,0) + 1

for key,val in counts.items():
    newtup = (key,val)
    lst.append(newtup)
lst = sorted(lst)
for key, val in lst[:]:
    print(key, val)
