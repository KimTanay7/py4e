print ("**************************")
print ("* Activity 3-Conditional *")
print ("**************************")
name = input("Name:")
print ("Hello ",name, "!")
print ("This program will print a grade relevant to your score")
print (" Please enter score between 0.0 to 1.0")
print ("--------------------------------")

x= input ('Enter Score:')
try:
    ival=float(x) or int(x)

except:
    ival=-1
if ival > 0:
    grade=float(x)
    if grade < 0.6:
        print('F')
    elif grade < 0.7:
        print('D')
    elif grade < 0.8:
        print('C')
    elif grade < 0.9:
        print('B')
    elif grade <= 1.0:
        print('A')
    else:
        print('Invalid!')
else:
    print('Invalid!')
