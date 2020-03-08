print ("************************")
print ("* Activity 6-Iteration *")
print ("************************")
name = input("Name:")
print ("Hello ",name, "!")
print ("--------------------------------")
count=0
total=0
average=0
small= None
large= -1
while True:
    num= input (" Enter a number:")
    if num == 'done':
        break
    try :
        number= float(num)
    except:
        print (' Invalid Input')
        continue
    if small is None:
        small = number
    elif number < small:
        small = number
    if number  > large:
        large = number
    count = count+1
    total=total+ number

print('------------------------------')
print(' Count:', count)
print(' Total:', total)
print(' Largest Number:', large)
print(' Smallest Number:', small)
