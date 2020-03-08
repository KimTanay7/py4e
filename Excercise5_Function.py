print ("***********************")
print ("* Activity 5-Function *")
print ("***********************")
name = input("Name:")
print ("Hello ",name, "!")
print ("This program will print a grade relevant to your score")
print (" Please enter score between 0.0 to 1.0")
print ("--------------------------------")
def computegrade(scores):
     try:
         ival=float(scores) or int(scores)

     except:
         ival=-1
     if ival > 0:
         grade=float(scores)
         print ("Conversion:", grade)
         if grade < 0.6:
             sgrade=str(grade)
             cgrade='F'
             print('Return: ', cgrade)
             return cgrade
         elif grade < 0.7:
             sgrade=str(grade)
             cgrade='D'
             print('Return: ', cgrade)
             return cgrade
         elif grade < 0.8:
             sgrade=str(grade)
             cgrade='C'
             print('Return: ', cgrade)
             return cgrade
         elif grade < 0.9:
             sgrade=str(grade)
             cgrade='B'
             print('Return: ', cgrade)
             return cgrade
         elif grade <= 1.0:
             sgrade=str(grade)
             cgrade='A'
             print('Return: ', cgrade)
             return cgrade
         else:
             print('Invalid!')
     else:
         print('Invalid!')


x= input ('Enter Score:')
grade=computegrade(x)
print ("---------------------------------")
print (" Grade: ", grade)
