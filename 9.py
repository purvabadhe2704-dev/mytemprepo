# 1. print() function in python
rad = 13
areac = 3.14* (rad * rad)

# 1. Concentration method with + symbol and str()
print('Radius = ' +str(rad) + 'Area of circle = ' +str(areac))
# 2. comma os a data separator method
print('Radius =',rad,' Area of circle = ',areac)
# 3. formatted string method 
print(f'Radius={rad} Area of circle = {areac}') # {} are called place holders
# 4. print() with format() function
print('Radius = {} Area of circle = {}'.format(rad,areac))
