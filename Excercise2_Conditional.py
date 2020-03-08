print ("**************************")
print ("* Activity 2-Conditional *")
print ("**************************")
name = input("Name:")
print ("Hello ",name, "!")
print ("--------------------------------")
x= input( ' Enter Hours:')
try:
    ival=int(x)
except:
    ival=-1
while ival <= 0:
        print (' Error, please enter numeric input')
        print (' ')
        x= input( ' Enter Hours:')
        try:
            ival=int(x)
        except:
            ival=-1
if ival > 0:
    z= input (" Enter Rate:")
    try:
        ival=int(z)
    except:
        ival=-1
    while ival <=0:
        print (' Error, please enter numeric input')
        print (' ')
        print (' Enter Rate:', x)
        z= input (" Enter Rate:")
        try:
            ival=int(z)
        except:
            ival=-1
    if ival > 0:
        hours = float(x)
        rate = float(z)
        if hours < 40:
            compute= hours * rate
        else:
            compute=(40*10)+((hours-40)*(rate*1.5))
            print ("---------------------------------")
        print (" Pay: ", compute)
