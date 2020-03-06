print ("**************************")
print ("* Activity 3-Conditional *")
print ("**************************")
name = input("Name:")
print ("Hello ",name, "!")
print ("--------------------------------")
x= input(" Enter Hours:")
hours = float(x)
z= input (" Enter Rate:")
rate = float(z)
if hours < 40:
    compute= hours * rate
else:
    compute=(40*10)+((hours-40)*(rate*1.5))
print ("---------------------------------")
print (" Pay: ", compute)
