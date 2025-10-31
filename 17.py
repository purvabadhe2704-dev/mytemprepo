# another example of Input/Output function
Rollno = int(input('Enter Rollno : '))
Name = input('Enter Name :')
Physics = int(input('Enter Physics marks : '))
Chemistry = int(input('Enter chemistry marks : '))
Maths = int(input('Enter maths marks : '))

gt = Physics + Chemistry + Maths
Percentage = gt / 3.0
print(f'Rollno {Rollno} Name = {Name} Gt = {gt} Percentage')