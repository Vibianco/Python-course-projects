#la función
def computepay(h,r):
    if h <= 40 :
        pay = h * r
    else :
        pay = (40.00 * r) + ((h - 40.00)*(1.50 * r))
    return pay

#inputs
hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

#conversión y error
try :
    h = float(hrs)
    r = float(rate)
except :
    print("Error, please enter numeric input")
    quit()

#final
p = computepay(h,r)
print("Pay",p)
