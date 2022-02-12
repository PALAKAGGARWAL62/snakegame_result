# Type casting

print('String Conversions')
s = '34'
print(type(s))
si = int(s)
print(' Type of ',si , 'is ', type(si))
print(' Type of ',int(s) , 'is ', type(int(s)))

sf = float(s)
print(' Type of ',sf , 'is ', type(sf))

sb = bool(s)
print(' Type of ',sb , 'is ', type(sb))

print('integer Conversions')
i = 100
print(' Type of ',i , 'is ', type(i))
print(' Type of ',str(i) , 'is ', type(str(i)))
print(' Type of ',float(i) , 'is ', type(float(i)))
print(' Type of ',bool(i) , 'is ', type(bool(i)))

print('float Conversions')
i = 10.56
print(' Type of ',i , 'is ', type(i))
print(' Type of ',str(i) , 'is ', type(str(i)))
print(' Type of ',int(i) , 'is ', type(int(i)))
print(' Type of ',bool(i) , 'is ', type(bool(i)))

b = False
print(str(b))
print(int(b))
print(float(b))


print('string Conversions')
i = '1050'
print(' Type of ',i , 'is ', type(i))
print(' Type of ',int(i) , 'is ', type(int(i)))
print(' Type of ',float(i) , 'is ', type(float(i)))
print(' Type of ',bool(i) , 'is ', type(bool(i)))


# implicit type conversion
d = 5/2
print(type(d))


# joining the strings
#, +
candies = 10
chocolate = 12
print('I have',candies, 'Candies and', chocolate, 'Chocolates')
print('I have '+ str(candies) + ' Candies and ' + str(chocolate) + ' Chocolates')

s1 = '23'
s2 = '34'
print(s1+s2)
add = int(s1)+int(s2)
print(add)

