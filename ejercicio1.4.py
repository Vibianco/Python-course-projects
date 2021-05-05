largest = None
smallest = None

#loop
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    #error
    try :
        number = int(num)
    except :
        print("Invalid input")
        continue
    #máximo y mínimo
    for the_num in [number] :
        if smallest is None :
            smallest = the_num
        elif the_num < smallest :
            smallest = the_num
        if largest is None :
            largest = the_num
        elif the_num > largest :
            largest = the_num
#prints
print("Maximum is", largest)
print("Minimum is", smallest)
