print ("**************************")
print ("* Activity 3-Conditional *")
print ("**************************")
name = input("Name:")
print ("Hello ",name, "!")
print ("--------------------------------")
def computepay(hours,rate):
    print (" Conversion:", hours, rate)

    if hours < 40:
        compute= hours * rate
    else:
        compute=(40*10)+((hours-40)*(rate*1.5))
    print (" Returning: ", compute)
    return compute

x= input(" Enter Hours:")
z= input (" Enter Rate:")
hour1 = float(x)
rate1 = float(z)

payment=computepay(hour1,rate1)
print ("---------------------------------")
print (" Pay: ", payment)
