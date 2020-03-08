print ("************************")
print ("* Activity 6-Iteration *")
print ("************************")
name = input("Name:")
print ("Hello ",name, "!")
print ("--------------------------------")
count=0
total=0
average=0
while True:
    num= input (" Enter a number:")
    if num == 'done':
        break
    try :
        number= float(num)
    except:
        print (' Invalid Input')
        continue
    count = count+1
    total=total+ number
    average=total/count
print('------------------------------')
print(' Count:', count)
print(' Total:', total)
print(' Average:', average)
