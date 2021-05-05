# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
sum = 0.0
count = 0
#mensaje de error
try:
    fh = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()
#sumar y promediar
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    izq = line.find(': ')
    num = line[izq+2:]
    numf = float(num)
    print(numf)
    for value in line:
        sum = sum + numf
        count = count + 1

print("Done")
print("Average spam confidence:", sum / count)
