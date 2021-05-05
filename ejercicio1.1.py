hrs = input("Enter Hours: ")
rate = input("Enter rate per hour: ")

#agregando al ejercicio try y except
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h <= 40 :
  pay = h * r
else :
  pay = (40.00 * r) + ((h - 40.00)*(1.50 * r))

print('Your pay is:',pay)
